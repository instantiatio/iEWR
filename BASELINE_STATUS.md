# iEWR Closed Beta — статус чистой поставки

Package ID: `iEWR-5.0.0-beta`.
Version: `5.0.0-beta`.
Source baseline: `iEWR-closed-beta-2026-09-05` — принят Human как **Closed Beta**.
Статус: **Closed Beta, distribution_ready=false, not a public release**.
Это чистая упаковка принятого baseline; public release, blanket reliance,
новое semantic Admission или active-root cutover из неё не следуют.

Поставка содержит 84 согласованных компонента; 55 historical/developer файлов
исключены из ZIP и сохранены в разработке. Все 32 Python-файла, шесть framework/
repertoire файлов и governing Core Contract побайтно сохранены из исходного ZIP.
Изменены только packaging documentation/status/configuration и manifest hashes.
Общие API и exact Method contracts сохранены, включая используемые consumers B1.

Entry: [AGENTS.md](AGENTS.md); инструкции проверки: [README.md](README.md).
Core Contract сохраняет собственный статус 1.0 RC. C не workflow engine;
E не инициирует Work/action; G не создаёт authority.

## Фактическая проверка и её границы

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

## Сохранённые пределы

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
