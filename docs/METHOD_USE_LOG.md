# Project method-use log

Keep the log in `project/artifacts/method-use-log.md`. Create it on first use and add entries during ordinary project work. Use it to recover what was done, continue the work, and compare past applications when choosing a method for similar conditions.

## Record an application

Record a method once it has made a concrete contribution to a decision or been carried out at least in part. Finding, reading, planning to use, and citing a method are separate from application. If one of those events matters to understanding the work, keep it in the task evidence or label it explicitly as reading or preparation. Identify the FPF contribution or MP method used. Where a local adaptation mattered, state what was adapted or point to the explanation.

Use one Markdown list item on one line by default. Use the task's stable ID or a short label that identifies it within this project. Give the MP ID and edition, or the FPF pattern and relevant section with its source edition recoverable from the entry or a pinned log header. The distribution's `external-sources/fpf/SOURCE.json` supplies the edition to pin. Keep old edition references when the source changes.

```text
- YYYY-MM-DD · task · FPF section or MP ID and edition · material condition → action or decision → observed outcome · [evidence](relative-path)
```

State the observed outcome in a few words. Include the input, constraint, or assumption when it changes how to interpret or reuse the result. When continuation depends on identifying a mutable input, keep a sufficient edition, fingerprint, or stable reference in the line or linked evidence. Point to existing evidence for the details. Use Markdown links relative to the log file, and retain the necessary linked evidence when transferring the project. If evidence is unavailable or incomplete, say what is unknown or only reported. Claim a confirmed useful effect only when the available evidence establishes that contribution to the task. A completed action or successful result alone may leave the method's effect unknown.

## Update as work progresses

Add the line at the first natural checkpoint after a distinct application. Repetitions within a task can share a line when they have the same material conditions and disposition. Keep significant failures, interruptions, and changes of approach visible. If an outcome is pending or unknown, record the last established state and, when material, what remains to be done. Add a dated follow-up that identifies the earlier attempt when an outcome is learned or the method is resumed, replaced, or corrected. Preserve the earlier conditions and outcome.

When several contributors work in parallel, have one contributor reconcile and append the entries. If a write is uncertain, inspect the actual log before retrying. If the log cannot be written, keep the available record with the task evidence and surface the gap at handoff. Mark any later reconstruction and its evidence limits.

## Retrieve or expand

Read the relevant lines and follow the evidence for the task or method in question. Before relying on a previous application, compare the earlier conditions and method edition with the current ones. Use current handoff records for authority and the next step. Link to the log from those records when an entry matters for continuation.

Add a detailed account on request. Link it to the original entry and include the selection grounds, operative conditions, actions, evidence, outcome and limits relevant to the request. Reuse material already in the project.

The log applies [FPF](../external-sources/fpf/FPF-Spec.md) A.10:4.3 and 4.6 by separating the method, its actual use, and evidence of results. Its compact entry and links adapt A.15.10:4.1–4.2 on preserving material needed for return. It uses ordinary Markdown and file operations.
