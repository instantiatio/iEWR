# Engineering Work Execution Guide

> Совместимый путь расширенного reference. Current application owner —
> [X](modules/execution/EXECUTION_BASIS.md); [dispatcher](AGENTS.md) выбирает только нужный use.
> Этот reference не второй runtime entry и не устанавливает общую последовательность.
> R восстанавливает accounts, G проверяет прямые grounds, E учитывает effects,
> L оценивает evidence/use, I отвечает за подачу; X не присваивает их state.


> Compatibility path: `WORKING_PROCESS_AND_LOOPS_GUIDE.md`
>
> Product: `Instantiatio EWR (iEWR)`
>
> `Working Process` и `Loop` сохранены в pathname и compatibility vocabulary,
> но не образуют обязательную runtime hierarchy.

## 1. Назначение

Guide управляет execution of bounded engineering Work после того, как current
question/use и достаточная execution basis восстановлены напрямую или через
conditional Formation.

Он определяет:

- recognition actual Work без смешения с Method, plan или record;
- direct execution-governance relations;
- optional WorkPlan/readiness use;
- Working Process как derived view;
- compatibility reading Loop/Task/Run;
- semantic-to-technical boundary и bounded effects;
- situation-responsive steering, concurrency, re-entry и recovery;
- conditional Verification, authority decision и reliance;
- adequate-result stop и smallest affected return.

Guide не задаёт domain Method, universal project lifecycle, обязательный Loop,
обязательный WorkPlan или универсальную Candidate → Verification → Admission
pipeline.

## 2. Core distinctions

Execution сохраняет direct FPF/DPF meanings:

```text
Method
≠ MethodDescription
≠ WorkPlan
≠ Work
≠ Work record
≠ Result
≠ evidence
≠ verification result
≠ authority decision
≠ reliance

capability
≠ assignment
≠ permission
≠ responsibility
≠ authority
≠ competence
≠ actual Work
```

EWR-specific carrier, filename, status, UI label или profile не создаёт ни одну
из этих relations. Когда material distinction имеет direct FPF/DPF owner,
ссылайся на него вместо EWR equivalent.

Execution relations относятся к exact engineering Work. Не переноси
assignment/authority внутри engineered subject на permission/authority выполнять
Work над этим subject. Static package, ZIP, source или specification не является
`U.System` автоматически. Work не является System; exact System boundary должен
быть independently established, если он нужен receiving use.

## 3. Execution entry

Перед первым или продолженным action:

1. При interruption, handoff, host/session/model change или ambiguity выполни
   deterministic re-entry по §9.
2. Восстанови current question, receiving use, exact subject и selected Method.
3. Реши, существует ли current `U.WorkPlan`. Если да, используй его только как
   intended-work episteme; если нет и planning не нужна, не создавай его.
4. Восстанови actual performer и independent direct governance relations.
5. Свяжи semantic requirements с current technical controls и effects.
6. Выполни один lawful next action по selected Method/FPF `A.15.7`.
7. Зафиксируй только фактически полученные Result/effects/evidence.
8. Reconcile effects, выполни triggered assurance/decision route и stop либо
   return к smallest owner.

Эта последовательность — minimal execution logic, а не обязательный Method.
Selected domain Method может организовать действия иначе, сохраняя invariants
этого Guide.

## 4. Actual Work и performer basis

### 4.1. Full Work admission

Ни action request, ни Task, Run, tool call, status `completed`, log или Result не
доказывают occurrence actual `U.Work`.

Перед claim Work используй строгий порядок:

```text
A.13 → independent full A.15.1 → conditional F.6
```

**Сначала `A.13`.** Для каждого exact actual performer восстанови:

- exact `U.System` performer;
- local agential system-role kind и его criterion;
- classification under that kind;
- obtaining assignment для exact action, scope, working situation и window;
- adequate core evidence;
- characteristic profile только когда exact Grade/autonomy/profile/assurance
  result действительно consume-ится.

**Затем independently `A.15.1`.** Admit exact dated Work из:

- grounded actual performance history;
- каждого A.13-qualified actual performer;
- как минимум одного obtaining `enactsMethod` к exact `U.Method`;
- actual temporal extent;
- как минимум одной obtaining locally declared Work-to-containing-System
  relation под exact boundary;
- иных actual bindings, resources, referents и relations, которые использует
  exact claim/receiving use.

Assignment, plan, description, output или record не заменяют этот basis.

