# GEO CRM: sales, stock, and liquidity

GEO CRM is a local demonstration system for a B2B supplier of surveying equipment. It connects customers, deals, versioned quotations, products and a single warehouse, activities, expense requests, and a 13-week liquidity model.

AI selected a Python/PostgreSQL architecture, implemented the data model, interface and business rules, and organized checks. The person supplied the intended result, functional boundaries, and delegation. The resulting product connects sales activity to stock movement and planned cash flows.

## The connected product

A quotation preserves the agreed commercial terms as a versioned snapshot. A deal can reserve stock and proceed to shipment. An expense request can refer to that deal and enter the payment calendar. LIQ-13 reads the requests as planned outflows and compares expected customer receipts with payments.

Development records document continuation of the same project along the Codex → DeepSeek Harness → Codex route. Expense requests were added in DeepSeek Harness; LIQ-13 was implemented in Codex using those requests. The current integration checks establish that these contributions work together in the recorded product.

The screenshots show the current Russian-language interface and synthetic data.

![GEO CRM sales pipeline with demonstration deals](/iEWR/assets/geo-crm/01-kanban.jpg)

*The sales pipeline groups demonstration deals by stage and shows their amounts and outstanding activities. Screenshot view: administrator.*

## A checked business scenario

The report's new HTTP scenario connected:

**Customer → RUB 125,000 deal → quotation → stock reservation → shipment → RUB 25,000 expense request → liquidity forecast.**

The quotation snapshot remained unchanged after shipment. The expense request entered the payment calendar and appeared once in the model's planned outflows. Financial scenarios and saved calculations were also inspected in the browser.

The report reran **33 tests** on a separate database. The suite covers the recorded cases for money calculations, reservation, concurrent requests, repeated operations, permissions, quotations, expense transitions, and liquidity. The HTTP scenario used the relevant operating roles; the illustrative screenshots use the administrator view.

## LIQ-13: the effect of delayed receipts

The model uses an explicit 91-day horizon, opening cash, expected receipts, and planned payments. It calculates daily balances and also presents them by week. Payments are recorded manually; this demonstration has no bank connection.

With the report's synthetic data:

| Scenario | Minimum daily balance | First cash gap |
|---|---:|---|
| Base plan | RUB 770,000 | None |
| All customer receipts delayed by 30 days | RUB −910,000 | 23 November 2026 |

An independent arithmetic loop checked all **182 daily rows** across the two scenarios. The supplied data and script reproduce this check.

![GEO CRM liquidity model with a 30-day delay](/iEWR/assets/geo-crm/07-liquidity-delay30.jpg)

*The scenario exposes a cash gap and separates receipts shifted beyond the horizon. The displayed minimum is calculated from daily balances.*

## Version, evidence, and open items

The report checked **GEO CRM 1.2.3-demo** on 5 November 2026 using **iEWR 7.0.0**, build release-r1, with MethodPack geo-liquidity-v1. The source snapshot is identified by hashes of 27 files rather than a Git commit. The exact environment build at the start of the original development run was not preserved.

The report retains earlier findings about exposure of another deal's title through an expense link, return-comment validation and persistence, and the policy for self-approval and separation of duties. Those findings were not re-probed or closed during report preparation.

The [full Russian report](/iEWR/assets/geo-crm/REPORT_RU.pdf) includes 12 screenshots, source identity, reproduction conditions, and the distinction between new checks and historical evidence. The [selected evidence package](/iEWR/assets/geo-crm-evidence.zip) contains the report, two original images, recorded test results, and the data and script for repeating the arithmetic check. It is an evidence package rather than an application-source distribution.

[Cases & Experiments](/iEWR/eng/cases/) · [Try iEWR](/iEWR/eng/try/) · [Русский](/iEWR/ru/cases/geo-crm/)
