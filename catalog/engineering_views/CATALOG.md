# Каталог инженерных представлений — EV references

Content cues для I, не отдельные runtime modules. Применение и ownership —
[README](README.md). Required evidence определяется exact receiving use,
Method/policy, а не category strength. Внешний вид не доказывает semantics.
Исторические EV IDs сохраняются; ниже нет requirement пройти все записи.

## `EV-01` — Контекст системы

| Поле | Значение |
|---|---|
| `view_id` | `EV-01` |
| `Russian/user name` | Контекст системы |
| `exact technical aliases` | System Context Diagram; C4 System Context; Context View |
| `engineering object` | system boundary, actors, external systems and critical interactions |
| `purpose/question answered` | Что находится внутри и снаружи системы и где проходят критические взаимодействия? |
| `typical audience/decision` | заказчик, архитектор, integration owner; решение о scope и границах ответственности |
| `context triggers` | product/system work; material boundary, supplier или integration decision |
| `counter-signals` | локальная работа без системной границы; sufficient current use-bound context |
| `selection limit` | relevance cue only; required evidence from exact use/Method/policy |
| `minimum content` | system boundary, actors, external systems, interfaces/interactions, assumptions |
| `authoritative source types` | direct context/source basis, ConOps, requirements, architecture |
| `allowed notations/formats` | C4/context diagram, Mermaid/PlantUML, annotated table/text |
| `freshness/change rule` | reverify при изменении scope, actor, external system или critical interface |
| `baseline-difference behavior` | на affected decision use показать добавленные/удалённые границы и взаимодействия |
| `accessibility/text equivalent` | concise summary; при text-only use — список inside/outside, actors, external systems и interfaces |
| `verification` | сверка границ и интерфейсов с authoritative sources и integration owner |
| `non-coverage` | не доказывает внутреннюю архитектуру, поведение или system properties |
| `extension point` | namespaced domain boundary/assurance annotations |
| `reopen trigger` | новый actor/interface, boundary dispute или integration gap |

## `EV-02` — Компоненты и ответственности

| Поле | Значение |
|---|---|
| `view_id` | `EV-02` |
| `Russian/user name` | Компоненты и ответственности |
| `exact technical aliases` | Component Diagram; C4 Container/Component; Logical Architecture View |
| `engineering object` | components, responsibilities, interfaces and integration ownership |
| `purpose/question answered` | Какие компоненты за что отвечают и как соединены? |
| `typical audience/decision` | архитектор, разработчики, integration owner; decomposition/interface decision |
| `context triggers` | multi-component system, shared services/interfaces, material ownership split |
| `counter-signals` | single bounded component без material interaction; sufficient current use-bound architecture |
| `selection limit` | relevance cue only; required evidence from exact use/Method/policy |
| `minimum content` | components, responsibilities, provided/required interfaces, ownership, integration responsibility |
| `authoritative source types` | current use-bound architecture, interface contracts, code/configuration baseline |
| `allowed notations/formats` | C4/UML component, Mermaid/PlantUML, dependency table |
| `freshness/change rule` | reverify при component/interface/ownership/configuration change |
| `baseline-difference behavior` | показать изменения decomposition, interfaces и integration responsibility |
| `accessibility/text equivalent` | concise summary; при exact/text-only use — component → responsibility → interfaces → owner table |
| `verification` | reverse trace к architecture/code baseline и проверка interface ownership |
| `non-coverage` | component pass не доказывает system-level integration/properties |
| `extension point` | namespaced runtime, safety или domain responsibility metadata |
| `reopen trigger` | новый component, interface conflict, ownership ambiguity или integration failure |

## `EV-03` — Последовательность взаимодействия