**Только затем conditional `F.6`.** Когда receiving use должен утверждать, under
which exact assignment Work was performed, проверь
`performedUnderAssignment(W, RA)` через то же obtaining A.13 assignment:

- exact Work уже admitted independently;
- assignment species/occurrence/participants/rule восстановлены;
- direct case fact связывает W с RA;
- holder равен actual performer;
- assignment predicate obtains throughout attributed Work extent.

Missing or failed F.6 leaves admitted Work intact. Оно оставляет unresolved
только precise assignment-bound attribution и никогда не является
Work-membership premise.

### 4.2. Formation Work

Source resolution, Method selection, planning, reviewing и other Formation
reasoning не являются «pre-runtime magic». Они могут быть represented as Work
со своими Methods, performers, Results и evidence, но только по тому же полному
`A.13 → independent A.15.1` basis. Их carriers сами Work не создают.

### 4.3. Work identity и records

Actual execution occurrence и его record различаются:

```text
actual execution occurrence → U.Work
Run/log/report              → record or episteme about Work
```

Interruption, retry, resumption, performer/Method/binding change и Work-part
relations интерпретируются по actual occurrence facts и applicable FPF/direct
policy. Не split/merge Work по chat boundary, filename или record layout.

## 5. Direct Work

Direct Work — product phrase для bounded current Work, где separate WorkPlan не
добавляет decision или recoverability value. Оно не является отдельным FPF kind.

Для Direct Work нужны:

- applicable Method и полный Work basis §4;
- exact current action/result/receiving use;
- actual capable performer;
- separately obtaining assignment, permission и authority, где применимо;
- material allowed/prohibited effects и current technical boundary;
- observable outcome/effect check;
- durable-effect disposition;
- stop/recovery/return;
- Verification или decision только при их own trigger.

Direct Work не требует Loop, ceremonial Working Process, Method Engineering при
adequate Method или Human Admission без receiving-use trigger. Reversible не
значит authorized; low consequence не отменяет direct relations.

## 6. WorkPlan и readiness

`U.WorkPlan` используется только для current intended-work coordination по FPF
`A.15.2`. Complexity, consequence, duration или число actions не являются
membership criteria.

Plan может назвать intended Method, future performance designator, horizon,
window/entry condition, intended performer System/local role-kind condition,
resources, dependencies, commitments, targets и baselines. Он не создаёт:

```text
actual assignment | capability | permission | authority | readiness
| Work | resource use | Result | acceptance | reliance
```

`PlanItem` — content component exact WorkPlan, не future/actual Work, Method
part, assignment или Result record. `Task` carrier можно признать plan content
только по exact claims, а не имени.

Когда current вопрос — entry одного exact WorkPlan/PlanItem, получи и применяй
FPF `A.15.5 WorkEntryReadiness@Context`. EWR связывает result с exact attempted
entry, holds/refuses when it blocks, rechecks on its own currentness condition и
отдельно записывает actual launch/performance. EWR не создаёт parallel readiness
ontology. Direct Work без WorkPlan использует direct relations.

## 7. Working Process — derived execution view

`Working Process` сохранён как EWR product/UI compatibility term:

> **Working Process is an EWR-derived execution view/carrier over the separately
> governed claims needed to understand or conduct current Work.**

Он не является:

- новым FPF kind;
- Method или Method whole;
- WorkPlan;
- authority-level Process;
- container, который делает referenced relations obtaining.

При actual navigation/recovery/handoff use view может проектировать:

- current question/receiving use;
- selected Method/MethodDescription refs;
- current WorkPlan, только если он существует;
- Execution Governance Account;
- Relied Execution Basis Account;
- Factual Execution Account;
- technical/effect boundary;
- Result/evidence/decision/reliance routing;
- stop/return/reopen.

View может иметь revision/hash для publication/currentness. Это не делает его
source of truth. Underlying claims остаются у direct owners. Stale/conflicting
Working Process игнорируется или регенерируется affected-only; его deletion или
rename не меняет direct relations.

Создавай carrier только если он решает named coordination, navigation,
recoverability, handoff или decision problem. Не создавай его из-за complexity,
template или package convention.

## 8. Loop, Task, Run и Candidate compatibility

### 8.1. Loop

Loop не является mandatory standalone runtime kind. Legacy material resolve
case-by-case:

- reusable semantic way of doing → candidate/admitted `U.Method`, только когда
  criteria FPF `A.3.1` obtain;
- `LOOP-NNN` text/carrier → possible `U.MethodDescription` или local profile,
  только когда соответствующие criteria obtain;
