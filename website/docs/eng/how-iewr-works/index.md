# How iEWR works

**iEWR is an engineering environment in which AI independently organizes and performs work assigned by a person.** You specify the result, its purpose, and the bounds of independent action. The agent determines the necessary work, selects methods, executes the assignment, and checks the outcome.

It supports software development and change, engineering concepts and solutions, research, comparison of alternatives, and preparation of reasoned decisions. [Try iEWR](/iEWR/eng/try/) provides a first assignment and the setup route.

## Your contribution and the agent's work

You define intent, value, important constraints, and the decisions you retain. You assess the result and decide whether to accept it. You can think through a question together with AI or delegate a result within agreed bounds.

The agent investigates the current situation, proposes or chooses methods, prepares and performs the work, checks actual results, and preserves decisions and evidence for continuation. It returns questions that need your knowledge or an undelegated decision while continuing independent authorized work.

iEWR calls joint thinking **S3** and delegated work **S4**. These describe participation, not a required sequence of stages.

## What you open

The 7.0.6 distribution contains instructions, methodology, applied methods, navigation, and project directories. Your agent environment supplies files, commands, computation, and other available tools.

| Part | Role |
|---|---|
| Instructions | Connect the environment, current task, working rules, and sources |
| FPF | General concepts, principles, and methods |
| MethodPack | Applied methods and accumulated specialization |
| Agent environment (ADE) | Execution tools, access, and technical boundaries |
| Project files | Inputs, decisions, results, checks, and continuation materials |

The working combination is **Instructions + FPF + MethodPack**, used by AI through the available ADE. iEWR does not require a separate universal software engine.

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

The supplied MethodPack contains 37 candidate descriptions. Their purpose, conditions, and checking grounds determine their use. See the [method catalog](https://github.com/instantiatio/iEWR/blob/7.0.6/docs/METHOD_CATALOG.md) and [FPF, DMG, and MethodPack](/iEWR/eng/foundations/methods/).

## Check and continue

The agent compares the actual result with the assigned use and criteria. A discovered problem can return the work to a requirement, assumption, method, implementation, or check. Passing tests is evidence about the properties those tests observe.

Inputs belong in `project/source/`, results and checking materials in `project/artifacts/`, and continuation materials in `project/handoff/`. The saved state connects the current assignment, decisions, editions, completed work, effects, and next questions. It enables continuation after a break or handoff.

The actual configuration determines available tools and access. Instructions guide the agent; technical protection is supplied by the ADE and connected systems where needed. [STATUS 7.0.6](https://github.com/instantiatio/iEWR/blob/7.0.6/STATUS.md) records release verification, and [Cases & Experiments](/iEWR/eng/cases/) provides a checked application.

[Try iEWR](/iEWR/eng/try/) · [Architecture](https://github.com/instantiatio/iEWR/blob/7.0.6/ARCHITECTURE.json) · [Full ConOps](https://github.com/instantiatio/iEWR/blob/7.0.6/docs/IEWR_CONOPS.md) · [Русский](/iEWR/ru/how-iewr-works/)
