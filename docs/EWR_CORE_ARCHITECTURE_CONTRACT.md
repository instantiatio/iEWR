# Engineering Work Runtime (EWR) — Core Architecture Contract

**Version:** 1.0 RC  
**Date:** 2026-09-03  
**Status:** Release Candidate architecture contract after scenario and source/conformance audit  
**Predecessor:** Instantiatio DPF (iDPF) 4.0.1 — Engineering Work Runtime · Beta  
**Architectural classification:** functional specialization of the Engineering Platform concept (`SYSE.12`)  
**Methodological foundation:** FPF Core + applicable FPF-grounded DPFs + optional LPFs

---

## 0. Purpose

This contract defines the **minimal architecture-specific obligations of Engineering Work Runtime (EWR)**.

It answers:

> What must an Engineering Platform do, beyond generic platform enablement, to support FPF-driven formation, steering, execution, recovery and inspectable reliance of bounded engineering Work?

## 0.1 Normative provenance

This document is normative **for the EWR product architecture**.

Its clauses have different source roles:

- some directly operationalize normative FPF/DPF patterns;
- some are EWR-specific specialization rules constrained by FPF distinctions;
- some retain proven runtime mechanisms from iDPF 4.0.1;
- self-hosting is a product acceptance requirement.

An EWR-specific `SHALL` does not imply that FPF itself prescribes that exact runtime mechanism. The companion `EWR_CORE_CONTRACT_0.2_SOURCE_CONFORMANCE_AUDIT.md` records the provenance classification.

The contract does **not** define:
- a universal engineering lifecycle;
- a universal project Method;
- a domain methodology;
- a mandatory traversal of FPF/DPF patterns;
- a fixed set of human or AI roles;
- a mandatory WorkPlan for every Work occurrence;
- a mandatory Human Admission;
- a new ontology parallel to FPF;
- a mandatory machine-readable DPF schema;
- a mandatory DPF Registry/Resolver.

---

# 1. Identity and classification

## 1.1 Product identity

**Engineering Work Runtime (EWR)**

Recommended functional description:

> **Engineering Work Runtime is an Engineering Platform specialized for FPF-driven, situation-responsive formation, execution control, steering and recovery of bounded engineering Work.**

## 1.2 Engineering Platform relation

EWR is designed and assessed as an **Engineering Platform** under `SYSE.12`, with an additional EWR-specific functional contract.

This wording does not assert an FPF class hierarchy in which `Engineering Platform` or `EWR` must be admitted as a new `U.Kind`.

A deployed EWR is an actual `U.System` only when the FPF System criteria obtain.

---

# 2. Architectural thesis

EWR separates two logical planes.

```text
FORMATION PLANE

current question / receiving use
        ↓
bounded source set
        ↓
FPF + applicable DPF + optional LPF + project sources
        ↓
smart-agent / human reasoning
        ↓
resolved pattern contributions
        ↓
Method decision only when current
        ↓
U.WorkPlan only when intended Work must be planned


EXECUTION PLANE

current executable basis
        ↓
performer / capability / assignment
permission / authority / commitments
actual platform configuration
technical enforcement / side-effect boundary
        ↓
A.15.5 readiness when applicable
        ↓
A.15.7 situation-responsive steering
        ↓
actual U.Work
        ↓
Result + durable effects
        ↓
conditional evidence / verification / authority decision
        ↓
actual downstream reliance
        ↓
re-entry / recovery / minimal reopen
```

The two planes are **functional views**, not separate ontological domains and not necessarily separate software services.

Actual reasoning performed in the Formation Plane is itself `U.Work` when the FPF Work criteria obtain. Its results—such as a source-resolution result, Method decision or WorkPlan—remain separately governed results.

---

# 3. Governing FPF distinctions

EWR SHALL preserve, not redefine:

```text
Method
≠ MethodDescription
≠ WorkPlan
≠ Work
≠ Work record
≠ Result
≠ evidence
≠ verification result
≠ decision
≠ permission
≠ authority
≠ reliance
```

