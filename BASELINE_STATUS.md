# iEWR 5.5.5 Beta — переносимый Recovery

25 сентября 2026. `candidate_for_review`, `distribution_ready=false`,
`public_release=false`, версия `5.5.5-beta`. Приёмка и публикация не выполнены.

## Exact baseline

Предоставленный опубликованный `iEWR-5.5.4-Beta.zip`, 135 files, SHA-256
`861ff8f3cd364feb8a7a813aa621e1605fb30d4574e134da6865151c02a8ec54`.
Сравнение ведётся только с ним. Baseline ZIP неизменён и не включён в продукт.
Поздние экспериментальные доработки development workspace не перенесены.

## Изменение и совместимость

Удалены три baseline-файла DSH companion. В новой поставке 132 файла с manifest.
Переносимые Recovery/C/bootstrap/reader/template сохранены побайтно; Core, owners
и bundled DPF не изменены. Уточнены instruction-led путь, необязательность schema-2
и helper, переиспользование direct selection, отсутствие технического guard.
DSH-only qualification runner и поздние runtime bridge files не входят в продукт.
Исторические evidence и прежняя development-конфигурация сохранены отдельно.

## Qualification и пределы

Локальные Python regression, package/configuration/import DAG, tail/ambiguity
audit и чистая распаковка проверяются на exact candidate. Протокол и delta
сопровождают ZIP вне продукта. Прежние Node consumer tests больше не имеют
поставляемого subject и не засчитываются как PASS новой версии.

Actual independent agent behavior / live host provenance / межhost перенос
истории — INCONCLUSIVE. Generic helper проверяет подготовленные records;
channel trust, owner interpretation и coverage остаются внешними основаниями.
Он не содержит producer, автоматической миграции, guard или actuation grant.
Python 3.10+ — interface floor helper, проверяемая локальная версия 3.13.14.
POSIX-only actuator на Windows не квалифицирован; fcntl shim не применяется.
Унаследованные внешние/неразрешимые локальные DPF links не чинятся в этом scope.
Встроенный DPF baseline остаётся `iEWR-dpf-5.5.3`. Source originals не изменены.
