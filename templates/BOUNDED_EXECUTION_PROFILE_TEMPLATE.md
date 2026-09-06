# Bounded Execution Profile — шаблон ограниченного профиля исполнения

> `BoundedExecutionProfile` — optional carrier под выбранным `Method`, когда несколько
> действий требуют одного явного envelope. Профиль описывает границы исполнения, но
> не создаёт `Method`, `WorkPlan`, `Work`, capability, assignment, permission,
> responsibility или authority и не допускает Result к reliance. Использовать
> отдельный carrier следует только при названном receiving use; для одной простой
> обратимой операции достаточно прямых relations и observable check.

## 1. Идентификация и применимость

- Profile ID: `BEP-...`
- Edition / exact configuration ID: `...`
- Carrier status for the named use: `draft | current | superseded`
- Date / currentness window: `...`
- Selected `Method` reference: `...`
- Relied-on `MethodDescription` edition/hash: `...`
- Exact current or intended Work reference, if it exists: `not established | ...`
- WorkPlan / PlanItem reference, only when current: `not applicable | ...`
- Receiving use: `...`
- Why one bounded profile is useful for this use: `...`
- Execution mode:
  `supervised_suggestion_only | supervised_action_at_human_confirmation | unsupervised_decision_or_actuation`

Do not infer actual Work from this profile or from execution records. Admit any
claimed `U.Work` independently under the full current `A.15.1` basis, after the
exact performer has the full `A.13` core and at least one enacted Method is
established. Apply `F.6 performedUnderAssignment` only when precise
assignment-bound attribution is current for the receiving use; it is not a
Work-membership premise.

## 2. Governing sources and exact configuration

| Input / configuration | Exact carrier, edition and hash | Role for this use | Currentness predicate | Drift return |
|---|---|---|---|---|
| selected Method / MethodDescription | `...` | `...` | `...` | `do not start / terminate affected execution` |
| semantic boundary source | `...` | `...` | `...` | `...` |
| intended-work carrier, if current | `...` | `...` | `...` | `...` |
| runtime/tool configuration | `...` | `...` | `...` | `...` |

A closed baseline may replace individual rows only when every relied-on input
resolves unambiguously from it. Access to a source and placement in this profile
do not make that source authoritative.

## 3. Independent execution relations

Record only relations that are current for the receiving use. A blank or missing
row remains unresolved; the profile supplies none of these relations.

| Relation / claim | Exact subject and scope | Direct source / decision / evidence | Effective window | Action-time check | Failure route |
|---|---|---|---|---|---|
| performer and applicable local kind | `...` | `...` | `...` | `...` | `...` |
| capability | `...` | `...` | `...` | `...` | `...` |
| assignment | `...` | `...` | `...` | `...` | `...` |
| permission / prohibition | `...` | `...` | `...` | `...` | `...` |
| decision/action authority | `...` | `...` | `...` | `...` | `...` |
| responsibility / commitment, if current | `...` | `...` | `...` | `...` | `...` |
| competence for an exact review/use, if current | `...` | `...` | `...` | `...` | `...` |

Capability, technical access, assignment, permission, responsibility and
authority remain separate from one another and from competence. Tool success,
a profile status, a title or an agent label establishes none of them. Review
competence supplies neither decision authority nor result Admission.

## 4. Allowed actions, prohibited effects and recovery

### Allowed actions and exact effect loci

| Action / effect | Exact target | Maximum instances or magnitude | Required current relations | Observable completion | Recovery / reconciliation |
|---|---|---:|---|---|---|
| `...` | `...` | `...` | `...` | `...` | `...` |

A wildcard is valid only with bounded recoverable instances and an enforceable
count rule. Unused budget does not authorize additional scope.

### Zero-by-default effect classes

| Effect class | `allowed` or `0/not allowed` | Exact boundary when allowed | Separate authority decision if crossed |
|---|---|---|---|
| destructive delete / move / overwrite | `0` | — | `...` |
| Git index / history / remote | `0` | — | `...` |
| network / external system | `0` | — | `...` |
| production / deployment | `0` | — | `...` |
| security / privacy boundary | `0` | — | `...` |
| packaging / release / publication | `0` | — | `...` |

Silence means not allowed. Name stop, rollback/repair and authoritative external
system-of-record routes before execution.

## 5. Method-bound steps and transition predicates

The rows below describe bounded enactment support for the selected Method. They
do not create a universal phase sequence, a `Loop`, or a new Method.

| Step ID / Method step ref | Allowed action | Entry predicates | Budget consumed | Exit observation | Allowed local repair | Failed-predicate route |
|---|---|---|---|---|---|---|
| `...` | `...` | `...` | `...` | `...` | `...` | `return / stop / escalate` |

