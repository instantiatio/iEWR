# First experiment

A small assignment with known expected answers: check quotation expiry dates. First [open an iEWR project](/iEWR/eng/try/#download). This experiment needs Python 3 and uses its standard library. Python is not a general requirement for other iEWR tasks.

## Give the assignment

This checked experiment builds a quotation-expiry checker. It includes an exact final-day boundary and invalid dates, so you can assess more than whether a program starts.

It requires Python 3 and uses only the standard library. Python is not a general requirement for questions or other work in iEWR.

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


## Evidence

This experiment was performed with iEWR 7.0.6. Its result, repeated checks, exact conditions, and file package are in the [experiment case](/iEWR/eng/cases/quotation-expiry/). The original assignment is retained here so you can compare your run with the expected answers.

[Try iEWR](/iEWR/eng/try/) · [Русский](/iEWR/ru/try/first-experiment/)
