# iEWR 5.0.1-beta — принятый Bundled DPF Baseline

Package ID: `iEWR-5.0.1-beta`.
Version: `5.0.1-beta`.
Source baseline: `iEWR-closed-beta-2026-09-05` — исходная принятая Closed Beta.
Bundled DPF Baseline: `iEWR-bundled-dpf-2026-09-06` — принят Human для локальной
Closed Beta `iEWR-5.0.1-beta` по exact proposal и resulting integration review.
Статус: **Closed Beta, distribution_ready=false, not a public release**.
Прямое Human решение от 2026-09-06 сохраняет заявленные ограничения и разрешает
final checks, локальную упаковку, evidence и затем Guide. Public release,
blanket reliance, новое semantic Admission или active-root cutover не следуют
из принятия source baseline. Decision/evidence carriers сохраняются отдельно
в development: `project/artifacts/process/dpf-baseline-refresh/ACCEPTANCE.md`.

## Текущая product-доработка: maintainer guide и external source locus

По следующему прямому Human запросу стабильный
[Bundled DPF Baseline Refresh and Integration Guide](docs/BUNDLED_DPF_BASELINE_REFRESH_AND_INTEGRATION_GUIDE.md)
включён в продукт. `source/external-dpf/` поставляется с пустым `.gitkeep` как
место пользовательских исходников. README и registration instructions
разделяют direct use, project registration и bundled baseline maintenance.
Регистрация сама по себе не требует отдельного MethodDescription; действующий
JSON consumer сохраняет свой обязательный Method binding и host requirements.

Текущий состав: **87 компонентов**, включая self-unhashed PACKAGE_MANIFEST;
86 inventory rows и 85 configuration rows. Новых DPF нет: пять upstream DPF,
отдельный experimental local SDLC и exact repertoire сохраняют прежние bytes.
Core Contract и функциональные runtime modules не менялись.

Human отдельно разрешил узкую правку P `repertoire_engine.py`: project source
может читаться из `source/external-dpf/` или прежнего `project/dpf/`, запись
repertoire остаётся только в `project/dpf/REPERTOIRE.yaml`. Path/no-follow/locking
controls, metadata schema, Method transport и owner contracts сохранены.
Maintainer package checker учитывает новый `source` tree; пользовательские
загрузки не включаются в product inventory автоматически.

Текущая проверка ограничена package/configuration/inventory, сохранностью
accepted sources/Core/owner code, допустимыми и запрещёнными source paths,
project-entry validation и packaged links. Полный DPF integration/probe cycle
не повторяется: принятые DPF semantics не меняются. Actual POSIX package helper
и source registration на Windows остаются unsupported, их tests явно skipped;
новая live-host qualification не заявляется. Exact logs и новый ZIP checksum
сохраняются отдельным package evidence, прежний ZIP не перезаписывается.

Проверка локальных inline Markdown paths прежней упаковки обнаружила 25
неразрешаемых occurrences в frozen OCE/PSD/SDLC. Их bytes сохранены; introduced
product links проверяются отдельно, без переноса этих исторических ограничений
на новые документы. Remote links и полный frozen-source anchor audit не выполнялись.
SDLC overlap audit не начат, `distribution_ready=false` сохраняется.

## Принятый DPF refresh — evidence до product-доработки

SYSE, ME, OCE и PSD обновлены до объявленной редакции `2026-09-05`; OPS той же
редакции добавлен как пятый upstream Engineering DPF. Exact upstream snapshot:
`43c46859c3926a371fa60cfb1c76aefa19f9eaf9`; все пять Git blob IDs проверены по
локальному SOURCE_MANIFEST, bundled bytes совпадают с `project/source/dpf/`.
Даты в development SOURCE_MANIFEST исправлены по заголовкам исходников,
добавлены raw SHA-256. Сами исходные документы сохранены без изменений.

Состав при принятии DPF refresh: **85 компонентов**, включая self-unhashed PACKAGE_MANIFEST;
84 inventory rows и 83 configuration rows. Шесть repertoire entries — пять
upstream DPF и отдельный неизменённый experimental local SDLC `0.1.0`.
В этом refresh Governing Core Contract и все runtime Python в modules/adapters/app сохранены
побайтно. Единственное изменение Python — список package slots и его сообщение
в maintainer-only `tools/package/integrity.py`; это не runtime routing.

OPS использует обычный `S → applicable source contribution → F`. OPS.6 даёт
bounded Method contribution для continuing case; permission, performance,
effects и progression требуют собственных оснований. В C нет нового workflow,
в G — grant, в E — инициирования, в R — repair. Новый DPF не вводит обязательный
Admission lifecycle или namespace branch. SDLC overlap audit не выполнялся.

Development tests находятся в
`project/artifacts/process/dpf-baseline-refresh/tests/`, вне product inventory.
Они проверяют raw bytes/metadata, exact inventory/import DAG, неизменность Core
и runtime, synthetic OPS.6 continuation, отдельное permission, unknown-effect
hold, reuse/stop и независимость от source_id: 6 PASS, 1 explicit SKIP.
Configuration/import DAG проверен отдельно. Windows/Python 3.13.14 позволяет
portable checks; actual POSIX filesystem reader/package helper здесь unsupported
и его integration test явно skipped. Controls не ослаблялись.

