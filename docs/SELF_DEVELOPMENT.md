# iEWR self-development

This mode starts with a direct Human instruction to change the environment itself: its behavior, instructions, architecture, or supporting tools. An ordinary phrase stating a clear result and scope is sufficient; no special formula or repeated general permission is required. Observing a defect does not itself authorize changing the environment. Improving a domain method within an already assigned task may remain within that task's scope.

S3 means joint thinking; S4 means delegated work; preserve the selected Human participation. This mode uses the same seven [architecture](../ARCHITECTURE.json) functions. A material new objective, trade-off, or authority beyond the instruction remains with Human and is presented through a concrete result.

## Source project and instance edition

Start with [PACKAGE.json](../PACKAGE.json). The version field identifies the installed distribution version; repository.url is iEWR's own source repository; source_edition identifies this build's exact immediate basis. For a local basis, retain the archive name and SHA-256; do not assume that the local copy corresponds to a Git commit. repository.public_baseline separately pins the public baseline of the source line. It does not replace the installed build or its immediate basis. FPF properties and its source repository are recorded separately in external-sources/fpf/SOURCE.json.

When instructed to compare the environment with upstream or update it:

1. Preserve the actual instructions, distribution, and project changes before editing. Establish the exact source edition from PACKAGE.json; do not infer it from the directory name, main, or the latest release number.
2. Consult repository.url and releases_url within the instruction's scope. Pin the selected external edition by exact commit or digest of the received archive. Test network and repository access through the current ADE.
3. Distinguish the installed instance, its preserved basis, and the selected candidate. Compare upstream changes with local changes and dependencies, preserving necessary project specialization. Public 6.0.8 is not an update to the installed instance merely because it is available in the repository.
4. Prepare a separate candidate copy, check the affected properties, and connect it using the operations below. In the new PACKAGE.json, record the actual immediate basis and its exact edition; do not assign an unproven Git correspondence.

If the network or exact previous basis is unavailable, identify the comparison limit and hold the dependent conclusion about upstream compatibility. Authorized local changes can continue while preserving the actual before state. The repository link provides navigation; updates and publication remain within the effective instruction.

Preserve exact source editions, method versions, and provenance independently of the new build's name.

## README and release information

Use `iEWR <version> Eternal Alpha` as the release title. Name the archive `iEWR-<version>-Eternal-Alpha.zip` and its root directory `iEWR-<version>-Eternal-Alpha`. Do not add prefixes or suffixes.

README contains the agreed iEWR description: purpose, project examples, getting started, methodological basis, transfer procedure, and links to detailed materials. A version change alone does not authorize rewriting this description, restructuring its sections, or making stylistic or substantive changes. Such edits require a separate Human request; a direct instruction to change README within agreed bounds is already sufficient, without repeated general approval of routine steps.

When preparing a new version without a separate README instruction:

1. Preserve the exact previous edition and use it as the basis. Update only numerical values that actually changed, such as version or method count, including corresponding numbers in paths and links. Keep numbers that remain true; do not automatically update historical dates.
2. Put new features, changes, checks, and release limits in RELEASE_NOTES.md, with a link to README.md. Do not duplicate the getting-started section or authorship/license details in release notes; they remain in README and the dedicated files.
3. Compare README before and after. Without a separate text instruction, each difference must be explainable by a confirmed numerical change. If no such values changed, leave README unchanged.
4. If a new version makes the agreed description false, identify the specific discrepancy and propose an edit to Human. Do not rewrite it on your own initiative or present the discrepancy as merely a version-number update.

The procedure for transferring an existing project's materials is in [README](../README.md#project-transfer-into-the-environment). Start another project with the original clean distribution; copying an accumulated working directory may transfer another project's methods and history. During an update, preserve sources, data, methods, decisions, and unfinished work; do not blindly overlay a new distribution onto a project. Technical conditions for updating the environment and MethodPack appear in the corresponding sections of this document and METHODPACK_CHECK.md.

## Change acceptance conditions

Before connecting a new edition, check the following conditions within the agreed change scope. They clarify the material-result check and activation conditions in “Carrying out a change” and also apply when changing these rules themselves.

1. **Clarity and preservation of meaning — F.19.** From the changed instructional passages, stated prerequisites, and task inputs, the intended reader can recover who must act, what to do, with what, under which conditions, and toward which result. Compare old and new text: preserve meaning, material distinctions, restrictions, and operational details; a substantive change must be grounded in the instruction or an accepted decision. Reread changed text with neighboring passages on which its meaning depends.
2. **Effective authority — A.2.8.PER.** The work and proposed activation fit the current Human instruction, selected S3/S4, necessary permissions, and ADE restrictions. Finding no prohibition, having file access, or holding an earlier permission does not itself establish missing current authority. Routine actions within already assigned bounds follow the effective rules without repeated general permission.
3. **Affected uses — A.10.1 and C.39.MC.** Compare changed claims, conditions of use, and availability. If compatibility is established, the necessary reference repair is sufficient. If a change can affect a consumer's action or result, find the actual dependent uses and check affected decisions, instructions, methods, or continuations. Retain sufficient results for unaffected uses. State material search limits and unknown dependencies; no visible edit in a consumer does not establish its independence.
4. **Suitability of the criterion and checker — C.41.QC.** The criterion answers a material work question, and the person, tool, or model can actually distinguish the required states from the available data. Reuse sufficient prior qualification. If suitability is unestablished, test discrimination between a satisfactory case and a plausible violation with grounded expected answers; consider false-success and false-rejection costs. When the criterion, checking means, its inputs, or conditions materially change, recheck the affected conclusion. Establish the suitability of the check separately from the answer about the change itself.
5. **Evidence and readiness limits — A.10.** Connect every material conclusion to the result actually obtained, the edition, and the conditions it covers. Distinguish author analysis, another participant's reading, file checks, and observed actual use. Claim only supported readiness; report violations, unchecked matters, and limits separately under AGENTS. Reuse historical results only while their grounds remain valid; a successful check does not close an omitted requirement or known defect.