- iteration, retry, feedback cycle → actual Method/Work structure без
  необходимости Loop object.

Loop filename, ID, approval или repetition не доказывает Method identity,
MethodDescription membership, WorkPlan или Work.

### 8.2. Task

Task остаётся compatibility request/intended-item carrier. По exact content/use
он может содержать instruction, request, plan cue или reference to Work, но:

- не является автоматически `PlanItem`;
- не создаёт assignment/permission/authority;
- не доказывает actual Work;
- не заставляет создавать Run.

### 8.3. Run

Run остаётся record/episteme об execution context, configuration, timing,
effects, evidence и recovery. Record не perform Work. Run completion не
устанавливает correctness, adequacy, Result kind, verification, decision или
reliance.

### 8.4. Candidate

`Candidate` — optional product/view label для direct Result, intended reliance
которого unresolved. Это не universal EWR entity/status и не обязательный вход
в Verification/Admission. Legacy Candidate/Admission records сохраняют exact
historical meaning/use без mass conversion.

## 9. Three execution accounts и deterministic re-entry

### 9.1. Accounts

Для safe continuation независимо resolve:

**Execution Governance Account** references:

- current assignment relations;
- permission/prohibition;
- authority;
- commitments/pending decisions;
- relevant responsibility relations.

**Relied Execution Basis Account** references:

- exact source editions;
- MethodDescription editions/currentness;
- WorkPlan/carrier revisions, если они есть;
- project baselines;
- actual platform/tool/model configurations;
- authoritative external systems of record.

**Factual Execution Account** references:

- actual Work and performers where established;
- Results and durable effects;
- interruptions, retries/resumptions;
- unresolved partial effects.

Это derived projections, не одна database/state machine. Source edition,
permission, plan revision, actual System configuration и effect остаются
разными claims.

### 9.2. Re-entry procedure

Re-entry нужен после interruption, handoff, session/model/host change, context
loss, ambiguity, suspected drift или partial execution:

1. Hold new consequential effects до resolution affected bindings.
2. Recover exact current question/use и три accounts из direct carriers,
   hashes, current observations и external SoR.
3. Compare required vs current source/MethodDescription/plan/configuration and
   governance bindings. Не доверяй transcript, mtime или filename.
4. Identify actual partial Work and reconcile all material durable effects.
5. Reject stale assignment, permission, source, plan, profile, provider or view
   bindings only for affected action/use.
6. Return either sufficiently resolved basis for lawful continuation or exact
   unresolved/blocker result.
7. Choose next action by §14; do not blind-replay.

Procedure детерминированна по inputs/guards, но не обещает восстановить любой
external fact. Honest unresolved result — valid outcome.

`STATE_INDEX` может ускорять navigation только по explicit project decision.
Он не authority, не factual truth и не package-wide registry. Invalid/stale/
conflicting index игнорируется; accounts восстанавливаются из direct owners.

## 10. Execution relations and authority

Для exact action/current window восстанови независимо:

| Relation | Current question | Не доказывает |
|---|---|---|
| Capability | Может ли exact System выполнить action при условиях? | assignment, permission, authority, performance |
| Assignment | Получает ли holder local system-role relation? | capability, permission, authority, Work |
| Permission/prohibition | Разрешён ли effect/action? | capability, responsibility, acceptance |
| Responsibility | Какая direct responsibility relation obtains? | assignment, permission, authority automatically |
| Authority | Кто вправе сделать exact commitment/decision/effect? | competence или technical access |
| Competence | Достаточен ли basis для exact review/judgment? | authority или admission |
| Actual Work | Произошло ли dated performance по §4? | Result quality или reliance |

Не выводи relation из participant title, confidence, profession, model/provider,
tool access, successful output или другой relation. Один participant может
занимать несколько positions только по separate basis для каждой.

Review competence даёт evidence, но не admits Result. Admission authority не
доказывает review competence. Missing/conflicting relation blocks only affected
action/reliance. Within exact unchanged delegated envelope continuation не
требует micro-approval; новый material commitment возвращается к owner.

## 11. Semantic-to-technical boundary

Если consequential Work relies on technical boundary, свяжи каждый semantic
requirement с exact current control/configuration и classify:

| Status | Meaning | Required evidence/action |
|---|---|---|
| `declared` | Requirement is stated; realization not yet qualified | Do not claim technical enforcement |
| `enforced` | Current control actually prevents/limits affected action | Fresh observed evidence for exact configuration |
| `compensated` | Named compensation holds boundary sufficiently for use | Compensation, owner, evidence, residual risk and failure route |
| `unsupported` | Current configuration cannot honestly hold boundary | Narrow, return for authority/control, or stop affected action |

Examples: allowed write/delete/execute loci, sandbox, tool/API permissions,
budgets, retries, external-provider limits, configuration pinning and recovery.
Policy prose, template, model name или prior-host observation не является
`enforced` evidence.

До action выбери `enforce | compensate | return/escalate | honest_stop`. Record
required/actual mapping, exact evidence/currentness и reopen trigger. Technical
capability/permission остаются distinct от semantic/project authority.

## 12. Bounded actions, effects и execution envelope

Consequential execution envelope должен быть exact и proportional:

```text
Current question / receiving use
Selected Method and applicable description
Exact inputs and configuration
Allowed actions/loci/effects
Prohibited actions/loci/effects
Permission/authority basis
Technical status per material boundary
Finite budgets/retries/time bounds
Observable evidence/check
Durable-effect dispositions
Recovery/escalation/termination
Conditional verification/final-decision trigger
```

За пределами explicit authorization effect budget равен нулю. Tool capability,
automation или broad task wording не расширяют envelope. Reversibility снижает
risk, но не создаёт permission.

Каждый attempt/retry учитывается по actual effect и budget. Не делай retry,
если prior partial effect не reconciled или binding стал stale.

## 13. Bounded Execution Profile и CAP

### 13.1. Purpose and boundary

Когда selected Method требует нескольких actions/phases под одним explicit
envelope, можно использовать optional **Bounded Execution Profile**. Legacy
`CAP` (`Consolidated Authority Package`) — compatibility alias, а не authority
package в target semantics.

Profile ссылается на independently obtained relations и grants no authority,
permission, capability, Method status, WorkPlan, Work, verification или
reliance. Его existence/approval не заменяет action-time currentness.

### 13.2. Exact profile content

Profile содержит только materially used fields:

- profile identity/revision/currentness and exact receiving use;
- selected Method and relied MethodDescription;
- exact inputs, allowed/prohibited loci/actions/effects;
- phases и entry/exit/termination predicates;
- budgets, retry/resource limits and depletion behavior;
- independently established performer/governance refs;
- semantic-to-technical mappings and actual capability evidence;
- required observations/evidence;
- durable-effect reconciliation;
- recovery/override/escalation;
- conditional Verification and final authority-decision triggers;
- explicit supervised/autonomy classification.

Carrier не должен дублировать direct sources as a parallel truth. Drift любого
relied binding invalidates only dependent phases/actions.

### 13.3. Activation and deviation

Execution under profile начинается только когда selected Method требует его и
all relations/current controls for the first action established. Profile-local
operational labels допустимы как view, но не являются Core lifecycle.

При deviation from exact inputs/loci/phases/predicates/budgets/governance/
technical boundary:

1. stop affected actions;
2. mark exact profile use `terminated_on_deviation` as an operational fact;
3. preserve deviation/current configuration evidence;
4. reconcile actual durable effects;
5. return to ordinary stepwise recovery/authority route.

Deviation terminates/returns without silent resume. Тот же exact profile не
resume. Successor profile требует нового current basis, scope and authorization
и не создаётся/активируется автоматически.

### 13.4. Conditional E.16 autonomy

Suggestion-only is E.16 non-use. Supervised execution, agent participation или
наличие profile не доказывают autonomous System, agency grade или authority.

FPF `E.16` применяется только для actual claimed unsupervised
decision/actuation. Тогда profile/use должен ссылаться на exact current
enactment-bound:

- budget and actual consumption;
- guards and stop/depletion predicates;
- ledger/effect account;
- override and escalation;
- separation of duties;
- authority/permission and technical enforcement;
- recovery and termination.

Каждый budgeted Work и каждый override SpeechAct
`PauseAutonomy | ResumeAutonomy | NarrowAutonomy | Escalate` остаётся actual
Work: exact performer сначала получает полный `A.13` core, затем occurrence
независимо допускается по полному `A.15.1`. Поскольку E.16 override use требует
precise attribution к exact obtaining override-authority assignment, `F.6`
применяется после Work admission через то же assignment и не становится
Work-membership premise. `DepletionNotice` также является SpeechAct Work и
требует собственного `A.13 → independent full A.15.1` basis; его later `F.6`
нужен только если receiving claim потребляет precise assignment-bound
attribution. Ledger — evidence о Work, а не его admission.