It SHALL also preserve:

```text
capability
≠ assignment
≠ permission
≠ responsibility
≠ authority
≠ actual Work
```

EWR SHALL reference direct FPF/DPF owners for these meanings rather than creating EWR equivalents.

---

# 4. Source and contribution resolution

## EWR-01 — Current question and receiving use

EWR SHALL make the current question and its receiving use recoverable at the grain needed for the next action.

EWR SHALL prefer:
1. reuse of an adequate current result;
2. bounded current Work;
3. intended-work planning only when planning is needed.

EWR SHALL return an honest blocker when the current question, receiving use or required direct relation cannot be recovered.

## EWR-02 — Bounded source set

EWR SHALL operate from a bounded source set that may include:
- FPF Core;
- applicable DPFs;
- applicable LPFs;
- project/domain sources;
- standards, policies and other authorities;
- current platform/tool capability information.

Exact edition/currentness SHALL be preserved where it can change a relied-on use.

No heavy Registry/Resolver is required as a core invariant.

## EWR-03 — Resolved pattern contributions

DPF/LPF resolution SHALL return **task-relevant pattern contributions**, not assume every contribution is a Method.

A contribution may supply:
- a distinction;
- a bounded question/problem frame;
- a Method or MethodDescription;
- a required or first useful Result;
- a constraint;
- an evidence/use boundary;
- a specialist-return requirement;
- a dependency;
- a stop/return/reopen condition;
- a source/currentness condition.

When reproducibility, audit, handoff or consequential reliance makes resolution material, EWR SHOULD preserve a lightweight resolution episteme with:
- current question / receiving use;
- exact source editions;
- selected PatternIDs / loci;
- applicability basis;
- expected contributions;
- material limits;
- reopen condition.

## EWR-04 — No framework-type precedence

The labels `FPF`, `DPF`, `LPF`, `policy`, `standard` or `local practice` do not by themselves establish precedence when claims conflict.

Conflicts SHALL be routed to the direct claim owner:
- authority/policy relation;
- evidence/currentness;
- Method choice/fit;
- domain result;
- source-use/reliance;
- other applicable direct governor.

The conflict remains visible until the governing relation is resolved.

---

# 5. Method boundary

## EWR-05 — Method use

EWR SHALL NOT assert or rely on an occurrence as `U.Work` unless the applicable FPF `A.15.1` admission basis is satisfied, including at least one enacted `U.Method`.

EWR does not define or upgrade Method identity. It consumes the Method identity/status supplied by the applicable FPF/DPF/Method Engineering or another direct owner.

Methods may be located from:
- FPF/DPF;
- LPF;
- another qualified professional source;
- an admitted local Method;
- Method Engineering when the Method itself is the current decision subject.

## EWR-06 — Method Engineering is conditional

Method Engineering SHALL be invoked only when a Method-related question is current, including:
- Method identity;
- repertoire;
- situational requirements;
- qualification;
- composition/conflict;
- adaptation;
- description/support;
- fit/transfer;
- practical worth;
- variant/change.

EWR SHALL NOT impose:

```text
every task → Method Engineering → execution
```

A domain project using an already adequate Method remains in the owning domain.

## EWR-07 — No mandatory Loop

EWR SHALL NOT require `Loop` as a standalone runtime kind.

Legacy iDPF Loop material SHALL be interpreted through FPF semantics:
- repeatable way of doing → candidate/admitted Method where criteria obtain;
- `LOOP-NNN` carrier → MethodDescription/local Method profile where criteria obtain.

Iteration, retry and cycle structure remain allowed when the selected Method requires them.

---

# 6. Intended Work and WorkPlan

## EWR-08 — WorkPlan only when intended-work planning is current

EWR SHALL use `U.WorkPlan` when the current claim is a coordinated intended-work episteme within the applicability of FPF `A.15.2`.

Typical EWR cases include intended Work that must be:
- coordinated;
- delegated;
- scheduled/reserved;
- dependency-managed;
- prepared for later execution;
- made recoverable across handoff/interruption;
- or otherwise relied upon before performance.