Only a full predicate pass permits an action. Completion of one row does not
manufacture a successor action; steering selects the next lawful action under
the current Method and situation.

### Concurrent or interleaved Work — only when current

- Applicable Method/DPF overlap or order result: `not applicable | ...`
- Concurrent Work/action refs and shared loci: `...`
- Action-time stale assignment/permission/configuration rejection: `...`
- Interleaved-effect reconciliation rule: `...`

Do not infer safe overlap from separate plans or profiles. Use the direct
Method/DPF result and current bindings; this template creates no scheduler.

## 6. Supervision boundary

Fill exactly one branch matching `Execution mode`.

### Supervised suggestion-only

- Observable Human confirmation point before every world-affecting action: `...`
- Suggested content that the performer may prepare: `...`
- Actions the profile itself may not initiate: `...`

This branch does not claim unsupervised decision or actuation. FPF `E.16` is not
applicable solely because an agent prepared a suggestion, used tools under
continuous Human confirmation, or followed bounded steps.

### Supervised action at Human confirmation

- Exact actions requiring point-of-execution Human confirmation: `...`
- How confirmation is bound to action, target and current configuration: `...`
- Expiry / stale-confirmation rejection: `...`

### Unsupervised decision or actuation

- Exact autonomy claim: `...`
- Exact actions that may proceed without continuous Human direction: `...`
- Required `E.16` profile: complete §7 before any such action.

## 7. Conditional FPF `E.16` autonomy profile

- Applicability:
  `not_applicable_supervised_or_suggestion_only | applicable_unsupervised_decision_or_actuation`
- Non-applicable basis and observable Human confirmation point: `...`

When applicability is `not_applicable_supervised_or_suggestion_only`, leave the
remaining fields in this section `not applicable`. When it is applicable, every
field required by the exact claim must resolve from its direct source; this
template does not create missing Systems, assignments, authority or Work.

### `AutonomyBudgetDecl`

- ID and version: `...`
- Binding state: `prospective | enactment-bound`
- Autonomy claim reference: `...`
- Budget-consumer local system-role kind reference: `...`
- Working situation and Work-admission condition: `...`
- Applicable policy reference: `...`
- `ClaimScope` and qualification window: `...`
- Budget: action tokens, decision tokens, risk bands, resource caps and time
  window as applicable: `...`
- `AdmissibilityConditionsId` / Aut-Guard policy: `...`
- Override protocol reference: `...`
- Override-authority local kind and policy: `...`
- Exact `A.2.7` separation-of-duties relation: `...`
- Edition pins: `...`

A prospective declaration describes a claim and future envelope only. It cannot
admit actual Work. Before autonomous enactment, use an enactment-bound edition
that resolves all actuals below.

### Enactment-bound actuals and Green-Gate

- Budget-consumer performer System: `...`
- Exact obtaining `A.2.1` assignment: `...`
- Exact budgeted Work: `...`
- Override-authority System and exact assignment: `...`
- Current independent authority-relation occurrence: `...`
- Matching Method steps and `requiresAutonomyBudget` reference: `...`
- Scope/window and enactable-assignment check: `...`
- Remaining-budget check: `...`
- Ordinary guards and verdicts: `...`
- Actual-pair `A.2.7` SoD predicate check: `...`

Any failed or unresolved Green-Gate predicate blocks only the affected autonomy-
gated enactment. Labels, different assignment IDs, budget prose or schema-field
presence do not establish an actual binding, SoD or authority.

### Ledger, override and depletion

- Work-anchored `AutonomyLedgerEntry` locus: `...`
- Required entry fields: Work, performer System, exact assignment, budget edition,
  deltas, guard verdicts and, for override Work, authority/SoD result refs.
- Override SpeechActs:
  `PauseAutonomy | ResumeAutonomy | NarrowAutonomy | Escalate`: `...`
- Override SpeechAct Work basis: exact actual performer with full `A.13` core,
  including the obtaining override-authority assignment; independent full
  `A.15.1` admission with enacted Method, extent and containment; then `F.6`
  through that same assignment because this E.16 use consumes precise
  assignment-bound attribution: `...`
- Depletion notice, block and parking/escalation behavior: `...`
- `DepletionNotice` SpeechAct Work basis: its exact actual performer with full
  `A.13` core and obtaining assignment; independent full `A.15.1` admission;
  conditional later `F.6` only if its receiving claim consumes precise
  assignment-bound attribution: `...`
- Conditions for admitted `ResumeAutonomy`: actual-assignment SoD, independent
  authority, remaining/renewed budget and ordinary guards: `...`
- Scout / probe / commit partition, only if actually used: `not applicable | ...`

