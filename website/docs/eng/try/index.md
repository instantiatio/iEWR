# Try iEWR

## TL;DR {#quick-start}

1. [Download iEWR 7.0.6](https://github.com/instantiatio/iEWR/releases/download/7.0.6/iEWR-7.0.6-Eternal-Alpha.zip) and extract the archive.
2. Open the folder containing `AGENTS.md` as a project in Codex.
3. In a new chat, describe your task or ask where to start.
4. Check the result. Discuss revisions and the next step.

Learn iEWR through a task of your own. You do not need to study its internals first; the details below help you get started.

## Download and open the project {#download}

[Download iEWR 7.0.6 Eternal Alpha ZIP](https://github.com/instantiatio/iEWR/releases/download/7.0.6/iEWR-7.0.6-Eternal-Alpha.zip) · [Release and checksum](https://github.com/instantiatio/iEWR/releases/tag/7.0.6)

Extract the archive into a separate folder for your project. You can rename it after the project. Its root should contain `AGENTS.md`, `START.txt`, `methods/`, and `project/`.

Open **this folder as a project in Codex** and start a new chat there. `AGENTS.md` is the entry point that connects the agent to iEWR's instructions and resources.

If the environment does not load `AGENTS.md` automatically, ask: “Read AGENTS.md and follow the iEWR instructions for my task.”

Here and below, Codex stands for an example of an **Agent Harness** with access to project files, command execution, and a model service. The same approach applies to another compatible agent environment. We assume you already know how to use one.

## Start a conversation {#start}

Choose one real, small task. Explain in your own words what you want to obtain, who needs it and why, what materials you have, and what matters. If the result is still unclear, describe a difficulty, a concern, or something you would like to change.

> I have an idea: a website for a small repair workshop. I don't know yet what it should contain. Help me work it through and suggest a useful first step.

If you already know the result you need, assign the work directly:

> Review these materials and compare the possible solutions. Show the grounds for your conclusions and the questions that still need answering.

Ask “What can you do?”, “How should I work with you?”, or request an explanation as you go. This is an ordinary conversation; no special commands are needed.

## What happens next {#work}

iEWR identifies the engineering work needed for the result, selects or develops suitable methods, and organizes their use. When the task is sufficiently clear, the agent starts work. It helps clarify material gaps and brings decisions that need your input back to you.

The way of working changes as facts emerge. A plan, an investigation, or a trial may be useful for the task; you do not have to design the agent's process in advance. Your clarifications and corrections steer what happens next.

You retain the goal, significant decisions, the bounds of independent action, and acceptance of the result. The agent organizes and performs authorized work, checks the outcome, and preserves the basis for continuation.

## Materials and continuation {#continuation}

Put source documents and data in `project/source/` when useful. Finished results appear in `project/artifacts/`. Files are optional: you can describe the task in words.

iEWR organizes the retention of decisions, results, checks, and unfinished work. Tell it about new facts and changed decisions; you do not have to design a context storage system by hand.

After a break, open the same project folder in Codex and start a new chat:

> How can we continue this project? Recover the goal, current decisions, results, and open questions. Suggest the next step.

Keep the whole project folder: its files support continuation between sessions and in a compatible environment. Use a separate copy of iEWR for a separate project.

## Check and refine {#check-result}

Inspect whether the result can serve its intended use. Ask what was actually done, what checks were performed, and what remains unresolved. For software this may mean running a working scenario; for research, examining sources, calculations, and the grounds for conclusions.

If the result does not fit, identify the specific discrepancy and ask for a revision. When it is useful and sufficient, accept it and decide whether further work is needed.

## Next {#next}

- [First experiment](/iEWR/eng/try/first-experiment/) — a small assignment with explicit expected results.
- [Advanced use](/iEWR/eng/try/advanced/) — work with the system as a whole, delegate complex results, and assess fitness for use.
- [Applications](/iEWR/eng/applications/) and [cases](/iEWR/eng/cases/) — possible tasks and work already performed.
- [How iEWR works](/iEWR/eng/how-iewr-works/) — the environment's organization, whenever you want to go deeper.

[Home](/iEWR/eng/) · [Русский](/iEWR/ru/try/)
