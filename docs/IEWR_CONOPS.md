# iEWR Concept of Operations

| Document information | Value |
|---|---|
| Basis | iEWR 7.0.6 Eternal Alpha |
| Document edition | 05.11.2026 |
| Status | Research concept; checking scope is stated in STATUS.md |
| Related descriptions | [Architecture](../ARCHITECTURE.json), [file inventory](../INSTALLATION.json), [source build status and limits](../STATUS.md) |

This edition describes expected behavior and does not expand the previous scope of verification. PACKAGE and the test dossier concern the environment development project, not the results of a new domain project. Describing a capability does not confirm its technical implementation.

---

iEWR helps a person and AI obtain a fit engineering result and organize the necessary work at reasonable total cost. The person sets intent, result value, and delegation limits. AI recovers context, determines the required contribution, selects or develops a method, performs authorized work using the agent environment's means, and checks the result for its use.

English is the primary language of iEWR's own internal methodological, architectural, normative, and operational materials. The user chooses the language of interaction; the task and recipient requirements determine the language of project artifacts. This policy does not require an LLM to reason in English.

## User and use situations

The main iEWR user is a person with an intention and domain competence, able to assess the result's value and fitness. This may be an entrepreneur, engineer, researcher, or manager working alone or in an organization. Some required work may lie outside their execution specialization. The environment helps determine the necessary contributions, find ways to obtain them, and organize authorized execution.

Typical situations are creating a new system, changing an existing one, and research that must first establish what change is needed. Creating a system involves clarifying its use, required result, and necessary contributions. An existing system reuses fit decisions, code, and evidence. In research, grounds that distinguish options and prepare a human choice can be a sufficient result. A new task does not require traversing a full development cycle or reconstructing the entire system from scratch.

The expected value of iEWR is a shorter path from intent to a fit result while preserving engineering responsibility. Goals and undelegated tradeoffs remain with the person. Work is bounded by available competence, sources, means, and mandate. A necessary external or specialist contribution cannot be replaced by a capability description.

## System formation and work organization

**System Formation** connects work to the system being formed: why it is needed, who will use it and how, what properties it must have, and what already exists. The agent establishes which contribution is needed in the system's current state and the grounds for that choice. Sometimes the design must change; sometimes knowledge must first be obtained, a criterion clarified, a decision agreed, or missing authority provided.

For the next significant decision, the agent connects the assignment to system use, structure and state, surroundings, constraints, and current decisions. It recovers significant dependencies and distinguishes facts, assumptions, decisions, and unknowns. This is a whole engineering context: the depth of its recovery is determined by the upcoming decision and consequences of error, not by the number of files read. Sufficient information is reused while it remains applicable.

**Runtime** means that necessary work is determined and reorganized during execution. A new fact, checking result, or human decision may change the next question, method, participants, or action sequence. The agent reviews affected decisions and results while preserving the fit part and current constraints. Work can be added, combined, reorganized, or canceled; significant changes to goals and criteria remain with the person unless that choice is delegated.

If an unknown can change an action's admissibility or result, either obtain information that distinguishes the possible situations, choose an action or conditional plan that is admissible and fit for the assigned result in every still-possible situation consistent with available information, or withhold the dependent part. A detailed model is needed only when it helps such a decision. Work finishes when the result is sufficient for the assigned use and significant effects are accounted for.

For a domain system, iEWR forms part of the supporting engineering team. In assigned self-development, the environment itself becomes the target system. In both cases, results and feedback determine further work. A universal operation sequence and a separate software engine are not mandatory for this.

## Methodological basis and applied repertoire

**FPF is the methodological basis of iEWR.** The exact original contains general concepts, distinctions, principles, and methods. If its content is sufficient for the task, the agent applies it directly, preserving significant conditions and dependencies.

**MethodPack (MP) is the applied repertoire.** It contains domain methods, local operations supporting iEWR, necessary adaptations, and accumulated experience. An MP method can be the primary working method for a specific task. An addition to the repertoire explains what it adds to the available basis and why the result's recipient needs it.

**Dynamic Method Generation (DMG)** finds, reuses, adapts, or develops a sufficient method for the current task. Sources include FPF, professional knowledge, authorized domain materials, and experience. A one-off action does not require a new maintained method. A repeatedly useful contribution is retained together with grounds, applicability conditions, and checking limits.