These are EWR usage examples, not additional FPF membership criteria.

EWR SHALL NOT create a WorkPlan merely because Work is complex, consequential or non-trivial.

Two lawful entries therefore exist:

```text
bounded current Work
→ applicable Method + direct execution/governance relations
→ actual Work

planned/delegated/recoverable Work
→ U.WorkPlan
→ direct execution/governance relations
→ actual Work
```

## EWR-09 — WorkPlan does not establish actuality

A WorkPlan SHALL NOT establish:
- actual assignment;
- actual capability;
- permission;
- authority;
- readiness;
- actual Work;
- actual resource consumption;
- result;
- acceptance/reliance.

These remain separately governed claims.

---

# 7. Working Process

## EWR-10 — Working Process is a derived execution view

`Working Process` is retained as an EWR product/UI term for compatibility.

It is **not**:
- a new FPF kind;
- a Method;
- a Method whole;
- a WorkPlan;
- a container whose existence makes referenced relations obtain.

Definition:

> **Working Process is an EWR-derived execution view/carrier over the separately governed claims needed to understand or conduct the current Work.**

It may project:
- a current WorkPlan, when one exists;
- selected Method/MethodDescription references;
- current execution-governance relations;
- current execution basis;
- factual execution information;
- evidence/reliance routing;
- stop/return/reopen information.

The view creates none of these relations.

A Working Process may have its own carrier revision/hash for publication/currentness purposes, while the underlying semantic claims keep their direct owners.

Long-term removal or renaming of `Working Process` SHALL NOT require semantic changes to EWR Core.

---

# 8. Execution-control relations

## EWR-11 — Exact subject discipline

Execution-control relations SHALL concern the exact Work governed by EWR.

EWR SHALL NOT confuse:
- assignment/authority **inside the engineered subject** (for example, an organization being redesigned),
with
- assignment/permission/authority **to perform the engineering Work that changes or analyses that subject**.

The same discipline applies to capability, responsibility, resource access and decision rights.

## EWR-12 — Execution-governance account

For re-entry and control, EWR MAY maintain a derived **Execution Governance Account** that references, without collapsing:
- current assignment relations;
- permission/prohibition relations;
- authority relations;
- commitments;
- pending decisions;
- relevant responsibility relations.

The account is a projection, not one homogeneous world-side “authority state”.

## EWR-13 — Relied execution-basis account

EWR MAY maintain a derived **Relied Execution Basis Account** that references, without collapsing:
- source editions;
- MethodDescription editions;
- WorkPlan/carrier revisions;
- actual platform/tool/model configurations;
- project baselines;
- external systems of record;
- other execution-basis claims.

A source edition, plan revision and actual System configuration remain different kinds of claim.

## EWR-14 — Factual execution account

EWR MAY maintain a derived **Factual Execution Account** containing references to:
- actual Work;
- actual performers where established;
- durable effects;
- produced Results;
- interruptions;
- retries/resumptions;
- unresolved partial effects.

A dashboard/index/chat summary is not authoritative merely by presentation.

---

# 9. Work-entry and technical realization

## EWR-15 — FPF readiness, not EWR readiness

When work-entry readiness is current for a WorkPlan/PlanItem, EWR SHALL obtain, evaluate and enforce the applicable FPF `A.15.5 WorkEntryReadiness@Context` result.

EWR owns only the runtime use of that result:
- connect it to the exact attempted entry;
- refuse/hold when it blocks;
- recheck when its conditions/currentness require;
- record actual launch/performance values separately.

EWR SHALL NOT define a parallel readiness ontology.

For bounded current Work with no WorkPlan, EWR SHALL use the required direct relations rather than invent an A.15.5 readiness result.

## EWR-16 — Semantic boundary to technical realization

When consequential Work relies on a technical execution boundary, EWR SHALL map the semantic requirement to the exact current runtime capability/control.

For each material boundary, the runtime SHALL be able to distinguish at least:

```text
enforced
compensated
unsupported / unresolved
```