| Поле | Значение |
|---|---|
| `view_id` | `EV-03` |
| `Russian/user name` | Последовательность взаимодействия |
| `exact technical aliases` | Sequence Diagram; Message Sequence Chart; Interaction View |
| `engineering object` | material scenario, participants, messages/events and temporal order |
| `purpose/question answered` | Кто с кем и в каком порядке взаимодействует в сценарии, включая ошибки? |
| `typical audience/decision` | разработчики, API/integration owner, verifier; interaction/failure-path decision |
| `context triggers` | cross-component/external workflow, race, retry, timeout или failure path |
| `counter-signals` | нет temporal/interaction question; state view уже полностью отвечает use |
| `selection limit` | relevance cue only; required evidence from exact use/Method/policy |
| `minimum content` | participants, ordered messages/events, alternatives/failures, pre/postconditions |
| `authoritative source types` | scenarios, contracts, protocol/event specifications, verified traces |
| `allowed notations/formats` | UML sequence/MSC, Mermaid/PlantUML, ordered event table |
| `freshness/change rule` | reverify при protocol, order, retry/error или participant change |
| `baseline-difference behavior` | выделить новые/изменённые messages, ordering и failure paths |
| `accessibility/text equivalent` | concise summary; при exact/text-only use — numbered interactions with conditions/outcomes |
| `verification` | сверка с contracts/scenarios и material runtime evidence, если доступно |
| `non-coverage` | не заменяет полный state model, API schema или timing proof |
| `extension point` | namespaced timing, security или protocol annotations |
| `reopen trigger` | race/failure incident, contract drift или непонятный порядок |

## `EV-04` — Состояния и переходы

| Поле | Значение |
|---|---|
| `view_id` | `EV-04` |
| `Russian/user name` | Состояния и переходы |
| `exact technical aliases` | State Machine Diagram; Statechart; Lifecycle Model |
| `engineering object` | lifecycle states, transitions, guards and invariants |
| `purpose/question answered` | Какие состояния и переходы управляют поведением объекта? |
| `typical audience/decision` | domain owner, разработчик, verifier; lifecycle/error/recovery decision |
| `context triggers` | material stateful lifecycle, guarded transitions, terminal/error states |
| `counter-signals` | stateless behavior; states не влияют на relying use |
| `selection limit` | relevance cue only; required evidence from exact use/Method/policy |
| `minimum content` | states, events, guards, transitions, terminal/error states, invariants |
| `authoritative source types` | requirements, domain model, state schema/code, protocol contract |
| `allowed notations/formats` | UML/statechart, transition table, Mermaid/PlantUML |
| `freshness/change rule` | reverify при state/event/guard/invariant change |
| `baseline-difference behavior` | показать added/removed states/transitions и changed guards |
| `accessibility/text equivalent` | concise summary; при exact/text-only use — transition table state + event + guard → next state/effect |
| `verification` | completeness/reachability checks proportional to risk plus source trace |
| `non-coverage` | не доказывает interaction order, persistence correctness или system safety |
| `extension point` | namespaced timing, safety или recovery properties |
| `reopen trigger` | invalid transition, orphan state, lifecycle change или recovery incident |

## `EV-05` — ER-диаграмма и модель данных

| Поле | Значение |
|---|---|
| `view_id` | `EV-05` |
| `Russian/user name` | ER-диаграмма и модель данных |
| `exact technical aliases` | ER/Data Model; Entity–Relationship Diagram; ERD; Logical/Physical Data Model |
| `engineering object` | material persisted entities, relationships and constraints |
| `purpose/question answered` | Какие данные сохраняются, как связаны и какие правила обеспечивают их целостность? |
| `typical audience/decision` | domain/data owner, разработчик, DBA, verifier; persistence/schema/migration decision |
| `context triggers` | material database или logical persisted data model |
| `counter-signals` | данные не сохраняются; use уже закрыт current use-bound equivalent model |
| `selection limit` | relevance cue only; required evidence from exact use/Method/policy |
| `minimum content` | composite order: logical entities/meaning/relationships/cardinalities/business invariants → necessary physical tables/columns/types, primary/foreign/candidate keys, constraints/indexes/migrations → separate source/change/limitation text; analytics layer separate, mappings/gaps explicit |
| `authoritative source types` | authoritative logical model and/or schema/migrations with exact source configuration and declared layer |
| `allowed notations/formats` | crow's-foot/IDEF1X/UML data model, Mermaid/PlantUML, relational table plus text |
| `freshness/change rule` | schema/model/migration change makes affected view stale until regenerated/reverified |
| `baseline-difference behavior` | affected decision use shows current model plus material entity/relation/key/constraint/migration difference |
| `accessibility/text equivalent` | concise summary always; when format unavailable or exact decision needs it, tables of entities, attributes/keys, relations/cardinalities, constraints/invariants and layer mappings |
| `verification` | reverse trace to model/schema/migrations/configuration; check order, keys, cardinalities, constraints, invariants, layer distinction and summary/fallback parity |
| `non-coverage` | slice-local ER не доказывает whole-product/full-scope data, state or invariant readiness; diagram не доказывает migration/runtime correctness |
| `extension point` | namespaced privacy, retention, lineage, regulatory или physical tuning metadata |
| `reopen trigger` | schema/migration drift, integrity incident, layer conflation или consequential persistence beyond represented scope |