For a new choice, first check whether FPF is sufficient. If domain specifics or adaptation are needed, turn to MP. Obtain a missing method through DMG; if necessary sources or means are unavailable, state the exact unclosed gap. Reuse an already read sufficient method while its conditions hold; a full FPF traversal and repeated search before every operation are unnecessary.

Instructions establish the instance entry, rules for connecting the basis, conditions of the specific environment, and human participation. Navigation helps locate the full description of a selected edition but does not replace its content or create a new methodology. A significant method has one principal content location.

DPFs can serve as coherent professional sources. The presence of a DPF, a YAML entry, and previous success do not make a source mandatory for every task or automatically raise quality. Its provenance, edition, attribution, and limits are preserved.

## Participants and environment boundary

| Participant or means | Contribution |
|---|---|
| Human | Intent, value, mandate, significant undelegated decisions, and selected participation |
| AI and other performers | Forming and performing work within the assignment, available capabilities, and authority |
| FPF and MP | Methodological content, conditions, and explanations of methods |
| Agent environment ADE | Tools, computation, access, and actual technical constraints |
| Project resources | Sources, decisions, exact editions, results, evidence, and continuation basis |

The current iEWR configuration connects these contributions for the assigned work. One person and one agent may be sufficient. Additional participants and technical mechanisms are needed when they provide a required property at acceptable cost. Using an external service does not itself include all its infrastructure within iEWR.

## Teams working together

An engineering team brings together people, AI performers, methods, and means to obtain a coherent contribution to the system. A team acts within its mandate. Additional teams are needed when separate competencies, responsibility, or execution capabilities are required.

| Relationship between participants and teams | What must be agreed |
|---|---|
| Mandate and delegation | Assigned contribution, responsible party, admissible decisions and effects. Transferring an assignment does not itself expand the recipient's authority |
| Delivery and acceptance | Recipient, exact result edition, fitness conditions, evidence, and limits. Who may accept the contribution and what else is required for use |
| Interfaces and integration | Compatibility of contributions and their premises, dependencies, and significant changes. Fitness of the whole is checked separately from readiness of parts |
| Escalation | Which question exceeds authority or capability, to whom it is transferred, and which dependent work is withheld |

A significant decision or change of grounds is communicated promptly to those whose work depends on it. The recipient recovers the assignment, editions, constraints, and unknown effects. Shared file space does not itself provide consistency or isolation. If a necessary contribution, permission, or protection is absent, the dependent part is withheld; independent authorized work may continue.

Team allocation need not mirror product structure. System integrity is preserved through agreement on use, criteria, and dependencies and checking the joint result. Several participants may supply one function, and one participant may perform several functions. The coordination method is selected according to the task and actual ADE capabilities.

## Seven functions and their relationships

| Function | Required contribution |
|---|---|
| CF — Context Formation | Sufficient current grounds for the next decision, including significant unknowns |
| SF — System Formation | The contribution the system needs for its specified use and its fitness conditions |
| DMG — Dynamic Method Generation | A sufficient executable method and joins, or a specific unclosed gap |
| EG — Execution Governance | Admissibility of a specific action under the current mandate and protective means |
| WEC — Work Execution & Continuation | Completed work, actual effects, and sufficient grounds for continuation |
| RAF — Result Assurance & Feedback | A checked fitness conclusion and return of a defect to the affected basis |
| HI — Human Interaction | An exact assignment or decision, preserved human participation, and understandable result delivery |

CF, SF, and DMG form the Generative Core; EG, WEC, and RAF form Governance. HI connects work to the person. The functions support both domain activity and management of the environment itself. They are not seven mandatory stages, methods, teams, or agents.

CF supplies grounds for SF. SF connects the necessary result to a DMG method and RAF criterion. EG checks admissibility of the specific action performed by WEC. RAF compares what was obtained with the required use and returns discovered defects to dependent decisions and results. HI preserves human choice throughout these relationships. If the necessary contribution is already provided, the remaining functions need not be performed again.

## Human participation and action admissibility

**S3 is joint thinking.** The agent explores the question and prepares grounds while preserving the selected human participation. **S4 is delegated work.** The agent independently makes necessary ordinary decisions within the agreed scope. S4 does not prohibit human participation or automatically expand the mandate.