Examples include:
- allowed loci;
- write/delete/execute restrictions;
- retry/budget limits;
- sandbox boundaries;
- tool/API permissions;
- configuration pinning;
- external-provider limits.

A semantic prohibition that the runtime cannot enforce or compensate SHALL NOT be represented as technically enforced.

## EWR-17 — Bounded autonomous execution profile

A CAP-like bounded execution profile MAY be used when several autonomous actions need one explicit envelope.

It may reference:
- allowed/prohibited effects;
- exact configuration;
- budgets;
- phase/termination predicates;
- recovery/escalation;
- authority/permission basis.

The profile creates none of the referenced authority or permission relations and SHALL terminate/return when governing conditions fail.

---

# 10. Steering and concurrency

## EWR-18 — Situation-responsive steering

During ongoing Work, EWR SHALL support next-action selection consistent with FPF `A.15.7`.

A steering result may:
- continue;
- choose another allowed action;
- request a bounded missing result;
- return to a responsible prior claim/result;
- stop;
- escalate for authority.

EWR SHALL NOT manufacture a successor action merely because the previous action completed.

## EWR-19 — Concurrency guard

When Work is concurrent, EWR SHALL:
- respect the semantic overlap/order decision supplied by the applicable Method/DPF (`SYSE.20`, `ME.6`, etc.);
- validate current execution bindings at action time;
- prevent stale or invalidated assignment/permission/configuration bindings from silently acting;
- keep interleaved durable effects reconcilable.

EWR does not need a universal scheduler.

---

# 11. Actual Work and records

## EWR-20 — Work is not a Run record

Actual execution is `U.Work` only when the FPF Work criteria obtain.

A `Run` MAY remain as a product/runtime record carrier for:
- exact execution context;
- tool/model/configuration;
- start/end/interruption;
- durable effects;
- evidence references;
- recovery information.

Therefore:

```text
actual execution occurrence → U.Work
RUN-NNN / Run log          → record/episteme about Work
```

Run completion does not establish correctness, result adequacy or reliance.

## EWR-21 — Formation Work remains visible when material

Source resolution, Method selection, planning, reviewing and other Formation Plane reasoning are not “pre-runtime magic”.

When they meet the criteria for actual Work, EWR SHALL permit them to be represented as Work with their own Methods, performers, results, evidence and reliance boundaries.

---

# 12. Results, effects and closure

## EWR-22 — Result keeps its direct kind

A Result produced by Work keeps the type and meaning supplied by its owning FPF/domain pattern.

EWR SHALL NOT create a universal `EngineeringResult` kind.

`Candidate` may remain only as an optional product/view label for a result whose intended reliance remains unresolved.

## EWR-23 — Durable-effect reconciliation

Before consequential closure, handoff or recovery completion, EWR SHALL NOT hide a material durable effect whose downstream relevance is unresolved.

A material effect should receive a recoverable disposition such as:
- represented in the current result/baseline;
- governed by an authoritative external system of record;
- disposable / no downstream reliance;
- unresolved/deferred and therefore blocking only dependent closure/use.

EWR SHALL NOT require Git duplication when another actual system of record is authoritative.

Disposable Work/effects SHALL NOT create baseline ceremony merely because they occurred.

---

# 13. Verification, decisions and reliance

## EWR-24 — Verification is conditional and typed

Verification SHALL be materialized only when required by:
- the selected Method;
- the receiving use;
- an applicable DPF/LPF;
- assurance/evidence need;
- law/regulation/policy;
- an actual decision basis.

Verification Work, when performed, is actual Work enacting an applicable verification Method.

Keep separate:
- Verification Method;
- Verification Work;
- observations/evidence;
- verification result;
- assurance result;
- later authority decision;
- actual reliance.

## EWR-25 — Explicit authority decision is conditional

An explicit human or other authorized decision is required only when the receiving use actually needs such a decision.

Examples include:
- release;
- consequential commitment;
- use outside delegated authority;
- acceptance required by policy;
- safety/regulatory authority.

