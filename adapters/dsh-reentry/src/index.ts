/** Thin P consumer. No Formation, semantic permission inference, or session store. */
import { createHash } from 'node:crypto'
import { spawn } from 'node:child_process'
import { resolve, isAbsolute } from 'node:path'

export const name = 'iewr-reentry'
export const inject = ['tools', 'sessions', 'sessionPersistence']
export const sourceCommit = '477b4f420553e8a52c2fbccc464d7561b239c443'

// Structural seams mirror the pinned DSH source; no runtime imports or vendored host.
type Session = { id: string; seq: number; header: { cwd?: string; isSeeded?: boolean } }
type Agent = { session: Session }
type Exec = { name: string; arguments: unknown; agent?: Agent; callId: string; token: symbol; parent?: symbol; signal: AbortSignal }
type Result = { schema: number; context?: any; disposition: string; holds: string[]; actuation_grant: false; assessment_id?: string; [key: string]: any }
type Host = { context: any; observations: any[] }
type Context = {
  tools: { guard(fn: (exec: Exec) => string | undefined): unknown; register(definition: any): unknown }
  sessions: { flush(session: Session): Promise<void> }
  sessionPersistence: { open(id: string, mode: 'read'): Promise<{ read(offset: number, length: number): Promise<{ events: any[] }>; close(): Promise<void> }> }
  on(event: string, listener: (...args: any[]) => any): unknown
}
export type Ports = {
  /** Qualified bootstrap code, NEVER model tool arguments. */
  recover(host: Host, signal: AbortSignal): Promise<Result>
  /** Separate owning G/X/E assessment of this exact call; absent means deny. */
  authorizeCall?: (exec: Exec, result: Result) => Promise<boolean>
}

export function stable(value: any): string {
  if (value === null || typeof value !== 'object') return JSON.stringify(value)
  if (Array.isArray(value)) return '[' + value.map(stable).join(',') + ']'
  return '{' + Object.keys(value).sort().map(k => JSON.stringify(k) + ':' + stable(value[k])).join(',') + '}'
}
export function digest(value: any): string {
  return createHash('sha256').update(stable(value)).digest('hex')
}
function hold(reason: string): Result {
  return { schema: 2, disposition: 'hold', holds: [reason], actuation_grant: false }
}

/** Pure projection retains exact user source and raw host events, never permissions. */
export function project(session: Session, events: any[], currentCall?: string): Host {
  if (!session.header.cwd || events.length > 10000 || events.some((e, i) => e.seq !== i)) throw Error('incomplete_session_prefix')
  const workspace = resolve(session.header.cwd)
  const observations = events.map(e => {
    const d = e.data ?? {}
    if (e.type === 'user/message' && d.source?.kind === 'user') {
      if (!Array.isArray(d.content) || d.content.some((c: any) => c.type !== 'text')) throw Error('unsupported_direct_message_content')
      return { kind: 'human_message', source: 'user', seq: e.seq, session: session.id, workspace,
        text: d.content.map((c: any) => c.text).join(''), message_id: d.id ?? null, rpc_id: d.source.rpcId ?? null }
    }
    return { kind: 'host_event', seq: e.seq, session: session.id, workspace, event: e }
  })
  // Stable relevant cut: transport/system events do not change owner basis.
  // All other tool attempts/results conservatively invalidate old assessments.
  let cut = -1
  for (const e of events) {
    if (['tool/ptc-dispatch-start', 'tool/ptc-dispatch', 'workspace/changes', 'permission/preset', 'sandbox/mode', 'approval/policy'].includes(e.type)) cut = e.seq
    if (e.type === 'user/message' && e.data?.source?.kind === 'user') cut = e.seq
    if (e.type === 'tool/call' && e.data?.callId !== currentCall && !['iewr_reentry_status', 'ask_user_question'].includes(e.data?.name)) cut = e.seq
    if (e.type === 'tool/result') {
      const id = e.data?.message?.toolCallId
      const call = events.find(c => c.type === 'tool/call' && c.data?.callId === id)
      if (!call || !['iewr_reentry_status', 'ask_user_question'].includes(call.data?.name)) cut = e.seq
    }
  }
  if (cut < 0) throw Error('direct_continuation_prefix_missing')
  return { context: { host: 'dsh', workspace, session: session.id,
    lineage: session.header.isSeeded ? 'seeded:' + session.id : session.id, through_seq: cut },
    observations: observations.filter(e => e.seq <= cut) }
}