Семь fresh-context agent probes использовали одинаковый продукт и controlled
local inputs. Пять подтвердили самостоятельный выбор, чтение реальных DPF
bodies и предметное применение: OPS continuing work, SYSE combined configuration,
ME documentary recovery/content-form, OCE operating arrangement и PSD decision
support. Два Direct Work controls использовали уже достаточный supplied Method
без DPF и не засчитаны в DPF integration passes. В двух отдельных продолжениях
r4 → r5 старый result не перенесён на новый use; unknown effect не повторён.
Это семь случаев плюс два follow-up, не девять независимых тестов.

OPS probe реально выполнил локальный PowerShell расчёт, сохранил результат и
остановился на достаточном результате либо affected missing input. Это
instruction-led execution, разрешённое текущими adapters instructions; JSON
entry в agent probes не запускался. Источники, исходные задачи, actual commands,
outputs, parent review и before/after hashes сохранены вне продукта. Affected
integration points SYSE/ME/OCE/PSD проверены в указанном scope. В первой упаковке
после принятия runtime и source bytes сохранились из проверенного agent-probe
продукта; изменились только четыре status/version/documentation/hash carriers.
Последующая product-доработка и её отдельные проверки описаны выше.

Evidence ограничено этими controlled local cases и cooperative boundaries.
Formal U.Work, live POSIX JSON end-to-end, полная host qualification, OPS/domain
conformance и гарантированное чтение DPF на любой задаче не установлены.
Исторические suites ниже в clean ZIP отсутствуют и в этой инициативе повторно
не запускались. Финальные checks и exact ZIP verification имеют отдельные logs;
development evidence и исходный narrative Guide не включались в тот inventory.
Его стабильная maintainer-редакция теперь поставляется в docs.

Пять текущих upstream editions имеют unresolved public redistribution basis;
исторические statements не перенесены на них как разрешение распространения.
`distribution_ready=false` сохранён. Full source-navigation audit новых editions
не выполнялся; внешние/относительные ссылки сохраняются как upstream bytes.

Основание сравнения: локальный `project/reference/iEWR-5.0.0-beta.zip`, SHA-256
`45da492fd342dab6764a3b4a65229618ac806c0d7342d02e77f541430f19ea67`.
До изменений все 84 файла workspace совпадали с этим ZIP. Historical editions
сохраняются в нём; смена repertoire не переписывает прежние relied bindings.

## Принятая чистая упаковка 5.0.0-beta — историческая basis

Исходная поставка содержит 84 согласованных компонента; 55 historical/developer файлов
исключены из ZIP и сохранены в разработке. Все 32 Python-файла, шесть framework/
repertoire файлов и governing Core Contract побайтно сохранены из исходного ZIP.
Изменены только packaging documentation/status/configuration и manifest hashes.
Общие API и exact Method contracts сохранены, включая используемые consumers B1.

Entry: [AGENTS.md](AGENTS.md); инструкции проверки: [README.md](README.md).
Core Contract сохраняет собственный статус 1.0 RC. C не workflow engine;
E не инициирует Work/action; G не создаёт authority.

## Историческая фактическая проверка и её границы

Чистый состав проверен без developer additions на macOS 26.6.2 ARM64 / Python
3.14.6: configuration/DAG — 82 rows, package manifest — 83 rows, пять exact DPF
bindings, 9 synthetic behavioral probes — PASS. Отдельно выполнены неизменённые
регрессии: 158 PASS + 1 SKIP / 159; original suite — 77 PASS + 1 SKIP / 78.
Это пересекающиеся evidence sets, а не 237 независимых продуктовых тестов.
SKIP: файловая система fixture не представляет distinct case-colliding files.

Эти behavioral results относятся к проверенной чистой подготовке. При финальной
упаковке изменены только шесть documentation/metadata файлов; runtime bytes
сохранены. Metadata/hash и проверка распакованного ZIP имеют отдельные developer
records. Tests/evidence не входят в продукт; проверки не доказывают live Human
authentication, полное U.Work основание или универсальную semantic conformance.

## Пределы исходной поставки — историческая запись

Ниже сохранены ограничения исходного baseline. Новые bounded Windows
instruction-led observations описаны выше; они не закрывают полный host matrix.

- Fresh-agent, live host/services/direct-channel authentication и general
  language/role qualification не установлены для произвольных configurations.
- Native PowerShell, полный Python/platform matrix и hostile-writer/ABA
  enforcement не проверены; cooperative-local boundary не host-wide isolation.
- HSI Method G-03 и live unattended/full E.16 остаются открыты.
- B5 — bounded synthetic local trials; не field validation/full domain
  conformance. SDLC 0.1.0 остаётся experimental local-trial source.
- E-06: четыре source distribution confirmations pending; SDLC basis
  project-authored local-trial only. LICENSE продукта не перелицензирует sources.
- OCE/PSD уже содержат шесть неразрешаемых относительных source addresses;
  SDLC содержит абсолютные provenance links. Их исходные bytes сохранены;
  полная переносимость source navigation не заявлена. История и exact old
  authority decisions не становятся runtime dependencies или blanket grants.
- Unknown external consumers не объявлены migrated. Исключение из payload
  сохраняет исходные historical records и их ограниченные meanings.

Source ZIP SHA-256: `b0946f59a6fe8144a01c40cbbfc298842af3d8f8a89e7f8c8e5ebc01547877b0`.
Source PACKAGE_MANIFEST SHA-256: `2b4d805a6e4a1cf180b516899b0b4c5c0203d42e2e4cd5116bad0b2f80a6821a`.
Текущий exact manifest находится рядом. Его SHA-256 и ZIP checksum хранятся
внешними records, чтобы не создавать self-hash cycle внутри продукта.