A bounded result within current delegated authority does not require ceremonial re-Admission solely because EWR produced it.

## EWR-26 — Actual reliance is receiving-use-relative

Reliance is a relation/use, not an intrinsic permanent artifact status.

When material, EWR SHOULD preserve:
- exact result/claim/configuration;
- receiving use;
- supporting evidence/assurance;
- source/currentness boundary;
- authority decision where required;
- reopen condition.

---

# 14. Source/configuration change

## EWR-27 — Affected-use revalidation

When a relied-on source claim changes, EWR SHALL use FPF `A.10.1` to recover and revalidate affected uses.

As an EWR specialization rule, analogous changes to other governing execution bases—such as a DPF/LPF contribution, MethodDescription, WorkPlan basis, platform configuration or other execution basis—SHALL be routed through their direct FPF/DPF owners and the same affected-only discipline.

Reopen only affected:
- contribution resolution;
- Method selection;
- WorkPlan content;
- readiness result;
- execution boundary;
- verification/assurance;
- decision/reliance;

where feasible.

Unaffected Work and Results remain usable while their grounds hold.

## EWR-28 — No silent mutation of governing basis

A change to:
- governing source edition;
- active MethodDescription;
- WorkPlan revision;
- permission/authority basis;
- runtime/tool configuration;
- EWR implementation itself;

SHALL NOT silently alter the meaning or boundary of an already executing action.

The change takes effect only through an explicit current-use/re-entry decision at a safe boundary.

---

# 15. Re-entry and recovery

## EWR-29 — Deterministic recovery procedure

After interruption, handoff, session/model/host change or ambiguity, EWR SHALL follow a deterministic recovery procedure that returns either:
- sufficiently resolved governing accounts for safe continuation; or
- an explicit unresolved/blocker result.

The procedure SHALL NOT promise that all external facts can always be reconstructed.

At minimum it resolves independently:

```text
Execution Governance Account
Relied Execution Basis Account
Factual Execution Account
```

## EWR-30 — Recovery

When partial execution, degradation or reconfiguration may change continuation, EWR SHALL:
- identify the affected Work/current intended Work;
- recover the performing/support configuration as far as required;
- reconcile durable effects;
- determine the smallest lawful continuation, repair, return or stop.

EWR SHALL NOT repeat Work merely because chat/session state was lost.

---

# 16. Proportionality and Direct Work

## EWR-31 — Cheapest lawful move

EWR SHALL prefer the least process machinery that can lawfully obtain the current useful result or blocker.

Possible outcomes include:

```text
reuse existing result
bounded Direct Work
WorkPlan-based execution
request bounded specialist result
honest stop/blocker
```

## EWR-32 — Direct Work

Direct Work is permitted when the action is bounded enough that a separate WorkPlan adds no decision/recoverability value.

Direct Work still requires:
- an applicable Method;
- actual capable performer;
- required direct permission/authority relations;
- material technical/effect boundary;
- observable enough outcome/effects;
- stop/recovery where needed.

Direct Work does not require:
- a Loop;
- a ceremonial Working Process;
- Method Engineering unless Method itself is uncertain;
- Human Admission unless downstream use needs a decision.

---

# 17. Stop, return and reopen

## EWR-33 — Adequate-result stop

EWR SHALL NOT continue solely because a process sequence remains once:
- the current receiving use has an adequate result under its governing Method/evidence/decision basis; and
- no other current obligation requires Work.

EWR itself does not define domain adequacy.

## EWR-34 — Minimal return

When something fails or changes, return to the smallest responsible:
- source claim;
- resolved contribution;
- Method decision;
- WorkPlan position;
- readiness result;
- execution-control relation;
- Work result;
- evidence/decision/reliance claim.

Independent unaffected results remain usable where their basis still holds.

---

# 18. LPF and local practice

## EWR-35 — LPF is optional input

EWR MAY use one or more applicable LPFs for persistent local practice, including:
- local Methods/variants;
- tool conventions;
- local authority/policy constraints;
- stable local checks;
- support/recovery practices.