## `EV-06` — Словарь данных и инварианты

| Поле | Значение |
|---|---|
| `view_id` | `EV-06` |
| `Russian/user name` | Словарь данных и инварианты |
| `exact technical aliases` | Data Dictionary; Information Model; Invariant Catalogue |
| `engineering object` | fields/values, domains, ownership and cross-entity rules |
| `purpose/question answered` | Что означают важные данные и какие правила действуют поверх структуры? |
| `typical audience/decision` | domain/data owner, разработчик, analyst, verifier; semantic/quality/privacy decision |
| `context triggers` | EV-05 labels insufficient; shared semantics, sensitivity, derived values или cross-entity invariants |
| `counter-signals` | trivial self-evident fields and no material receiving use |
| `selection limit` | relevance cue only; required evidence from exact use/Method/policy |
| `minimum content` | definitions, types/domains, nullability, ownership, sensitivity, derived values, invariants |
| `authoritative source types` | domain model, schema, contracts, current use-bound glossary/policy |
| `allowed notations/formats` | Markdown/CSV/table, model export with semantic text |
| `freshness/change rule` | reverify при field/domain/ownership/policy/invariant change |
| `baseline-difference behavior` | показать changed definitions/domains/sensitivity/invariants |
| `accessibility/text equivalent` | concise semantic summary plus readable table when exact values/relations are needed |
| `verification` | source trace, duplicate/undefined term and invariant consistency checks |
| `non-coverage` | не заменяет ER relations, physical schema или analytics lineage proof |
| `extension point` | namespaced regulatory vocabulary, units, lineage or quality rules |
| `reopen trigger` | semantic dispute, data-quality/privacy incident или new shared field |

## `EV-07` — API-контракт и взаимодействие

| Поле | Значение |
|---|---|
| `view_id` | `EV-07` |
| `Russian/user name` | API-контракт и взаимодействие |
| `exact technical aliases` | API Contract View; Interface Control Document; AsyncAPI/OpenAPI View |
| `engineering object` | external/shared operations, messages, schemas, errors and compatibility |
| `purpose/question answered` | Что пересекает interface boundary и как стороны сохраняют совместимость? |
| `typical audience/decision` | provider/consumer, integration/security owner, verifier; contract/version decision |
| `context triggers` | relied-on external/shared API, event contract или material interface change |
| `counter-signals` | private local call без separate relying use; current use-bound contract sufficient |
| `selection limit` | relevance cue only; required evidence from exact use/Method/policy |
| `minimum content` | operations/events, request/response/message schemas, errors, auth boundary, versioning/compatibility; interaction view where useful |
| `authoritative source types` | current use-bound OpenAPI/AsyncAPI/protocol/interface specification and version configuration |
| `allowed notations/formats` | OpenAPI/AsyncAPI/IDL plus readable table/text; sequence view when triggered |
| `freshness/change rule` | reverify при operation/schema/error/auth/version change |
| `baseline-difference behavior` | affected decision use shows breaking/non-breaking contract difference and consumers |
| `accessibility/text equivalent` | concise summary; exact/text-only use gets operation/message table with inputs, outputs, errors, auth and version rules |
| `verification` | schema validation, compatibility analysis, provider/consumer trace and contract tests |
| `non-coverage` | не доказывает implementation, end-to-end behavior или operational availability |
| `extension point` | namespaced protocol, QoS, security or regulatory constraints |
| `reopen trigger` | consumer failure, compatibility incident, new version или auth boundary change |

