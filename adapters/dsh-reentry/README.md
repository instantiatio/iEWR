# DSH thin re-entry consumer (E-min)

Отдельный private package P, разработанный по pinned official DSH source
`477b4f420553e8a52c2fbccc464d7561b239c443`. В работающий DSH не установлен.
Observed qualification: offline contract harness + настоящий Python subprocess,
Windows, Node 24.18.0. Live DSH loader, actual plugin graph, model behavior и
upstream TypeScript type-check не квалифицированы.

Package расположен в `adapters/dsh-reentry/`, чтобы сохранить существующие product
trees и инструменты упаковки. Это тот отдельный P package, который RCA предлагал
как `integrations/dsh-reentry/`; смысл и границы не меняются. Runtime dependencies
не устанавливаются: Node исполняет erasable TypeScript, используются built-ins.

## Статус в поставке 5.5.4

Bundled consumer необязателен для ordinary instruction-led работы Codex, DSH
и других host. Он не подключается при распаковке ZIP. Обязательный bootstrap
ниже требуется только при выборе этой интеграции для технического контроля.
Python helper требует Python 3.10+; проверенная среда — Python 3.13.14 и Node
24.18.0. Версия companion согласована с candidate, а qualification остаётся offline.

## Граница и подключение

`apply(ctx, ports)` синхронно ставит monotonic `ctx.tools.guard`, затем регистрирует
read-only `iewr_reentry_status`, `agent/pre-step`, awaited `tools/pre-execute` и
`tools/execute`. Нужны штатные `tools`, `sessions`, `sessionPersistence`.
`sessionPersistence.open(id, 'read')`/`read`/`close` не создают второй session store.
Открытый read handle всегда закрывается. Snapshot ограничен 10 000 events; более
длинная/неполная история даёт точный hold, без усечения и recency selection.

Программный bootstrap после проверки actual host API должен выполнить:

```ts
import { apply, pythonRecovery, requireInstalled } from './src/index.ts'

const consumer = apply(ctx, {
  recover: pythonRecovery({
    python: absolutePythonExecutable,
    packageRoot: absoluteIEWRRoot,
    channelBasis: independentlyEstablishedDirectChannelReference,
    bindingFor: qualifiedCurrentBindingQuery, // host snapshot -> { locus, sha256 } | undefined
  }),
  // Необязательно. Без qualified owning G/X/E port никакие effect tools не открываются.
  authorizeCall: qualifiedExactCallAssessment,
})
requireInstalled(consumer)
// Только после этой проверки bootstrap может открыть agent/model entry.
```

Это contract программного bootstrap, не готовая YAML-конфигурация установленного
DSH. Нельзя выдать строку версии или наличие package за qualification actual loader.
`requireInstalled` должен находиться в обязательном startup пути host, а не в
необязательном plugin callback: отсутствующий plugin не может сам заблокировать
своё отсутствие. Unload/reload и изменение tool graph требуют остановки agent
entry и новой проверки bootstrap. Без этого rollout остаётся unsupported.

`ports` — independently bound код композиции, не model-facing API. `recover` и
`authorizeCall` нельзя принимать из JSON tools или файлов, которым агент сам
приписал доверие. `pythonRecovery` запускает pinned helper с `shell:false`, hidden
Windows process, timeout и output budget. Binding locus/hash выбирает qualified
query, а не аргументы модели. `channelBasis` обозначает уже установленное доверие;
сам параметр никого не аутентифицирует.

## Что удерживается

Cold consumer ничего не наследует от старой session. Before-model pre-step передаёт
read-only assessment; если новый direct input ещё находится в inbox и DSH пока
не записал его в log, передаётся точный hold с требованием вызвать status tool.
Так старая история не выдаётся за восстановление нового сообщения. Status tool
и pre-execute читают уже durable direct messages; до meaningful choice действует
инструкция iEWR. Нельзя технически доказать внутренний выбор модели одним guard.

На hold/completed/new_question разрешены только собственный read-only status tool
и штатный Human clarification `ask_user_question`. Имена и реализации этих tools
должны сохранять qualified identity в выбранном host graph. Иначе не подключать
consumer. Свободные read/shell команды не классифицируются как безопасные по тексту.

Effect dispatch требует одновременно `ready_for_current_use` от R и отдельный
положительный `authorizeCall(exec, result)` owning G/X/E port для exact arguments.
Порт устанавливает direct scope, отрицательные ограничения, capability, currentness
и разрешённое действие; consumer не выбирает Method или next action за owner.
Без такого порта consumer пригоден для безопасного completed/ambiguous recovery,
но не для самостоятельного нового исполнения. Это bounded v1, не полный G engine.

Разрешение переносится в одноразовый in-memory ticket для registry token/call/
arguments/session.seq; последующий monotonic guard только отказывает. Изменение
session после assessment/authorization, cancellation, malformed output или bypass
helper не открывают ticket. Concurrent material actions удерживаются до окончания
awaited body; ошибочный body не создаёт разрешение retry. Nested PTC/subagent/MCP/
background обход через данный registry удерживается, если не получил отдельный
квалифицированный direct route; PTC вложенные dispatch в v1 запрещены полностью.

Observers `tools/result` не участвуют в выдаче допуска. После нового tool attempt/
result прежние accounts требуют новой сверки; unknown effect не replay. DSH loop,
sandbox, sessions, approvals и orchestration не заменяются кодом iEWR.

## Records и совместимость

Схема bindings и CLI — в [ENTRY](../../app/bootstrap/ENTRY.md), meaning — у
[R](../../modules/recovery/CONTRACT.md). Нормализованные observations сохраняют
workspace/session/seq, exact direct text, message ID/rpcId либо полный raw event.
Human только `user/message` с `source.kind=user`; agent-instructions, tool output
и summary не становятся direct Human. Ref digest — SHA-256 canonical UTF-8 JSON
(sorted keys, compact separators); file ref digest вычисляется по исходным bytes.
Ответ UI, записанный только как tool result, не повышается до direct Human:
для него нужен отдельно qualified channel projection. В v1 непосредственно
поддержаны direct user messages, как в исследованном FAIL.

`through_seq` — последний relevant direct/tool event, а не wall-clock и не текущая
длина всех system/transport сообщений. Текущий ещё не dispatched call исключён;
прежние неизвестные tool attempts/results учитываются консервативно. Fork имеет
отдельную lineage, текущий session ID не подменяется родительским. Context из
carrier должен совпасть с наблюдённым; не переписывать его молча в P.

G interpretations, covered surfaces и factual completeness не извлекаются NLP.
Qualified owner queries должны сохранить действительные prohibitions/revocations;
поддельный owner record с верными hashes не становится trustworthy от проверки R.
Readonly carrier не обязателен для обычного разговора. При legacy Markdown без
machine bindings правильный результат — precise hold; automatic migration нет.

## Ограничения первой версии

- Cooperative local filesystem reads, не atomic snapshot и не hostile-writer protection.
- Нет контроля произвольного plugin I/O вне registry, внешних процессов и удалённых SoR.
- Нет native transaction journal, rollback, exactly-once или auto reconciliation.
- Семантический смысл Human ответа проверяется owner, а не checksum или regex.
- Offline synthetic ports не доказывают доверие к реальным provider/loader/channel.
- Live DSH trial, installation, publication в текущем поручении запрещены и не выполнены.

На другом host нужен его qualified consumer тех же R/owner contracts. Core не
импортирует DSH; отсутствие equivalent seam означает declared/unsupported предел,
а не автоматическую потерю semantic invariants.