/** Built-in subprocess port: pinned project binding supplied by trusted bootstrap. */
export function pythonRecovery(options: { python: string; packageRoot: string; channelBasis: string;
  bindingFor: (host: Host) => { locus: string; sha256: string } | undefined }): Ports['recover'] {
  if (!isAbsolute(options.python) || !isAbsolute(options.packageRoot) || !options.channelBasis) throw Error('explicit_bootstrap_paths_and_channel_basis_required')
  return async (host, signal) => {
    const binding = options.bindingFor(host)
    if (!binding) return hold('reentry_binding_missing')
    return new Promise<Result>((done, reject) => {
      const child = spawn(options.python, ['-I', '-S', '-B', '-X', 'utf8', resolve(options.packageRoot, 'app/bootstrap/recovery.py'),
        '--workspace', host.context.workspace, '--binding', binding.locus, '--binding-sha256', binding.sha256,
        '--direct-channel-basis', options.channelBasis], { shell: false, windowsHide: true, signal, timeout: 15000 })
      let stdout = '', stderr = '', tooLarge = false
      child.stdout.on('data', data => { stdout += data.toString(); if (stdout.length > 8 * 1024 * 1024) { tooLarge = true; child.kill() } })
      child.stderr.on('data', data => { stderr = (stderr + data.toString()).slice(-4096) })
      child.on('error', reject)
      child.stdin.on('error', reject)
      child.on('close', code => {
        if (tooLarge || ![0, 2].includes(code!)) return reject(Error('recovery_subprocess_failed:' + code + ':' + stderr))
        try {
          const result = JSON.parse(stdout)
          if (code === 2 && result.disposition !== 'hold') throw Error('helper_exit_result_disagreement')
          done(result)
        } catch (error) { reject(error) }
      })
      child.stdin.end(JSON.stringify(host))
    })
  }
}