## `EV-08` — Развёртывание и конфигурация

| Поле | Значение |
|---|---|
| `view_id` | `EV-08` |
| `Russian/user name` | Развёртывание и конфигурация |
| `exact technical aliases` | Deployment Diagram; Infrastructure View; Runtime Topology |
| `engineering object` | environments/nodes, deployed components, networks, dependencies and configuration boundaries |
| `purpose/question answered` | Где работает система и какие зависимости/настройки влияют на её поведение? |
| `typical audience/decision` | operations/SRE, architect, security/release owner; deployment/recovery decision |
| `context triggers` | material environment, release, network, configuration, recovery or operations decision |
| `counter-signals` | environment irrelevant to current use; adequate current deployment baseline |
| `selection limit` | relevance cue only; required evidence from exact use/Method/policy |
| `minimum content` | nodes/environments, components, networks/dependencies, configuration and secrets boundaries, recovery |
| `authoritative source types` | deployment/configuration/IaC/release baseline and environment inventory |
| `allowed notations/formats` | UML deployment/C4 deployment, Mermaid/PlantUML, topology/config table |
| `freshness/change rule` | reverify при environment/topology/dependency/configuration/recovery change |
| `baseline-difference behavior` | показать topology/configuration/recovery difference without secret values |
| `accessibility/text equivalent` | concise summary; exact/text-only use gets environment-node-component-dependency/config boundary table |
| `verification` | compare with current use-bound configuration/IaC and observable deployment evidence |
| `non-coverage` | не раскрывает secrets и не доказывает availability, security или recovery outcome |
| `extension point` | namespaced capacity, region, safety, compliance or threat annotations |
| `reopen trigger` | environment drift, deployment/recovery incident или new operational decision |

## `EV-09` — Трассировка требований и проверок

| Поле | Значение |
|---|---|
| `view_id` | `EV-09` |
| `Russian/user name` | Трассировка требований и проверок |
| `exact technical aliases` | Requirements Traceability Matrix; Verification Cross-reference; Evidence Map |
| `engineering object` | source, requirement, design/change, test/evidence and relied-on result relations |
| `purpose/question answered` | Какие связи и evidence поддерживают утверждение и где остаются пробелы? |
| `typical audience/decision` | accountable authority, reviewer, verifier; Admission/change-impact decision |
| `context triggers` | consequential product change; trace is Admission basis; material impact review |
| `counter-signals` | reversible low-risk action without relied-on trace use; equivalent current trace exists |
| `selection limit` | relevance cue only; required evidence from exact use/Method/policy |
| `minimum content` | forward/reverse relations, exact configuration/status, verification evidence and visible gaps |
| `authoritative source types` | current use-bound carriers, exact requirements/design/configuration and test/run evidence |
| `allowed notations/formats` | trace table/matrix, graph projection plus textual gap list |
| `freshness/change rule` | reverify when any relied-on node/configuration/status/relationship changes |
| `baseline-difference behavior` | affected decision use shows added/removed/changed relations, evidence and gaps |
| `accessibility/text equivalent` | concise summary plus readable relation table and explicit unsupported claims/gaps when needed |
| `verification` | forward/reverse coverage, exact identity/status and dangling/conflicting relation checks |
| `non-coverage` | trace existence не доказывает correctness, adequacy или system-level property |
| `extension point` | namespaced assurance case, hazard, regulation or supplier evidence links |
| `reopen trigger` | missing evidence, changed requirement/configuration, dangling trace или Admission dispute |

## Ограниченный состав

EV-01…EV-09 сохраняют предметные questions, source/currentness и non-coverage.
DFD, dashboards и business-process views не добавляются ради полноты; иной useful
view допустим по direct question без новой common entry. Catalog promotion и
изменение persistent project profile требуют собственного scoped решения,
если этот effect/use его требует; обычное представление такого решения не создаёт.
