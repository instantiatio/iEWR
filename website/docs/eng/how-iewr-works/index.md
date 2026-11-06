# How iEWR works

**iEWR — an AGENTS.md-based agent-native application.** It is not a separate AI model or an agent platform. It runs using the capabilities of Codex or another compatible agent environment.

You specify the result, its purpose, and the bounds of independent action. AI independently organizes and performs the engineering work: the agent determines what is needed, selects methods, executes the assignment, and checks the outcome.

It supports software development and change, engineering concepts and solutions, research, comparison of alternatives, and preparation of reasoned decisions. [Try iEWR](/iEWR/eng/try/) covers setup and getting started on your own task.

## You can begin with an unfinished idea

You do not need to design the agent's workflow or choose its methods. Describe the result you want, even approximately, or ask for help understanding the problem. iEWR can clarify the intended use, identify the work needed, obtain a suitable method, carry out the assignment, and check the result.

You can also ask it to explain its own capabilities, organization, or next steps. [Try iEWR](/iEWR/eng/try/) shows ordinary first messages and how to continue work; [Applications](/iEWR/eng/applications/) describes the wider range of work.

## Your contribution and the agent's work

You define intent, value, important constraints, and the decisions you retain. You assess the result and decide whether to accept it. You can think through a question together with AI or delegate a result within agreed bounds.

The agent investigates the current situation, proposes or chooses methods, prepares and performs the work, checks actual results, and preserves decisions and evidence for continuation. It returns questions that need your knowledge or an undelegated decision while continuing independent authorized work.

iEWR calls joint thinking **S3** and delegated work **S4**. These describe participation, not a required sequence of stages.

## What you open

AGENTS.md is the entry point. The 7.0.6 application includes instructions, FPF, MethodPack, and resources for organizing engineering work: navigation, project directories, checks, and continuation materials. Your agent environment supplies file access, commands, computation, and other available tools.

| Part | Role |
|---|---|
| AGENTS.md and connected instructions | Connect the application, current task, working rules, and sources |
| FPF | General concepts, principles, and methods |
| MethodPack | Applied methods and accumulated specialization |
| Agent environment (ADE) | Execution tools, access, and technical boundaries |
| Project files | Inputs, decisions, results, checks, and continuation materials |

## How the work is organized

The architecture names seven connected functions:

| Function | Contribution |
|---|---|
| Context Formation — CF | Recover the current task, system state, decisions, and significant unknowns |
| System Formation — SF | Determine the contribution the system needs and its result criteria |
| Dynamic Method Generation — DMG | Find, reuse, adapt, or construct a suitable way of working |
| Execution Governance — EG | Connect an action to the assignment, authority, and execution conditions |
| Work Execution & Continuation — WEC | Perform the work, establish effects, and preserve continuation |
| Result Assurance & Feedback — RAF | Check fitness for use and return defects for correction |
| Human Interaction — HI | Obtain human contributions and deliver understandable results |

These functions are used according to the task. They are not seven mandatory stages or seven agents. Existing adequate decisions, methods, and results are reused. New information can change the next action.

## Methods for the task

For a new method choice, the agent checks for a sufficient FPF contribution, then the applied detail needed from MethodPack. DMG supplies what remains missing through adaptation or construction. Already established sufficient grounds are reused.

The supplied repertoire is a starting point. Within the assignment, the agent can obtain missing knowledge from professional sources, including the internet through available tools, adapt a suitable method, or construct and check what is missing. You do not need to commission each method separately. Useful contributions are retained in MethodPack for later tasks with their conditions and checking grounds.

The supplied MethodPack contains 37 candidate descriptions. Their purpose, conditions, and checking grounds determine their use. See the [method catalog](https://github.com/instantiatio/iEWR/blob/7.0.6/docs/METHOD_CATALOG.md) and [FPF, DMG, and MethodPack](/iEWR/eng/foundations/methods/).

## Context that continues with the project

The agent organizes working materials and maintains the basis for continuation as the project changes. You do not need to design a separate context-storage system. Inputs belong in `project/source/`, results and checking materials in `project/artifacts/`, and continuation materials in `project/handoff/`.

Useful records connect the current assignment, decisions, source editions, obtained results, checks, unfinished work, and next questions. In a new session, the agent recovers the relevant state from these files and checks what still applies. Ask “How can we continue this project?” and then discuss or assign the next contribution.

The project folder carries this basis between sessions. In the [GEO CRM case](/iEWR/eng/cases/geo-crm/), preserved context supported the observed Codex → DeepSeek Harness → Codex continuation and subsequent finance guides. The current instruction determines what to do next; a saved proposal does not become a new assignment on its own.

## Check and continue

The agent compares the actual result with the assigned use and criteria. A discovered problem can return the work to a requirement, assumption, method, implementation, or check. Passing tests is evidence about the properties those tests observe.

The actual configuration determines available tools and access. Instructions guide the agent; technical protection is supplied by the ADE and connected systems where needed. [STATUS 7.0.6](https://github.com/instantiatio/iEWR/blob/7.0.6/STATUS.md) records release verification, and [Cases & Experiments](/iEWR/eng/cases/) provides a checked application.

[Try iEWR](/iEWR/eng/try/) · [Architecture](https://github.com/instantiatio/iEWR/blob/7.0.6/ARCHITECTURE.json) · [Full ConOps](https://github.com/instantiatio/iEWR/blob/7.0.6/docs/IEWR_CONOPS.md) · [Русский](/iEWR/ru/how-iewr-works/)