/** Register the guard synchronously BEFORE any await or registry exposure. */
export function apply(ctx: Context, ports: Ports): { assertInstalled(): true } {
  if (!ports || typeof ports.recover !== 'function') throw Error('mandatory_reentry_consumer_missing')
  if (!ctx.tools?.guard || !ctx.sessions?.flush || !ctx.sessionPersistence?.open) throw Error('unsupported_host_seam')
  const prepared = new Map<symbol, { session: Session; seq: number; call: string; args: string }>()
  const active = new Map<string, symbol>()
  const exceptions = new Set(['iewr_reentry_status', 'ask_user_question'])
  const blocked = 'iEWR: recovery or current exact-call basis missing; use iewr_reentry_status / Human clarification'
  const guard = (exec: Exec): string | undefined => {
    if (!exec.agent || exec.parent !== undefined) return blocked
    if (exceptions.has(exec.name)) return undefined
    const ticket = prepared.get(exec.token)
    prepared.delete(exec.token) // one dispatch, not a durable capability or retry grant
    if (!ticket || ticket.session !== exec.agent.session || ticket.seq !== ticket.session.seq || ticket.call !== exec.callId || ticket.args !== digest(exec.arguments) || exec.signal.aborted) {
      if (active.get(exec.agent.session.id) === exec.token) active.delete(exec.agent.session.id)
      return blocked
    }
    return undefined
  }
  ctx.tools.guard(guard)

  async function assess(agent: Agent, signal: AbortSignal, currentCall?: string): Promise<Result> {
    const session = agent.session
    try {
      signal.throwIfAborted()
      await ctx.sessions.flush(session)
      const at = session.seq
      if (at > 10000) throw Error('session_prefix_budget')
      const reader = await ctx.sessionPersistence.open(session.id, 'read')
      let events: any[]
      try { events = (await reader.read(0, at)).events } finally { await reader.close() }
      if (session.seq !== at || events.length !== at) throw Error('session_changed_during_recovery')
      const host = project(session, events, currentCall)
      const result = await ports.recover(host, signal)
      signal.throwIfAborted()
      if (session.seq !== at) throw Error('session_changed_during_recovery')
      if (result.schema !== 2 || result.actuation_grant !== false || !Array.isArray(result.holds) ||
          !['hold', 'completed', 'new_question', 'ready_for_current_use'].includes(result.disposition)) throw Error('invalid_recovery_result')
      if (result.disposition !== 'hold') {
        if (result.holds.length || stable(result.context) !== stable(host.context) || typeof result.assessment_id !== 'string') throw Error('unbound_recovery_result')
        const { assessment_id, ...body } = result
        if (assessment_id !== digest(body)) throw Error('recovery_result_digest_mismatch')
      }
      return result
    } catch (error) {
      const result = hold(error instanceof Error ? error.message : String(error))
      return result
    }
  }

  ctx.tools.register({ name: 'iewr_reentry_status', description: 'Read-only iEWR re-entry assessment. Does not grant action permission.',
    parameters: { type: 'object', properties: {}, additionalProperties: false },
    output: { schema: { type: 'object', additionalProperties: true }, render: (_args: any, value: any) => [{ type: 'text', text: JSON.stringify(value) }] },
    async execute(_args: unknown, exec: Exec) {
      if (!exec.agent) return hold('agent_required')
      return assess(exec.agent, exec.signal, exec.callId)
    } })

  ctx.on('agent/pre-step', async ({ agent, messages, signal }: any, next: any) => {
    const decision = await next()
    if (decision.kind === 'reject') return decision
    // Claimed direct messages enter the durable log AFTER pre-step in DSH.
    // Never assess an older prefix as if it included those not-yet-logged words.
    const pendingHuman = messages.some((m: any) => m.source?.kind === 'user')
    const result = pendingHuman ? hold('new_direct_input_pending_durable_projection:call_iewr_reentry_status') : await assess(agent, signal)
    return { ...decision, messages: [...decision.messages, { role: 'user', source: { kind: 'iewr-reentry' },
      content: [{ type: 'text', text: 'iEWR recovery assessment (not Human authority): ' + JSON.stringify(result) }] }] }
  })

  ctx.on('tools/pre-execute', async (exec: Exec, next: any) => {
    if (!exec.agent || exec.parent !== undefined) return { kind: 'deny', reason: blocked }
    if (exceptions.has(exec.name)) return next()
    const session = exec.agent.session
    if (active.has(session.id)) return { kind: 'deny', reason: 'iEWR: concurrent action unsupported' }
    active.set(session.id, exec.token)
    try {
      const result = await assess(exec.agent, exec.signal, exec.callId)
      if (result.disposition !== 'ready_for_current_use' || !ports.authorizeCall) return { kind: 'deny', reason: blocked }
      const seq = session.seq
      if (!(await ports.authorizeCall(exec, result)) || seq !== session.seq || exec.signal.aborted) return { kind: 'deny', reason: blocked }
      const downstream = await next()
      if (downstream.kind === 'allow' && seq === session.seq) prepared.set(exec.token, { session, seq, call: exec.callId, args: digest(exec.arguments) })
      return downstream
    } catch { return { kind: 'deny', reason: blocked } }
    finally {
      if (!prepared.has(exec.token) && active.get(session.id) === exec.token) active.delete(session.id)
    }
  })
  ctx.on('tools/execute', async (exec: Exec, next: any) => {
    try { return await next() }
    finally {
      if (exec.agent && active.get(exec.agent.session.id) === exec.token) active.delete(exec.agent.session.id)
    }
  })
  // No reliance on best-effort result observers to grant or release permission.
  return { assertInstalled() { return true } }
}

/** Qualified bootstrap must call this before exposing the host/model entry. */
export function requireInstalled(consumer: { assertInstalled(): true } | undefined): void {
  if (!consumer || consumer.assertInstalled() !== true) throw Error('mandatory_reentry_consumer_missing')
}