Если E.16 basis отсутствует, lower route to supervised/suggestion-only либо stop;
не изображай unsupervised action как authorized autonomy.

### 13.5. «Форсаж» boundary

Core не определяет route, owner, MethodDescription, profile, content или tests
для legacy product cue «Форсаж». Его target disposition остаётся `DEFER`. Этот
Guide не активирует и не предлагает его автоматически.

## 14. Situation-responsive steering и concurrency

Во время ongoing Work выбирай next action согласно applicable Method и FPF
`A.15.7`. Возможные результаты steering:

```text
continue with allowed action
choose another allowed action
request bounded missing result
return to responsible prior claim/result
stop
escalate for authority
```

Не создавай successor action только потому, что previous action completed.

При concurrent Work:

1. получи semantic overlap/order decision из owning Method/DPF, если он нужен;
2. validate assignment, permission, authority and configuration at action time;
3. reject stale/invalidated binding only for affected action;
4. keep interleaved durable effects attributable and reconcilable;
5. stop/serialize/narrow только когда current guard требует.

EWR не создаёт universal scheduler. Parallel agent execution не создаёт
concurrency safety без exact Method and evidence.

## 15. Results и durable-effect reconciliation

Result сохраняет kind/meaning owning FPF/domain pattern. EWR не создаёт
universal `EngineeringResult`. Record, evidence, decision, acceptance и reliance
не являются Result автоматически и не выводятся из completion.

Перед consequential closure, handoff или recovery completion каждый material
durable effect получает recoverable disposition:

```text
represented            — included in current Result/baseline
authoritative_external — governed by named external system of record
disposable             — explicitly no downstream reliance
unresolved/deferred    — blocks only dependent closure/use
```

Не скрывай effect, если его downstream relevance unresolved. Persistence не
означает correctness/adequacy. Git duplication не требуется, если actual
authoritative SoR находится вне Git. Disposable/read-only/unchanged Work не
создаёт baseline ceremony.

## 16. Conditional Verification, decision и reliance

### 16.1. Verification

Materialize Verification только когда её требует:

- selected Method;
- receiving use;
- applicable DPF/LPF;
- evidence/assurance need;
- law/regulation/policy;
- actual decision basis.

Keep separate:

```text
Verification Method
Verification Work
observations/evidence
verification result
assurance result
later authority decision
actual reliance
```

Simple observable check не обязан становиться отдельным Verification Work.
Scenario/protocol/marker text не является evidence execution. Tool success
доказывает только exact observed fact в current configuration.

### 16.2. Authority decision

Explicit Human/other authorized decision нужен только когда receiving use
реально его требует: release, consequential commitment, action outside delegated
authority, policy/regulatory acceptance или other exact trigger.

Bounded Result within current delegated authority не требует ceremonial
re-Admission solely because EWR produced it. Decision record фиксирует exact
Result/configuration/use, authority, conditions and effect — и не создаёт
semantic truth или review competence.

### 16.3. Reliance

Reliance — actual receiving-use-relative relation, не intrinsic permanent
artifact status. Когда material, сохрани exact:

- result/claim/configuration;
- receiving use;
- evidence/assurance;
- source/currentness boundary;
- authority decision, если он требовался;
- reopen condition.

Один Result может поддерживать use A и не поддерживать use B. Legacy `admitted`
status остаётся evidence old decision for named use; он не делает вечный
`Relied-on Result`.

## 17. Source/configuration change и affected-only reopen

Changed relied-on source обрабатывай по FPF `A.10.1`: compare at claim size,
confirm direct reliance, bound discovery, revalidate affected uses and stop
locally. Аналогичную discipline применяй через direct owners к changes:

- DPF/LPF contribution;
- Method/MethodDescription;
- WorkPlan;
- assignment/permission/authority;
- platform/tool/model configuration;
- EWR implementation itself.

Change не меняет meaning/boundary already executing action silently. Apply it
через explicit current-use/re-entry decision at safe boundary.

Reopen only affected contribution resolution, Method selection, plan content,
readiness, execution boundary, Verification/assurance, decision или reliance.
Unaffected Work/Results/evidence остаются usable, пока держится их basis.

## 18. Partial-execution recovery

Когда interruption, degradation или reconfiguration может изменить
continuation:

1. identify affected actual Work/current intended Work;
2. recover performer/support configuration на нужной grain;
3. distinguish finished, partial, not-started and unknown actual effects;
4. reconcile every material durable effect по §15;
5. validate current governance/basis/technical bindings;
6. choose smallest lawful continuation, repair, return or stop;
7. preserve evidence and reopen trigger.

Не repeat Work because chat/session state was lost. Не называй recovery complete,
пока unresolved material effect скрывает dependent closure.

## 19. Optional carriers

Carrier count/format остаётся proportional. Possible locations below are
conventions, not mandatory Core structure.

### 19.1. Working Process view

```text
# Working Process — derived view

Current Question / Receiving Use
Source Claims and Currentness
Selected Method / MethodDescription
WorkPlan Reference, if one exists
Execution Governance Account refs
Relied Execution Basis Account refs
Factual Execution Account refs
Current Technical/Effect Boundary
Result / Evidence / Decision / Reliance Triggers
Stop / Return / Reopen
View Revision / Derived From / Stale If
```

### 19.2. Work record / legacy Run

```text
# Work Record

Exact Work claim and A.13/A.15.1 basis refs
Actual start/end/interruption
Actual performer/configuration
Method enacted
Actions and actual effects
Results and evidence refs
Durable-effect dispositions
Unresolved facts / recovery
Record provenance and limitation
```

Record content не заменяет world-side facts, а file creation не доказывает
Work.

### 19.3. Decision or reliance record

Создавай только при distinct use. Сохрани exact object/configuration,
receiving use, evidence/assurance, authority and scope, conditions, outcome,
date/currentness and reopen route. Empty checklist не является decision;
completed checklist не доказывает correctness или reliance.

## 20. External capabilities и views

External skill/provider при actual/requested use classify:

```text
capability_only | process_bearing_mappable | process_incompatible
```

Map useful capability, Method или contribution into current Work. Не импортируй
foreign lifecycle, status, authority, source truth или plan automatically.
Preserve provider identity, privacy, limits, drift and fallback. Incompatible
process возвращает bounded fallback или stop.

Model assignment, independent review, Engineering Views, decision UI,
checklists и progress summaries — host/application or conditional Verification
aids. Они не Core authority, не mandatory lifecycle и не parallel truth.
Capability/independence claims требуют current evidence; view должен указывать
derivation/currentness и игнорироваться при staleness.

Operational lessons могут стать evidence для separate governed improvement
Work. Они не мутируют active Method, LPF, DPF или Core автоматически.

## 21. Compatibility и provenance

iEWR обеспечивает reading compatibility, а не продолжение legacy universal
semantics:

| Legacy carrier/term | Target reading |
|---|---|
| Working Process | optional derived execution view |
| Loop / `LOOP-NNN` | Method/MethodDescription/local-profile candidate only after qualification |
| Task / `TASK-NNN` | request/intended-item carrier; type by exact content |
| Run / `RUN-NNN` | record/episteme about Work/effects |
| Candidate | optional unresolved-reliance view label |
| Verification field | exact old check/evidence/verification claim by context |
| Admission record | exact authority decision for old named use |
| Relied-on Result | recover actual result/configuration/use relation |
| CAP | legacy alias for Bounded Execution Profile; grants nothing |
| STATE_INDEX | optional derived navigation projection |

Не mass-convert historical carriers, не re-admit их и не infer kind/status из
filename. Preserve exact IDs/hashes/links as provenance when material.

Bundled DPF editions и catalogue/reference materials остаются external sources/
aids. Directory placement не создаёт Core precedence. Release notes, baseline
tag/ZIP и compatibility scenarios остаются historical truth; target package
integrity, behavior, Human Admission, release и publication — separate facts.

## 22. Stop, return и no automatic successor

Stop, когда current receiving use имеет domain-adequate result under its
Method/evidence/decision basis и нет другой current obligation. EWR не определяет
domain adequacy.

При failure/change return к smallest responsible:

```text
source claim
resolved contribution
Method decision
WorkPlan position
readiness result
execution-control relation
technical boundary
Work Result
evidence / decision / reliance claim
```

Independent unaffected results остаются usable. Completion не создаёт automatic
successor action, new Loop/Task/Run, Process Review, proof apparatus, LPF/DPF/
Core mutation, release или publication.

Главная формула:

```text
resolve current execution basis
→ perform one lawful Method-directed next action
→ record actual Work/Result/effects without collapse
→ qualify only for the use that needs it
→ reconcile, stop or reopen the smallest affected owner
```
