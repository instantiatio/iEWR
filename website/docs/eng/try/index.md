# Try iEWR

Give AI a small engineering assignment and inspect a working result. You set the goal and acceptance conditions; AI chooses how to organize and perform the work.

iEWR 7.0.6 Eternal Alpha is a research environment: instructions, methods, and project files used by an AI agent. Start your agent in the extracted folder. You can try it without reading Foundations.

## Requirements

- An installed, signed-in agent environment that can read and write local files and run commands. Codex CLI is the concrete route used for this check; a basic chat without file and execution access is insufficient.
- Access to the agent's model service, according to its account and network requirements. Model usage follows that service's terms and limits.
- Python 3 for this particular experiment. The tool uses the standard library; no additional packages or application server are required. Python is not a general requirement for using iEWR.

## Download

[Download iEWR 7.0.6 ZIP](https://github.com/instantiatio/iEWR/releases/download/7.0.6/iEWR-7.0.6-Eternal-Alpha.zip) · [Release and checksum](https://github.com/instantiatio/iEWR/releases/tag/7.0.6)

Extract it into a new folder. Open **iEWR-7.0.6-Eternal Alpha**, the folder containing `AGENTS.md`, `START.txt`, `methods/`, and `project/`.

## Start

Start a new agent conversation with that folder as its workspace. In an already configured Codex CLI, the corresponding interactive command is:

```sh
codex --cd "/path/to/iEWR-7.0.6-Eternal Alpha"
```

Replace the path with the extracted folder's actual location. Keep quotes around a path containing spaces. Allow the local file operations and Python commands needed by this exercise. No publication or external-system access is needed.

## Give the assignment

This experiment builds a quotation-expiry checker. It includes an exact final-day boundary and invalid dates, so you can assess more than whether a program starts.

Copy the following assignment into the new conversation:

```text
Read AGENTS.md and use it as working instructions for my current task.

Build and check a small command-line tool for checking whether sales quotations have expired. Work independently within this folder: choose a suitable method, implement the tool, run it, and test it. Use Python 3 and its standard library only; no package installation or network access is needed.

The user supplies an explicit --as-of date in YYYY-MM-DD format. A quotation is valid through its final day, expired after that day, and invalid if valid_until is missing or is not a real YYYY-MM-DD calendar date. One invalid row must not stop processing the others. Preserve every row and its id in the output CSV, adding a status column with valid, expired, or invalid.

Create project/source/first-experiment/quotes.csv from this synthetic data, then leave that input unchanged:
id,valid_until
Q1,2026-11-04
Q2,2026-11-05
Q3,2026-11-06
Q4,2026-02-30
Q5,
Q6,not-a-date

Save the tool, tests, output for --as-of 2026-11-05, and a short README under project/artifacts/first-experiment/. Leave the released environment files unchanged. In your final response give one command to run the tool from the environment root, what you actually checked, and any remaining limits. This is a local experiment; do not publish anything.
```

## Check the result

Open `project/artifacts/first-experiment/`. Follow the agent's README and rerun its command and tests. The output for the fixed date **2026-11-05** must contain all six rows:

| id | Expected status |
|---|---|
| Q1 | expired |
| Q2 | valid |
| Q3 | valid |
| Q4 | invalid |
| Q5 | invalid |
| Q6 | invalid |

Q2 checks that the final day is included. Q4–Q6 must remain visible as invalid; they must not disappear or prevent valid rows from being processed. Compare the original CSV with the six rows in your assignment. The agent should report actual checks and remaining limits. A polished explanation or passing self-written tests alone is insufficient.

If the agent only proposes a plan, ask it to carry out and check the assigned solution. If execution is blocked, identify the missing command, access, or runtime before continuing. The outcome is a small local demonstration; assess suitability separately before using it with real business data.

## Continue with your own task

Describe the result you need, why it matters, constraints, and what AI may do independently. Provide materials in `project/source/`. Ask the agent to carry out the work, check the result, and report anything unresolved.

For background, explore [Foundations](/iEWR/eng/foundations/). See [How iEWR works](/iEWR/eng/how-iewr-works/) and the [case and evidence](/iEWR/eng/cases/). For current implementation and limitations, see the [README](https://github.com/instantiatio/iEWR/blob/7.0.6/README.md) and [release status](https://github.com/instantiatio/iEWR/blob/7.0.6/STATUS.md).

## Verification scope

One English-language automated Codex CLI run completed this assignment in a newly extracted 7.0.6 folder on macOS, using Python 3.14.6. The output and tests were rerun separately; all six expected rows matched. Account setup, manual interactive startup, other agent environments and operating systems, and a separate Russian-language run were not tested.

[Home](/iEWR/eng/) · [Русский](/iEWR/ru/try/)
