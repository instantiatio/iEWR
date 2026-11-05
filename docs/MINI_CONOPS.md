# iEWR: Architecture and Mini ConOps

*iEWR 7.0.5 Eternal Alpha · 5 November 2026*

<!-- Three conceptual pages; two explicit breaks for printing and export. -->

## 1/3. Architecture: human, methodology, work

**iEWR is an engineering environment for human–AI collaboration.** The person sets intent, the value of the result, and limits of autonomy. AI helps form the necessary work, select a method, perform the assignment, and check the result for its use. A system already in operation with accumulated context can be the starting point.

The architecture rests on **Instructions + FPF + MethodPack**. Instructions connect the environment, sources, and current rules. **FPF—First Principles Framework by Anatoly Levenchuk—provides general concepts, principles, and methods. MethodPack (MP) contains applied methods and project experience.** The model's domain knowledge and available sources supplement this basis.

Technical execution is provided by **ADE—the agent execution environment**: files, commands, programming, search, a browser, and external systems within the access granted. Assignment, performer capability, and technical access are accounted for separately.

### Seven functions

| Function | Contribution provided |
|---|---|
| **CF — Context Formation** | Sufficient current context: task, system, sources, decisions, and significant unknowns. |
| **SF — System Formation** | Determining the necessary system change, expected use, and result criteria. |
| **DMG — Dynamic Method Generation** | Obtaining a suitable method: search, reuse, adaptation, or creation. |
| **EG — Execution Governance** | Checking admissibility of a specific action, constraints, and execution conditions. |
| **WEC — Work Execution & Continuation** | Performing work, accounting for actual effects, and enabling continuation. |
| **RAF — Result Assurance & Feedback** | Checking result fitness and returning discovered problems to their grounds. |
| **HI — Human Interaction** | Joint thinking, delegation, human decisions, and understandable delivery of results. |

CF, SF, and DMG form the **Generative Core**. EG, WEC, and RAF form **Governance**. HI connects the person to all the work. The seven functions are selected and combined according to the task; an existing sufficient contribution is reused.

```text
Human ⇄ HI ⇄ Generative Core: CF · SF · DMG
                         ⇅
                 Governance: EG · WEC · RAF
                         ⇅
                 Work · effects · result
```

Results and feedback update context, the system representation, and ways of working. These functions support both domain activity and management of iEWR itself. Changing the environment starts with the corresponding human assignment.

<div style="break-after: page; page-break-after: always;"></div>

## 2/3. DMG and MethodPack: a method for the task, experience for reuse

**The idea of DMG is to obtain a sufficient method for the current task.** The agent starts with the required result and checks which actions, knowledge, conditions, and means make it achievable. An existing suitable method is applied directly; development is required where a significant gap remains.

A new choice follows **FPF → MethodPack → missing development**. First, the agent looks for a sufficient principle or method in FPF and reads the original section with its conditions. If domain specifics are required, it opens the corresponding MP body. It closes any remaining gap by adapting or constructing a method from professional knowledge, available sources, and experience. DMG covers this entire mechanism. An already established sufficient basis is reused while its conditions continue to hold.

### What MethodPack accumulates

MethodPack is a **coherent applied project repertoire**: one book with thematic blocks and a YAML index. It contains methods supporting iEWR work, general-purpose methods, and accumulated specialization. One method can serve several areas of use.

A useful method's description preserves:

- the task, expected result, and conditions of use;
- necessary inputs, means, and performer preparation;
- actions, significant connections, branches, and stop conditions;
- grounds: exact sources, editions, and available experience;
- checking methods, observed results, and limits;
- relationships with other methods and review conditions.

Relationships help connect contributions and find alternatives. The YAML index leads to an exact body and edition. A separate structural FPF index helps locate sections in the original; recommendations by work question are in task entries.

**A repeatedly useful method is retained with its grounds and limits.** Project facts, assignments, and individual executions remain working materials. A simple one-off action may finish with a result without a new MP entry. An empty repertoire permits starting work using FPF and sufficient professional knowledge.

### How the repertoire develops

