# GEO CRM: from an assignment to a working system

GEO CRM brings sales, stock, expense requests, and a 13-week liquidity forecast into one local application. It grew through a series of assignments, with engineering work continuing along the route **Codex → DeepSeek Harness → Codex**.

## From an assignment to a working CRM

### Assignment in brief

> Build a local CRM for a company selling surveying equipment. Use Bitrix24 as the reference for interaction, research its interface independently, and deliver a working demonstration.
>
> The brief specifies the stack, the scope of the first release, and the main rules for sales and stock.

### The agent's work

The agent independently organized the interface research, architecture, implementation, and checks. The person set the direction and made the necessary domain decisions.

### Result

A connected application with customers, deals, a sales kanban, stock reservations, and versioned quotations.

![GEO CRM sales pipeline with demonstration deals](/iEWR/assets/geo-crm/1.4.0-usd/01-sales-pipeline.jpg)

*The sales pipeline: deals by stage, amounts, and outstanding activities. An English interface, fictional companies, and USD demonstration data.*

## Codex → DeepSeek Harness → Codex

The same project folder was opened in DeepSeek Harness with an assignment to add expense requests. After clarifying approval rules and the module's scope, the agent implemented roles, statuses, scheduling, and manual payment recording.

Back in Codex, the next assignment was to model liquidity over 13 weeks and show the effect of delayed customer payments. The agent first developed LIQ-13 in MethodPack, then implemented the calculation, scenarios, interface, and checks.

The additions work together: a deal leads to a quotation, stock reservation, and shipment; a linked expense request enters the payment plan; the liquidity model compares expected receipts with planned payments. In this observed same-computer route, the project could be continued in both directions.

![A scheduled GEO CRM expense request and its history](/iEWR/assets/geo-crm/1.4.0-usd/07-request-detail.jpg)

*Request ER-0008 for USD 3,200: approval, payment scheduling, and the history of actions.*

## What a payment delay changes

The model calculates daily balances across 91 days and presents them by week. With the report's current synthetic inputs:

| Scenario | Minimum daily balance | First cash gap |
|---|---:|---|
| Base plan | USD 7,950 | None |
| All customer receipts delayed by 30 days | USD −8,850 | 20 November 2026 |

Daily detail matters: in the stress scenario, week 11 closes at USD +550 while its minimum daily balance is USD −1,650.

![GEO CRM liquidity forecast with customer receipts delayed by 30 days](/iEWR/assets/geo-crm/1.4.0-usd/08-liquidity-delay30.jpg)

*The scenario makes the cash gap visible and separately identifies receipts moved beyond the forecast horizon.*

## Using the context to explain the system

A further short assignment produced two finance guides: one structured around GOST 19.505-79, the other guided by ISO 26514 and Diátaxis. The agent used the working application and accumulated project context, ran a training scenario, and prepared Markdown and PDF guides with screenshots.

The project folder carried code, decisions, methods, the state of work, and recorded checks. These supported both further development and documentation of the system that had actually been built. The current demonstration uses an English interface, USD, and the consistent Graphite theme.

Finance guides, in English:

- [Operator guide using the GOST 19.505 structure (PDF)](/iEWR/assets/geo-crm/1.4.0-usd/manuals/FINANCE_GOST_EN.pdf).
- [User guide using ISO 26514 and Diátaxis (PDF)](/iEWR/assets/geo-crm/1.4.0-usd/manuals/FINANCE_ISO_DIATAXIS_EN.pdf).

## Checks and report

The new report records checks of **GEO CRM 1.4.0-demo**: **36 tests**, working scenarios, profile migration, demonstration-data installation, and a full restart preserving 19 tables. It independently matches **182 daily rows, 26 weekly aggregates, and 91 daily shifts after funding**. The case began in an **iEWR 7.0.0** project. The website's current iEWR release is 7.0.6; this case retains its actual project version.

The application is a local demonstration with synthetic data and manual payment recording. The report identifies the checked source and conditions, and records remaining issues in cross-module access, return-reason history, and self-approval policy.

[Report in English (PDF)](/iEWR/assets/geo-crm/1.4.0-usd/REPORT_EN.pdf) · [Отчёт на русском (PDF)](/iEWR/assets/geo-crm/1.4.0-usd/REPORT_RU.pdf)

Both reports contain the same facts and shared screenshots: the work, results, checks, source edition, and reproduction conditions.

[Cases & Experiments](/iEWR/eng/cases/) · [Try iEWR](/iEWR/eng/try/) · [Русский](/iEWR/ru/cases/geo-crm/)