EWR SHALL work without an LPF where none exists.

EWR SHALL NOT identify itself as an LPF merely because it executes local Work.

## EWR-36 — EWR does not mutate LPF automatically

Repeated Work and telemetry may provide evidence for separate LPF-development Work.

No runtime success/failure automatically changes:
- LPF;
- DPF;
- Method;
- EWR Core.

---

# 19. Platform/tool boundary

## EWR-37 — Host independence

EWR semantics SHALL NOT depend on one:
- model provider;
- agent host;
- IDE;
- forge;
- repository;
- CI product.

Host adapters and product-specific recommendations remain outside Core.

## EWR-38 — Current capability over product name

EWR SHALL reason from the observed/qualified capabilities and limits of the exact current platform configuration.

Provider/model/tool identity alone does not establish:
- authority;
- capability beyond evidence;
- independence;
- quality;
- applicable Method.

---

# 20. Views and carriers

## EWR-39 — Derived views do not create truth

Working Process views, dashboards, state indexes, progress summaries and Engineering Views MAY be provided.

A view:
- derives from governed source claims;
- identifies relevant currentness/configuration where material;
- does not create authority, Work, result, evidence or state.

Stale/conflicting views SHALL NOT silently govern execution.

---

# 21. Improvement and self-development

## EWR-40 — Platform/Process Engineering feedback

EWR MAY expose operational evidence about:
- ceremony burden;
- failed recovery;
- repeated bookkeeping;
- source-resolution drift;
- Method mis-selection;
- handoff loss;
- enforcement failure;
- transferred human burden.

Using that evidence to change EWR, its platform configuration, an LPF, a Method or DPF is separate governed Work.

## Product acceptance requirement — self-hosting

For this EWR product, self-development SHALL be demonstrated through the same runtime contract using appropriate sources, for example:

```text
FPF Core
+ Systems Engineering DPF
+ Human–AI Software Engineering DPF
+ Method Engineering when current
+ EWR Development LPF
+ project sources
```

Self-hosting is a product acceptance requirement, not a defining property of every conceivable Engineering Work Runtime.

---

# 22. Core invariants

A conforming EWR SHALL satisfy:

### INV-01 — No parallel domain methodology
No hidden universal engineering lifecycle or domain Method in EWR Core.

### INV-02 — FPF distinction preservation
Direct FPF/DPF objects and relations do not collapse into EWR umbrella objects.

### INV-03 — No mandatory Loop
Cycles come from Methods/Work structure, not mandatory runtime hierarchy.

### INV-04 — Conditional WorkPlan
WorkPlan exists when intended-work planning is current, not merely because Work is complex.

### INV-05 — Working Process is only a view
Working Process creates no semantic relations.

### INV-06 — Domain relation vs execution relation separation
Relations inside the engineered subject do not become relations governing the engineering Work by wording alone.

### INV-07 — Formation Work is still Work
Consequential formation reasoning may be governed, recorded and relied upon like other Work.

### INV-08 — Authority independence
Capability, assignment, permission, responsibility and authority remain separate.

### INV-09 — Technical enforcement honesty
A semantic boundary is not called enforced unless current platform controls actually enforce it or a stated compensation is used.

### INV-10 — Durable-effect visibility
Consequential closure does not hide unresolved material durable effects.

### INV-11 — Conditional assurance
Verification and explicit authority decisions appear only when current use requires them.

### INV-12 — Proportional machinery
No mandatory artifact/check/gate without a receiving decision, protected condition, execution need, reliance need or recoverability function.

### INV-13 — Source extensibility
A new FPF-grounded DPF can contribute normally without EWR Core modification.

### INV-14 — LPF optionality
EWR works with or without persistent LPF.

### INV-15 — Deterministic re-entry procedure
Re-entry deterministically resolves or explicitly reports unresolved governance, basis and factual execution.

### INV-16 — Affected-only reopen
Changed premises reopen only dependent claims/Work where feasible.

### INV-17 — No silent basis mutation
Active execution is not silently redefined by changed sources/plans/configuration/runtime.