A **Human Gate** is needed for a significant undelegated decision: changing a goal, choosing a tradeoff, expanding authority, or permitting an effect. An agreed choice is reused. A conditional answer is preserved together with the presented subject, edition, and condition. Until the necessary decision exists, the dependent part is withheld while independent authorized work continues.

Authority, performer capability, technical access, and evidence of quality are different grounds. Before a significant action, check whether the mandate covers the specific performer, action, resource, scope, and current conditions. For deferred execution, account for permission revocation, time limit, and subject changes. Publication, deployment, and access to external systems remain within direct assignments.

### Selecting technical protection

A methodological prescription does not itself guarantee execution. Choose control according to the protected condition and consequences of violating it:

- If an error may be detected and corrected before significant use of the result, methods, observation, and correction may suffice at acceptable total cost.
- If a violation is inadmissible and its consequences cannot acceptably be corrected after the action, technical protection is required to maintain the boundary independently of the correctness of the agent's decision.
- If ADE does not provide the required limit, change execution conditions, narrow available effects, choose other means, or withhold the dependent action.

For a significant control, it must be clear which condition it protects, where the requirement came from, who may change it, and which mechanism actually operates. Control states are distinct:

| State | What is established |
|---|---|
| `declared` — stated rule | An action is prescribed or prohibited, but this does not establish technical enforcement |
| `enforced` — technical enforcement | An actual ADE mechanism maintains the required constraint under established conditions |
| `compensated` — admissible compensation | Missing support is replaced by an acceptable method; grounds for admissibility and substitution limits are known |
| `unsupported` — absence of support | The required condition is not provided |

Evaluate compensation against the protected condition, consequences, and current permission. It must provide the necessary property within agreed boundaries; its limitations and residual risk are retained with the grounds for admissibility. Agreement to an individual operation does not remove a mandatory constraint. If a mandatory condition is unmet and no admissible compensation exists, the dependent action is not performed.

Shared file space and a new agent context do not themselves provide isolation. The presence of a tool does not prove control fitness: necessary properties are established for the actual ADE configuration and specific action.

## Result and continuation

A result is assessed by whether its recipient can use it for the assigned purpose. Criterion, observation, and conclusion retain distinct roles. Counts of files, options, operations, or passed minor checks do not replace a significant property of the whole.

When a source, condition, performer, or means changes, review the dependent part of the work. A historical edition and observed event are preserved: correcting today's conclusion does not rewrite the past. If an operation's effect is unknown, first reconcile the state of that same attempt, then select an admissible continuation.

Project materials have stable roles: `project/source/` holds direct inputs, `project/reference/` reference and historical sources, `project/artifacts/` results and checking grounds, and `project/handoff/` continuation. Internal organization is chosen according to use. Repeatedly useful methods reside in one `methods/`. Facts, assignments, and specific executions remain working materials and do not automatically become methods.

Handoff to the next performer requires the current assignment, significant decisions, exact basis used, obtained results, known and unknown effects, open question, and continuation conditions. An existing sufficient recording system is reused. A mandatory universal log, scheduler, or document set is not required.

## Example of work on an existing system

This is a constructed example. In an existing system, a new customer cannot submit an inquiry without a contract number. The person assigns investigation of the cause and preparation of a checked change in a separate copy. The new product rule and publication remain with the owner.

Checking shows that the form and server consistently require a contract, although the use description includes a new customer. Fixing one field will not resolve the semantic contradiction. The agent prepares options: a normal request without a contract, a separate preliminary inquiry, or retaining the constraint with changed use conditions. While the owner's decision is needed, independent investigation of consequences continues.

The owner chooses a preliminary inquiry with a responsible recipient and without starting order execution. The agent preserves the choice and aligns the form, server rules, and processing route. The entire path is checked: a new customer can submit an inquiry, the responsible person receives the required information, order execution does not begin, and the previous path for a customer with a contract is preserved. The method is selected through FPF and the applied MP, taking the established contradiction into account.

Handoff includes the prepared edition, observations, and checking limits. Successful local tests do not mean publication or prove behavior of the live system. If only checked preparation was assigned, work finishes at this handoff.

## Deviations and returns

