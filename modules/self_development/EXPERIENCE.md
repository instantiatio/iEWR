# Опыт для следующей доработки iEWR

Это scoped reuse, не grants и не универсальные правила. Exact текущая поставка
и пределы проверки — [BASELINE_STATUS](../../BASELINE_STATUS.md).

| Когда полезно | Наблюдение → применённое улучшение | Основание и предел |
|---|---|---|
| Handoff содержит несколько одинаково названных ZIP | В 5.0.1 были 85-file промежуточные и 87-file published packages → выбирать по digest/inventory, evidence связывать с конкретной конфигурацией | Handoff 5.0.1 от 2026-09-07; совпадение имени не identity |
| Авторская дата DPF не меняется | В snapshot d514a6fc каждый из пяти DPF получил только license line → сохранять авторскую дату и отдельный revision binding; проверять raw delta до обещания новых semantics | Фактическое сравнение пяти файлов с 5.0.1; не обобщать на будущие editions |
| Нужна работа без development history | Старый clean package не содержал сборщика, historical scripts зависели от прежнего scope → portable manifest-only helper поставляется вместе с bounded инструкцией | Потребность обнаружена при разработке 5.1; integrity не behavioral evidence |
| Доработка начинает обрастать документацией | Достаточны текущая задача/criteria и один recoverable process locus; DPF refresh guide переиспользуется специализированно | Design 5.1 по R1–R9; не доказанный минимум для любой архитектурной миграции |
| Проверка упала после metadata edit | В 5.0.1 uppercase hash parser дал failed attempt → сохранить failure и отдельный passing rerun, обновлять hashes после обоснованного delta | Historical finalization observations; новое изменение требует своей проверки |
| Metadata выглядят согласованными | В 5.0.1 inventory hash Core был верным, а отдельное architecture_sha256 устарело → проверять load-bearing duplicate field против actual source; исправление metadata не объявлять изменением Core | Обнаружено и исправлено при self-use 5.1; негативная проверка проходит даже после обновления manifest |
| Новые hashes могут скрыть прежнюю identity | В helper 5.1 сравнение repertoire с baseline отвергает same source/edition с иным digest; новая explicit revision проходит | Portable negative test; predicate не выбирает новую relied basis автоматически |
| Проверяется переносимость поддержки | Fresh-context агент по чистой 96-file candidate нашёл guidance, доработал TextRenderer и собрал проверенный ZIP; ordinary calculation, user-app edit и project registration обошлись без self-development | Четыре bounded cases 5.1 на одном Windows host; не общий model/host PASS и не самостоятельное DPF discovery |
| Проверка ZIP использует глубокий Windows-каталог | Adapter trial упал при частичной распаковке из-за длины пути → сохранить список уже созданных файлов и перейти к новому короткому extraction root, затем проверить exact bytes | Actual D trial 5.1, успешная повторная проверка; прежняя частичная копия остаётся явно test evidence |
| В receipt указано «enforced» | Project registration открыла FileStream с выбранным sharing mode, но конкурирующий write/delete не испытывался → отдельно записывать configuration, observed operation и проверенный отказ | S trial 5.1 и последующий parent review; successful API return не доказывает adversarial enforcement или crash durability |

Не переносить исторические agent PASS, Human permissions, licensing gaps или
host qualification на новую работу. Source citations и formal semantic status
сохраняют собственные требования. Новые наблюдения текущего цикла добавляются
после проверки, с named use и оставшимися ограничениями.