When changing a method or its description, first distinguish editorial changes to the description from changes to the reusable way of doing: compare affected actions, entry and stop conditions, participants, result, and applicability. If only wording changes while meaning is preserved, a local description check is sufficient; do not initiate variant development. When an actual or unclear change to material semantics raises a method-identity or variant question, use A.3.1.MV: justify preserving identity, a refinement, or a new Method and the necessary edition. Preserve provenance and the limits of earlier evidence; a new description edition does not itself prove a new method or its suitability. IE-M003 still applies to a new MP pair.

For a material change to work support, handoff, or continuation means, use A.15.8: establish the dependencies and state required to continue, where they can be recovered, and who can change and use them. Check them in a proportionate representative situation involving interruption, handoff, or lost support; preserve what was observed, what remains unchecked, and the recovery or stop condition.

Select checks by consequences and material unknowns; reuse sufficient earlier results under unchanged conditions. Obtain an independent reading if an action-changing ambiguity remains, an observed miss makes prior reading insufficient for the affected instructions, or actual reader understanding or mastery is claimed. Give the cold reader the text, stated prerequisites, and task inputs while withholding the author's rationale, hints, and expected answers. Obtain the reader's initial understanding before explanation; state assistance and familiarity with the previous edition as trial conditions. Limit the conclusion to the tested text, question, reader preparation, and reading conditions. Test correct recovery of the instruction separately from practical suitability.

Use a sufficient decision or result record already needed for the work. Acceptance itself does not require separate cards, a full traversal of FPF or every method, a new MP method, or a mandatory document cycle. When the conditions are met, the new edition is accepted within the agreed scope; this does not itself establish production admission. A material unresolved condition holds only the dependent activation or conclusion: report the specific gap and continuation condition, and continue useful independent work.

## Carrying out a change

For a new method choice, first check a sufficient FPF principle/method under the [connection rule](../AGENTS.md#method-source-priority). C.39.MF helps resolve an unclear Method/non-Method focus; C.39 obtains missing methods and joins; C.39.MC supports continuation under changed conditions; C.43 connects observation, choice, and action and checks the effect. Do not search again for an already sufficient basis. A.10 distinguishes a historical report from a new actual check; an old specific event does not transfer to the current edition.

[IE-M004 v1.9](../methods/METHOD_PACK.md#ie-m004-v1-9) provides local operations: recover the instance and current/candidate boundary, preserve before, prepare an authorized copy, change genuinely dependent references, run available checks, reconcile actual current, and connect the edition only when activation conditions are met. [IE-M003 v1.9](../methods/METHOD_PACK.md#ie-m003-v1-9) coordinates book/index/snapshots and the writer. These IDs are not universal start prerequisites: with an empty MP, direct FPF and a professional method allow assigned work while preserving the source and checking the material result.

Use only actually supplied and available ADE means. If a supplied validator/test exists, establish its availability and scope and apply it to the relevant properties. Otherwise check changed paths/anchors/editions, source availability, current pointers, and material behavior with available means. Identify unchecked matters precisely; a file, walkthrough, or single trial does not prove actual use, general reliability, or savings. When the effect of a write is unknown, recover the actual state of the same attempt first.

A saved current handoff is a state pointer, not a new instruction. A checked candidate may be handed over with an exact activation blocker; do not change effective current when activation is outside scope or a material condition is unmet. Publication, deployment, connecting external means, and changes to the original FPF require their own grounds. Finish with the sufficient assigned result or return the useful portion, held part, and continuation condition, without a mandatory document cycle.

Creating and substantively developing a DPF is a separate Human mode under [DPF_CREATION.md](DPF_CREATION.md) and the original canonical FPF method. Recording an ordinary local method or changing this environment does not replace its authoring/qualification.

If the change includes a new MethodPack pair, meet IE-M003 requirements using a sufficient [activation implementation](METHODPACK_CHECK.md) supported by the ADE: check the candidate before replacing current, preserve the previous state, and reconcile the result. MethodPack checking does not replace the criteria for the entire environment change.

Changing the FPF edition is maintenance of the methodological basis: the main path is a prepared, coherent original-and-index pair with provenance, terms, and sufficient verification grounds under [FPF_INDEX.md](FPF_INDEX.md). It requires an instruction and preservation of previous dependent uses. Local generation with the supplied Python tool is a separate preparation operation; current iEWR work and MP development do not require it.