### INV-18 — Host independence
Core semantics do not depend on one host/provider/toolchain.

---

# 23. Minimal conforming execution logic

```text
0. RE-ENTER IF NEEDED
   resolve-or-block:
   execution governance
   relied execution basis
   factual execution

1. IDENTIFY CURRENT USE
   question / receiving use / exact subject

2. CHOOSE CHEAPEST LAWFUL MOVE
   reuse?
   bounded current Work?
   need intended-work planning?
   need specialist result?
   blocker?

3. RESOLVE SOURCES / CONTRIBUTIONS AS NEEDED
   FPF / DPF / LPF / project sources
   preserve exact editions when material

4. RESOLVE METHOD AS NEEDED
   use direct adequate Method
   open Method Engineering only if Method decision is current

5. FORM WORKPLAN ONLY IF NEEDED
   intended Work / dependencies / conditions

6. BIND EXECUTION
   direct performer/governance relations
   exact execution basis
   technical/effect boundary
   A.15.5 readiness if applicable

7. STEER / PERFORM
   A.15.7 next action
   actual U.Work
   maintain factual execution account

8. RECONCILE RESULT / EFFECTS
   exact domain Result
   durable-effect dispositions

9. QUALIFY FOR USE ONLY AS REQUIRED
   verification Work/evidence
   assurance
   authority decision
   actual reliance

10. STOP / RETURN / REOPEN
    stop on domain-adequate result
    reopen smallest affected basis
```

This is a runtime architecture model, not a mandatory Method or lifecycle.

---

# 24. Semantic minimum

A conforming EWR needs only enough durable information to recover the positions that are material for current Work.

Possible carriers include:

| Position | Possible carrier |
|---|---|
| current question / receiving use | issue, context note, decision record |
| resolved contributions | optional resolution episteme |
| intended Work | `U.WorkPlan` when needed |
| Working Process view | derived execution projection |
| Method/description refs | source refs |
| execution governance | derived account referencing direct relations |
| execution basis | derived account / manifest / external records |
| actual Work/effects | Work records + external evidence |
| Result | domain artifact/result |
| verification/evidence | direct result/evidence carrier |
| authority decision | direct decision carrier |
| reliance | use/reliance record when material |
| re-entry | derived accounts over authoritative sources |

Carrier count and format remain proportional.

---

# 25. Explicit non-goals

EWR Core SHALL NOT become:
- DPF;
- LPF;
- replacement FPF;
- Method Engineering framework;
- project-management methodology;
- software lifecycle;
- agent-role taxonomy;
- engineering-result ontology;
- heavy DPF registry;
- autonomous authority system;
- mandatory human-review bureaucracy;
- UI design framework;
- model-selection framework.

---

# 26. Accepted migration decisions

### Decision A — Loop retyping
`Loop` is not a mandatory runtime kind; Method semantics own reusable ways of doing.

### Decision B — Working Process demotion
`Working Process` is a derived execution view over separately governed claims.

### Decision C — Conditional reliance route
No universal Candidate → Verification → Human Admission → Relied-on lifecycle.

---

# 27. Acceptance scenarios

The contract must pass without Core modification:

1. Systems Engineering architecture work.
2. Organization Change work involving human/AI arrangements.
3. Problem Structuring / Decision Support.
4. Bounded Direct Work.
5. EWR self-development through Human–AI Software Engineering DPF.

A failure occurs if a normal domain question requires:
- a new EWR semantic kind;
- mandatory lifecycle stage absent from its Method;
- hard-coded DPF-specific route;
- fake authority/verification requirement;
- hidden durable effect;
- or patch to EWR Core merely to express ordinary DPF contributions.

---

# 28. One-sentence architecture

> **EWR is an Engineering Platform that preserves the executable boundary between FPF-grounded reasoning and real engineering effects: it resolves or receives the current basis for Work, enforces current execution relations, supports situation-responsive performance and recovery, and keeps evidence, authority and reliance inspectable without inventing a parallel methodology.**