A DPF—Domain Principles Framework—may be supplied as a domain source of connected principles and methods. Its useful contributions are considered when forming a method; original provenance is preserved. Creating a standalone DPF has a separate entry to the canonical FPF method.

When a used description changes, its previous edition is preserved. The agent prepares a new book, index, and snapshot, then performs IE-M003 using available means. The supplied Python helper uses **`activate`**; the bounded alternative is a file procedure with one agreed writer. Both require checking before activation, preservation of previous files, and result verification. An assignment through chat is sufficient; no special Human command is required. The substantive fitness of a method is checked against the task and its application result.

<div style="break-after: page; page-break-after: always;"></div>

## 3/3. Mini ConOps: from assignment to continuation

### Human participation

In **S3**, the person and agent jointly explore a question and make decisions. In **S4**, the agent is delegated autonomous work within agreed boundaries. The person retains undelegated decisions about goals, significant tradeoffs, and new commitments. Ordinary necessary actions are performed within the assignment already given.

### Example: changing an existing CRM

> Add expiry dates to commercial proposals. The final day is included. Preserve old accepted documents. Prepare and check the change in a separate system copy.

**1. Recover the basis.** The agent reads the assignment, current decisions, available sources, and continuation materials. It establishes how proposals, editions, permissions, and data work. It clarifies only unknowns that obstruct the next significant decision: for example, the calendar-date source or the rule for old drafts.

**2. Determine the required change and method.** The required result is connected to the data model, server rules, interface, and document history. Through FPF and MP, the agent finds sufficient general and applied methods. Existing serialization of changes is reused; expiry and migration rules receive the necessary adaptation through DMG.

**3. Perform the authorized work.** The agent preserves the initial state, prepares the change in the assigned copy, and uses available ADE tools. New information can change the plan. If a mandatory source, means, or permission is missing, the dependent part is withheld while useful independent work continues.

**4. Check the result for use.** Boundary dates, immutability of accepted proposals, data preservation, permissions, and concurrent operations are checked. A discovered defect is corrected together with affected grounds; dependent checks are then repeated. Preparation and checking of the copy finish with delivery of the result; activation in the live system occurs within a separate current assignment.

**5. Preserve experience and hand over the work.** A repeatedly useful adaptation becomes a new edition of a local method. The previous body, checking grounds, limits, and review conditions are preserved. Handoff includes what was done, actual effects, open questions, and sufficient information for the next performer.

The scenario adapts to system state: actions can be combined, repeated, or finish at an already sufficient result. With a new requirement, the agent reviews affected decisions and methods while preserving applicable results.

### Working memory and success criterion

Inputs go in `project/source/`, reference materials in `project/reference/`, results and checking grounds in `project/artifacts/`, and continuation in `project/handoff/`. Repeatedly useful methods are in `methods/`. Sufficient grounds for the next action are preserved; a mandatory document set for every task is not required.

**Success is a fit result within the mandate and at reasonable total cost**, with understandable checking grounds and the ability to continue. AI-native-first means readiness to change models, tools, and specific methods as capabilities develop while preserving human goals and engineering responsibility.

*Description basis: [iEWR ConOps](IEWR_CONOPS.md), [MethodPack rules](PROJECT_METHODS.md), [activation control](METHODPACK_CHECK.md).*

Current iEWR work and development of the project MP use sufficient ADE means without mandatory Python; an available suitable helper is reused. Changing the FPF edition is maintenance of the methodological basis: when assigned, a prepared coherent original/index pair is connected with provenance and checking according to [FPF_INDEX.md](FPF_INDEX.md). Local index generation is not a condition of current work.

### Grounds for decisions and readiness

Before a significant decision, the agent recovers sufficient grounds and applies the selected original FPF/MP contribution; before a readiness conclusion, it connects significant assignment conditions to the actual result and checking coverage. Existing sufficient records are reused. A CF card, separate stage, and full repertoire traversal are not mandatory. The entry for modification is `change-basis` in navigation/task-entries.yaml. This is a declared rule, not a technical write prohibition or proof of compliance by every model.