| Situation | Required continuation |
|---|---|
| Existing FPF is sufficient | Apply the original contribution without a new MP method that repeats its content |
| Local specifics are needed | Open the full description of the suitable MP edition and its conditions |
| The required method is absent | Develop the missing contribution through DMG and check it for current use |
| A significant source or means is unavailable | Name the dependent gap; continue the authorized independent part |
| Grounds have changed | Review dependent conclusions, preserving what remains fit and the history |
| A response is lost with a possible effect | Reconcile the same attempt; absence of a record does not prove absence of action |
| Work is handed to another performer | Recover the assignment and significant grounds without repeating completed work |
| MP is empty | Begin with the connected FPF, sufficient professional knowledge, and authorized sources |

## Success criteria

Success is a fit result within the mandate and at reasonable total cost. For a specific use, select significant questions from the table. Before a readiness conclusion, each requires conditions, sufficient observation, and an indication of failure. The table helps construct checking; it does not prescribe a mandatory complete test list or an overall score.

| Characteristic | Assessment question |
|---|---|
| Usefulness | What benefit needed by the recipient does the result provide, or what grounds support expecting it in the assigned use? |
| Fitness | Can the recipient use the result for the assigned purpose under the stated conditions? |
| Checkability | Are significant properties confirmed by suitable observations, distinguishing criterion, evidence, and conclusion? |
| Autonomy | Is necessary work performed without unnecessary human intervention while preserving the selected S3/S4 and delegation boundaries? |
| Governability | Are the mandate, admissible effects, and necessary human decisions preserved; are mandatory constraints provided by actual means or admissible compensation? |
| Adaptability | Are affected decisions, methods, and actions reviewed when significant facts or conditions change? |
| Continuity | Can the next performer recover the assignment, exact grounds, results, and effects and continue without losing significant information or repeating completed work? |
| Total cost | Is the combined burden acceptable, including human attention, checks, corrections, and support; is there a comparable alternative for a claimed gain? |

Confirmed, unfit, unknown, and unchecked results are delivered separately. Failure of a significant condition is not compensated by a count of positive answers. The example above helps prepare checks but does not serve as evidence of actual use. Success of an individual trial concerns its configuration and conditions. Robustness and savings require corresponding observations.

Total cost includes search, reading, execution, checks, corrections, tool support, and human attention. A conclusion of gain requires a comparable alternative. Text compactness and degree of autonomy do not themselves establish it.

## Environment development

iEWR self-development starts with a direct assignment and uses the same architecture. A change must improve the required behavior of the whole while preserving the source basis and a return path. Ordinary accumulation of MP methods does not require changing the entire environment.

Creating or substantively revising a DPF has its own entry to the canonical method in the exact FPF. A sufficient result may be an ordinary fit procedure, an addition to an existing description, or more convenient access. The existence of a coherent MP book does not by itself make it a canonical DPF.

The concept supports AI-native-first: necessary functions are preserved as models, methods, and tools change. The strongest available performer receives admissible work, while the person retains control of goals and responsible decisions. The methodological basis is FPF; the applied repertoire is MethodPack; technical execution is ADE.

Current iEWR work and development of the project MP use sufficient ADE means without mandatory Python; an available suitable helper is reused. The FPF edition is changed when assigned: a prepared coherent original/index pair is connected with provenance and checking according to [FPF_INDEX.md](FPF_INDEX.md). Local index generation is not a condition of current work.

## Changing the concept

ConOps is changed on a grounded proposal and Human decision relating to the presented edition and its conditions. A proposal shows the difficulty or new grounds, affected provisions, expected behavior, reasonable alternatives, and consequences for use, architecture, and implementation. Architecture, distribution composition, and verification limits are checked separately. New text does not by itself change them or authorize implementation or publication.

A direct assignment to revise the concept within agreed boundaries provides grounds to perform and check the revision. Repeated general approval of ordinary steps is unnecessary. A significant new choice of goal, tradeoff, or authority beyond the assignment is presented through the Human Gate. Until a decision, the accepted edition of the affected provision is preserved, the proposal is marked separately, and dependent work is withheld.

When a change is accepted, preserve the exact previous edition, decision grounds, change scope, and a sufficient return path. Continuation pointers are connected to the actual current edition; historical results remain tied to their previous basis. Check affected provisions and relationships of the whole without a mandatory complete traversal of the unchanged basis.

An implementation defect or limitation may justify a proposal but does not automatically change the concept. A version limitation is stated together with the affected use and admissible continuation. The concept is not rewritten to justify the chosen implementation. An unmet mandatory condition without admissible compensation still withholds dependent action.
