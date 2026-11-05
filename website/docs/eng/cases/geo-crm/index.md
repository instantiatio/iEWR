# GEO CRM: from an assignment to a working system

GEO CRM brings sales, stock, expense requests, and a 13-week liquidity forecast into one local application. It grew through a series of assignments, with engineering work continuing along the route **Codex → DeepSeek Harness → Codex**.

## From an assignment to a working CRM

Build a local CRM for a company selling surveying equipment. Use Bitrix24 as the reference for interaction, research its interface independently, and deliver a working demonstration.

The brief set the stack, the scope of the first release, and the main rules for sales and stock. The agent organized the interface research, architecture, implementation, and checks independently.

The result included customers, deals, a sales kanban, stock reservations, and versioned quotations. The person set the direction and made the necessary domain decisions; AI turned those requirements into a connected application.

![GEO CRM sales pipeline with demonstration deals](/iEWR/assets/geo-crm/01-sales-pipeline.jpg)

*The sales manager's view: deals by stage, amounts, and outstanding activities. The English interface uses fictional companies and GBP demonstration data.*

## Codex → DeepSeek Harness → Codex

The same project folder was opened in DeepSeek Harness with an assignment to add expense requests. After clarifying approval rules and the module's scope, the agent implemented roles, statuses, scheduling, and manual payment recording.

Back in Codex, the next assignment was to model liquidity over 13 weeks and show the effect of delayed customer payments. The agent first developed LIQ-13 in MethodPack, then implemented the calculation, scenarios, interface, and checks.

The additions work together: a deal leads to a quotation, stock reservation, and shipment; a linked expense request enters the payment plan; the liquidity model compares expected receipts with planned payments. In this observed same-computer route, the project could be continued in both directions.

![An approved GEO CRM expense request linked to the sales case](/iEWR/assets/geo-crm/06-case-expense.jpg)

*The finance director's view: a GBP 1,250 request scheduled after approval. Its history records the people and workflow transitions.*

## What a payment delay changes

The model calculates daily balances across 91 days and presents them by week. With the report's synthetic inputs:

| Scenario | Minimum daily balance | First cash gap |
|---|---:|---|
| Base plan | GBP 8,850 | None |
| All customer receipts delayed by 30 days | GBP −10,100 | 13 November 2026 |

Daily detail matters: a week can end with a positive balance while containing several days below zero.

![GEO CRM liquidity forecast with customer receipts delayed by 30 days](/iEWR/assets/geo-crm/09-liquidity-delay30.jpg)

*The scenario makes the cash gap visible and separately identifies receipts moved beyond the forecast horizon.*

## Using the context to explain the system

A further short assignment produced two finance guides: one structured around GOST 19.505-79, the other guided by ISO 26514 and Diátaxis. The agent used the working application and accumulated project context, ran a training scenario, and prepared Markdown and PDF guides with screenshots.

The project folder carried code, decisions, methods, the state of work, and recorded checks. These supported both further development and documentation of the system that had actually been built. The same application was later translated into English and given a consistent Graphite interface.

## Checks and report

The report checks **GEO CRM 1.3.1-demo**, developed in the **iEWR 7.0.0** project. Its new run passed **36 tests**, completed a role-separated scenario from customer and shipment through an expense request to the forecast, and independently matched **182 daily rows and 26 weekly aggregates**. The website's current iEWR release is 7.0.6; this case retains its actual project version.

The application is a local demonstration with synthetic data and manual payment recording. The report identifies the checked source and conditions, and records remaining issues in cross-module access, return-reason history, and self-approval policy.

[Read the illustrated report (PDF, English)](/iEWR/assets/geo-crm/REPORT_EN.pdf). It includes the work, screenshots, checks, source identity, and reproduction conditions.

[Cases & Experiments](/iEWR/eng/cases/) · [Try iEWR](/iEWR/eng/try/) · [Русский](/iEWR/ru/cases/geo-crm/)