Every budgeted Work, override SpeechAct and `DepletionNotice` is independently
recognized as Work only through `A.13 → independent full A.15.1`; a ledger row
does not perform that admission. Every admitted budgeted or override Work gets
its own ledger entry. Depletion blocks subsequent autonomy-gated steps. A
successful probe never authorizes a commit, wider budget or wider scope without
the declared checkpoint decision. Do not create an autonomy service, registry,
state machine or telemetry service merely to fill this profile.

## 8. Semantic-to-technical boundary

| Semantic requirement | Required capability/control | Exact current implementation/configuration | State | Evidence | Affected-action route |
|---|---|---|---|---|---|
| `...` | `...` | `...` | `declared \| enforced \| compensated \| unsupported` | `...` | `enforce \| compensate \| Human Gate \| honest_stop` |

`declared` is not evidence of `enforced`. Use
`RUNTIME_CAPABILITY_PROFILE_TEMPLATE.yaml` only when a repeated/material
receiving use warrants a separate derived view. A technical capability or
permission never supplies project authority.

### External capabilities and process-bearing contributions — only when current

| External item and exact configuration | Classification | Accepted direct capability / Method / contribution | Rejected foreign lifecycle/status/authority semantics | Drift or conflict route |
|---|---|---|---|---|
| `...` | `capability_only \| process_bearing_mappable \| process_incompatible` | `...` | `...` | `...` |

Availability does not authorize use. Map accepted parts into current Work under
their direct owners; a foreign `approved`, `complete` or `success` label is at
most evidence for its exact source use and never imports a parallel lifecycle.

## 9. Durable-effect reconciliation

| Actual effect | Observation / evidence | Disposition | Authoritative carrier or SoR | Unresolved dependent use | Recovery state |
|---|---|---|---|---|---|
| `...` | `...` | `represented \| external_system_of_record \| disposable_no_reliance \| unresolved_deferred` | `...` | `...` | `...` |

Unknown or unresolved material effects block only dependent closure/use. Do not
duplicate an effect in Git when another actual system of record is authoritative.

## 10. Verification, decision and reliance — only when current

| Current question | Required by selected Method / receiving use / policy? | Direct owner and carrier | Evidence / outcome | Return condition |
|---|---|---|---|---|
| Verification | `yes \| no` | `...` | `...` | `...` |
| authority decision | `yes \| no` | `...` | `...` | `...` |
| actual reliance | `yes \| no \| unresolved` | `...` | exact Result/use/configuration: `...` | `...` |

Verification, an authority decision and actual reliance are independent and
conditional. Passing a check does not admit a Result; an authority decision does
not prove correctness; completion of this profile authorizes no successor Work.
Keep every produced Result under its direct FPF/domain kind. Use `Candidate` only
as an optional view label when intended reliance is unresolved.

## 11. Deviation termination and recovery

If a governing condition, boundary, action-time binding, budget or mandatory
predicate fails, set this exact profile execution to `terminated_on_deviation`
and immediately stop profile-controlled actions.

Leading report:

> Bounded Execution Profile прекращён: обнаружено отклонение от согласованных условий.

Record:

- exact deviation and affected step: `...`;
- last completed observation: `...`;
- actual effects and their reconciliation state: `...`;
- preserved Result/evidence state: `...`;
- recovery performed or unresolved: `...`;
- smallest lawful ordinary return/stop/escalation route: `...`.

The same profile execution does not pause-and-resume or retry after deviation.
After cause and new exact bounds are understood, the applicable authority may
select a successor edition or ordinary stepwise execution. Neither is created or
activated automatically. Termination of the profile does not by itself terminate
unaffected Work or the wider initiative.

## 12. Legacy CAP compatibility mapping

`CAP` / `Consolidated Authority Package` remains a compatibility label for exact
iDPF records. Existing CAPs retain their original configuration, decisions,
statuses and receiving-use meaning; they are not auto-converted.

| Legacy CAP field / behavior | iEWR interpretation |
|---|---|
| CAP identity, version and hash | predecessor carrier identity/provenance; optionally maps to a new profile ID only by explicit project decision |
| phase/action/budget envelope | Method-bound bounded execution fields in §§4–5 |
| authority-package wording | references independent relations in §3; grants none |
| universal Candidate / Admission fields | preserved only for the exact legacy contract; not required by this template |
| `terminated_on_deviation` and no-resume rule | preserved profile-execution behavior in §11 |
| legacy phrase `CAP прекращён: обнаружено отклонение от согласованных условий` | valid rendering for an exact legacy CAP record only |

The profile is not a universal lifecycle, governance bundle or authority source.
`Loop`, `Task`, `Run`, CAP and status names in predecessor records remain readable
without becoming target semantic kinds.
