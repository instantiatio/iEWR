# AGENTS.md — Instantiatio EWR

Статус: iEWR 5.2.2 Beta; комплект подготовлен к рассмотрению для публикации.
Принятая основа — 5.2.2-beta.3-docs.2; точный ZIP и границы испытаний
указаны в BASELINE_STATUS.md. Оставлены единый указатель и прямое обращение к DPF.
Проверки ограничены переносимыми проверками и локальными агентными испытаниями;
distribution_ready=false. Приёмка не расширяет полномочия и технические возможности.
Direct Human decisions и policy сохраняют свои scope; этот dispatcher их не создаёт.

Только explicit поручение изменить **сам iEWR** подключает
[поддержку саморазвития](modules/self_development/GUIDANCE.md).
Обычные задачи, упоминание iEWR и project DPF registration её не включают.
Это bounded instruction support существующих owners, не новый runtime owner.

Обычное общение, первое приветствие и понятная подача хода/предмета работы —
по [I interaction](modules/interaction/HUMAN_INTERACTION.md). Применяй её
соразмерно текущему вопросу; это не включает поддержку саморазвития.

Перед meaningful continuation восстанови три accounts по
[R](modules/recovery/CONTRACT.md): governance, relied execution basis, factual
execution/effects. Source/frozen/package/candidate evidence не user-project
history. 0 инициатив — normal new question, 1 — exact direct basis, несколько —
Human selection. STATE_INDEX optional/stale ignored. Unknown effects no replay.

Current question / exact subject / receiving use → adequate reuse либо bounded
Direct Work; нужная formation — только если missing result меняет решение.
WorkPlan только для current intended coordination, не от complexity. Достаточный
результат оценивается по всему текущему поручению: завершение части не повод
ждать «продолжай», если остаётся необходимое разрешённое действие. Выполнить его
в действующем scope через existing owners. Stop на результате поручения и
reconciled effects либо honest affected blocker; независимое разрешённое
продолжать. Завершение не создаёт successor/review/Admission; новый запрос — через C.
Содержательную выдачу структурировать заголовками. Явно обозначать нужное участие
Human либо завершение без обязательного следующего действия. Существенный выбор —
«Требуется решение», реальные нумерованные варианты, рекомендация и последствия;
в длинной выдаче непосредственно перед ним — «Кратко». Детали и связь ответа — I/G.
Перед отправкой сверить фактическую подачу по I: в Markdown-канале смысловые
заголовки оформлены как `## ...`, в том числе один заголовок короткого результата.
Если в Markdown-чате даёшь ссылку на локальный файл, проверь абсолютный путь:
для Windows `C:/...`, без `/` перед буквой диска; пробелы — внутри `<...>`.
Относительные ссылки допустимы внутри сохраняемого документа, не в ответе чата.

При новой содержательной задаче самостоятельно найди подходящие DPF и прочитай
нужные разделы до существенной постановки, критериев или рекомендации, в том
числе в промежуточном сообщении. Название и оглавление не заменяют метод. Подходящие методы
с нужным вкладом применяй; собственное рассуждение не оправдывает их пропуск.
Достаточную основу переиспользуй, механическая правка не требует нового поиска.
Точное правило — [F](modules/formation/DOMAIN_WORK.md), доступ и чтение —
[S](modules/sources/GUIDANCE.md), быстрый вход — [единый указатель](catalog/dpf/METHODS.md).

Current owners и instructions:

| Owner | Governing application locus |
|---|---|
| S semantic/domain sources | [S guidance](modules/sources/GUIDANCE.md), [registration](modules/sources/REGISTRATION.md) |
| F formation/Method/intended basis | [F domain work](modules/formation/DOMAIN_WORK.md) |
| G direct governance grounds | [G guidance](modules/governance/GUIDANCE.md) |
| X execution/steering/profiles | [execution basis](modules/execution/EXECUTION_BASIS.md) |
| E effects/technical boundary | [E guidance](modules/effects/GUIDANCE.md) |
| L evidence/Verification/reliance | [receiving use](modules/reliance/RECEIVING_USE.md) |
| R recovery | [R contract](modules/recovery/CONTRACT.md) |
| C coordination | [C guidance](modules/coordination/GUIDANCE.md) |
| I Human Interaction | [I interaction](modules/interaction/HUMAN_INTERACTION.md) |
| P platform | [adapters](adapters/ADAPTERS.md) |

C не workflow engine; E не инициирует Work/action; G не создаёт authority.
I не вызывает X/E напрямую. R/L только query/assessment, не actuation. Owner
records single-writer, нет общего RuntimeState/authority registry. Allowed DAG
и bootstrap boundary заданы C guidance; FPF/DPF/LPF не runtime routes.

FPF — semantic authority; [Core Contract 1.0 RC](docs/EWR_CORE_ARCHITECTURE_CONTRACT.md)
сохраняет governing status. DPF/LPF bounded external sources; directory order не
precedence. Для ordinary work не требовать, скачивать, копировать или полностью
читать FPF-Spec, в том числе частями/делегированием. Primary source development/
audit требует separate explicit question/source/effect scope; full text отдельно.
См. S guidance; policy declared, не host control.

При formal Work claim строго `A.13 → independent full A.15.1 → conditional F.6`.
Admitted actual performer/assignment, grounded performance/enactsMethod/temporal
extent/obtaining containing-System relation независимы; missing F.6 удерживает
только precise attribution. План, file, run status и tool success не Work.

Перед material effect: current direct permission/authority, capability,
allowed/prohibited scope, technical `declared/enforced/compensated/unsupported`
basis, recovery/check/stop. Beyond explicit authorization zero-by-default.
Несколько действий под уже данным scope не требуют повторных microapprovals;
changed material basis/scope/unknown effect возвращаются только affected owner.

Русский task → русская обычная подача с exact terms/IDs где нужны для выбора.
Preferences только presentation; сохранять material conditions/effects/gaps.
Legacy guides/catalogs/scenarios/CONTRACT B1 читаются для bounded historical
meaning, не universal lifecycle. Candidate label не type/status ladder.

`project/source/**`, `project/iEWR-reference/**`, `project/reference/**`,
`frameworks/**` frozen/read-only без отдельного exact Human scope. Не создавать
project/sources. User results — project/artifacts, interaction — project/handoff;
нужные durable accounts — project/artifacts/process. Сначала existing authoritative
locus; обычный документ можно править на месте. Preserve user edits/provenance/UTF-8.
До использования редакции как основания/поставки обеспечить её сохранность и
доступность; исправление зафиксированного результата — новая редакция. Оригиналы,
зафиксированные результаты и необходимые основания — без автоматического срока
удаления. Достаточность метаданных обосновать по use и переиспользовать.
Project repertoire — project/dpf/REPERTOIRE.yaml; source inspect in-place,
без source copy/execution/network. User locus — source/external-dpf/.
Общие правила файлов, совместных правок и решений — [project/README](project/README.md).

Exact selected package inventory: [manifest](PACKAGE_MANIFEST.md).
Поставляемый JSON entry — app/bootstrap/operation.py; он требует independently
established direct grounds и current host controls. Его observed qualification
ограничена synthetic local subprocess evidence; fixture trust не переносится
на live host. Tests/fixture entry и historical tools находятся вне продукта,
в development. Historical direct decisions не становятся blanket grants.
