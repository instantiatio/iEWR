# Cases & Experiments

The task, the work performed, the result, and its checks make an experiment useful to others. The materials below connect assignments to results, checks, and conditions.

## GEO CRM: an integrated demonstration system

Customers, deals, quotations, stock, expense requests, and LIQ-13 work in one local application. GEO CRM 1.2.3-demo was checked with iEWR 7.0.0: 33 tests, a connected business scenario, and arithmetic verification of 182 daily rows.

[Read the GEO CRM case and view the screenshots](/iEWR/eng/cases/geo-crm/).

## From a business rule to a checked tool

**Task:** build a command-line tool that checks whether sales quotations have expired. A quotation remains valid on its final day. Missing or impossible dates must be marked invalid without losing rows or stopping the rest of the file.

The person supplied the goal, CSV data, acceptance conditions, and execution bounds. In a newly extracted iEWR 7.0.6 workspace, a fresh agent session independently selected its approach, implemented the tool, wrote tests, ran the solution, and prepared a README. No content corrections or implementation instructions were supplied during the run.

### Result

The agent delivered a Python standard-library program, five executable tests, a processed CSV, and run instructions. It preserved the input and all 42 released iEWR files.

For the explicit checking date **2026-11-05**, the output was:

| id | valid_until | status |
|---|---|---|
| Q1 | 2026-11-04 | expired |
| Q2 | 2026-11-05 | valid |
| Q3 | 2026-11-06 | valid |
| Q4 | 2026-02-30 | invalid |
| Q5 | empty | invalid |
| Q6 | not-a-date | invalid |

### Checks

The expected outcomes were fixed before execution. A separate verification reran the documented command and all five tests, compared every row with those expectations, and checked input and distribution-file preservation.

Changing the checking date to 2026-11-06 changed Q2 to expired while Q3 remained valid. The output checker was also challenged with three incorrect results: excluding the final day, dropping invalid rows, and marking every row valid. It rejected all three.

### Reproduce or inspect

To have AI create the solution, follow [Try iEWR](/iEWR/eng/try/) with a new copy of the environment and the supplied assignment.

To inspect the delivered solution, [download the evidence package](/iEWR/assets/quotation-expiry.zip) and extract it into a separate folder. From that folder, run:

```sh
python3 project/artifacts/first-experiment/check_quotes.py project/source/first-experiment/quotes.csv project/artifacts/first-experiment/output.csv --as-of 2026-11-05
python3 -m unittest discover -s project/artifacts/first-experiment -v
```

The package contains the program, tests, input, expected output, and recorded checks. This runs the produced tool; regenerating it through an agent is the Try iEWR experiment.

### Recorded conditions

The generation run used iEWR 7.0.6, Codex CLI 0.166.0-alpha.6, macOS 27.0.1 arm64, and Python 3.14.6. The English assignment was executed; the Russian assignment is a corresponding localization. The exact backend model snapshot was not recorded. The agent used an existing signed-in account on the same host as the verification.

The program processes UTF-8 CSV in memory and writes its output directly. Large-file behavior, concurrent writers, and interrupted output writes were outside this experiment. The tool's README records its input-format conditions.

The result shows a complete small assignment: choose a method, implement a business rule, handle boundary and invalid-data cases, execute checks, and deliver reusable files.

[Try iEWR](/iEWR/eng/try/) · [How iEWR works](/iEWR/eng/how-iewr-works/) · [Русский](/iEWR/ru/cases/)
