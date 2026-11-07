# iEWR 7.0.8 Eternal Alpha

iEWR is a research engineering environment for collaboration between people and AI. You specify the result you need, why it matters, and the bounds within which the agent acts independently. The agent helps shape the work, select methods, carry out the assignment, and check the result.

The environment helps turn an idea into a usable result: understand the task, identify the work needed, connect participants' contributions, and preserve the grounds for checking and continuation. You can assign it, for example:

- developing an application or changing an existing software product;
- preparing an engineering concept for a system or workflow;
- investigating a question, comparing options, and preparing a reasoned decision.

**Eternal Alpha** indicates the environment's research character: its design and methods evolve through use. The suitability of each result is checked for its intended use.

## Getting started

1. Extract the archive and open the `iEWR-7.0.8-Eternal-Alpha` directory in an agent environment that can read and modify files and perform the actions your task requires.
2. Have the agent read [AGENTS.md](AGENTS.md) if the environment does not load it automatically.
3. Describe the task, required result, and material constraints. Put materials in `project/source/` or point to an existing working context.
4. Results are saved in `project/artifacts/`; materials for handoff and continuation between people and agents are saved in `project/handoff/`.

English is the primary language of the environment's own active internal materials. Communicate with the agent in your preferred language; project outputs follow the task and recipient's requirements.

For example: “Study the materials in project/source/, propose a solution, and discuss the material options with me.” Or: “Prepare and check a solution independently within these bounds.”

## Ask the environment itself

The most convenient way to learn about iEWR's capabilities and design is to ask an agent working in it. For example:

- “List the methods in the MethodPack and briefly explain what each is for.”
- “How can I transfer an old project here while preserving its materials and unfinished work?”
- “How is iEWR organized, and how are its seven functions connected?”
- “Which actions can you perform here, and which require additional tools or access?”

## Methodological basis

The working combination is **Instructions + FPF + MethodPack**. FPF (First Principles Framework), by Anatoly Levenchuk, provides general methodology; the exact original is included. MethodPack is the applied repertoire: one thematic book and a YAML index with 37 method descriptions. For a new choice, the agent first checks for a sufficient FPF contribution, then the necessary MethodPack detail, and develops what is missing for the task.

This mechanism is called **Dynamic Method Generation (DMG)**. It covers finding, reusing, adapting, and creating ways of doing work. Methods useful again accumulate with their grounds, relations, checks, and preserved editions. Neither a full FPF traversal nor use of the entire repertoire is required.

You can request methods directly: “Apply TEXT-EDIT from the MethodPack to this text.”

- [File map](docs/FILES.md): purposes and locations of distribution files.
- [Method catalog](docs/METHOD_CATALOG.md): available methods and links to their descriptions.
- [Architecture overview and mini ConOps](docs/MINI_CONOPS.md): how the environment works, with an example.
- [Full ConOps](docs/IEWR_CONOPS.md): concept of operations, participants, functions, and working conditions.

## Project transfer into the environment

Choose a way to provide an existing project's materials to the agent:

1. **Specify the project directory path.** This is a convenient first step: the agent can study the project before transferring materials.
2. **Copy the whole project directory into `project/source/`.** This suits small projects.
3. **Put a ZIP of the project directory into `project/source/`.** This is the preferred way to transfer an entire project.

State what the agent is assigned to do with the project: study materials, propose a solution, or prepare a change. Preserve sources, data, methods, accepted decisions, and unfinished work. For changes, the agent prepares a working copy in an agreed location; original materials are preserved. Do not blindly extract a project archive over the environment files or working directory.

## Developing the environment

When instructed, the agent can [develop the environment itself](docs/SELF_DEVELOPMENT.md) and [create coherent domain methodologies (DPFs)](docs/DPF_CREATION.md) using the canonical FPF method.

## Project and releases

[Download iEWR 7.0.8 Eternal Alpha](https://github.com/instantiatio/iEWR/releases/download/7.0.8/iEWR-7.0.8-Eternal-Alpha.zip) · [SHA-256](https://github.com/instantiatio/iEWR/releases/download/7.0.8/iEWR-7.0.8-Eternal-Alpha.zip.sha256) · [Release page](https://github.com/instantiatio/iEWR/releases/tag/7.0.8).

[iEWR repository](https://github.com/instantiatio/iEWR) · [Published releases](https://github.com/instantiatio/iEWR/releases) · [Release changes](RELEASE_NOTES.md).

## Authorship and terms

Copyright (c) 2026 Instantiatio EWR contributors

- Distributed under the [MIT License](https://github.com/instantiatio/iDPF/blob/main/LICENSE)

[This distribution's full MIT text](LICENSE). The external MIT link above points to the license text in the iDPF repository. Independent sources retain their own terms: [applied-method authorship](docs/METHOD_SOURCE_NOTICES.md), [exact sources and editions](ORIGINS.json).

FPF — [Anatoly Levenchuk](https://ailev.ru/). [Author's FPF repository](https://github.com/ailev/FPF). The [exact edition and provenance](external-sources/fpf/SOURCE.json), [CC BY 4.0](external-sources/fpf/LICENSE), and [third-party material terms](external-sources/fpf/LICENSING.md) are preserved. Distribution does not imply endorsement of iEWR by FPF's author.
