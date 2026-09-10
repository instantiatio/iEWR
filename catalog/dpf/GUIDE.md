# Быстрый выбор предметной основы

Найдите вопрос и первый нужный результат. Рассмотрите пересечения нескольких
DPF; сходство названия ещё не доказывает пригодность. [S](../../modules/sources/GUIDANCE.md)
задаёт достаточное чтение, [F](../../modules/formation/DOMAIN_WORK.md) — выбор и
содержательное применение. Прочитанное на неизменной основе переиспользуется.

## Доступный package repertoire

| Вопрос | Кандидат и полезный вклад | Граница / куда углубиться |
|---|---|---|
| Что именно за проблема, какие варианты и критерии сравнивать, что рекомендовать? | [PSD](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#table-of-contents): постановки, граница, альтернативы, последствия, неопределённость, рекомендация | Предметные факты и решение получателя имеют собственные основания. Для bounded boundary/return есть [PSD.4 и PSD.13](CARDS.md#psd-4). |
| Какую систему получать или менять; как связать описания, конфигурацию и проверки? | [SYSE](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#table-of-contents): устройство и interfaces, способы получения результата, конфигурации, integration и assurance | Системная инженерия включает physical и software subjects; code-only маршрут из названия не следует. Сначала авторский вопросный индекс. |
| Как выбрать, описать, проверить или улучшить способ работы и доступ к нему? | [ME](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#table-of-contents): критерии fit, сравнение способов, описания, source recovery, retrieval и trials | Описание, supporting tools, performed work и эффективность различаются. [ME.3 / ME.10](CARDS.md#me-3) покрывают узкие критерии и retrieval. |
| Как изменить распределение вкладов, назначения, полномочия и обеспечивающие связи организации? | [OCE](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#table-of-contents): current arrangement, альтернативы организации, позиции, assignments, human–AI/provider configuration | Схема организации и доступ не устанавливают полномочий или фактического вклада. Сравнивать нужные реальные отношения. |
| Как продолжать операцию при меняющемся спросе, очередях, ограничениях и обязательствах? | [OPS](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#table-of-contents): shared attention, продолжение случая, admission, capacity, coordination и улучшение операций | Календарь/статус не доказывают исполнение и не создают автоматический следующий шаг. Для нового способа работы может понадобиться ME. |
| Где код реализует поведение; как изменить, диагностировать или перестроить его? | [SDLC](../../frameworks/dpf/sdlc/0.1.0/SDLC_DPF.md#table-of-contents): четыре bounded code questions | **Experimental local working candidate 0.1.0**, не upstream DPF и не квалифицированный общий SDLC. Source self-description о публикации историческая; package presence не усиливает admission/fit. |

Внешние entries смотреть в существующем `project/dpf/REPERTOIRE.yaml` и,
если подготовлен, `project/artifacts/dpf/GUIDE.md`. Они равноправные кандидаты,
даже если namespace неизвестен и строки выше о них нет. Для exact direct source
можно сразу открыть его навигацию. Не найденная в этой выборке тема не означает,
что подходящего DPF нет. После проверки пригодности нужный метод применяется.

## Exact source bindings

Актуальный состав устанавливается [репертуаром](../../frameworks/dpf/REPERTOIRE.yaml)
и actual bytes. Эта таблица привязывает именно данную производную редакцию.

| Alias / source_id | Edition | SHA-256 |
|---|---|---|
| PSD / problem-structuring-decision-support | 2026-09-05-rev-d514a6fc | dbf0f86337d24dcb89d90faa38240991579b9fe6d1487120285c36126673efa9 |
| SYSE / systems-engineering | 2026-09-05-rev-d514a6fc | 45c49096102c11c7ac1024e3b459f7b9e791c48613163af46f2d63cfdf579887 |
| ME / method-engineering | 2026-09-05-rev-d514a6fc | cc9056e958c0435ec33666291f6fa4bb207d5e307ae6b28213f134f74d92bef4 |
| OCE / organization-change-engineering | 2026-09-05-rev-d514a6fc | a7ab62df62afe22086165830d0c91bf04c43d07437431f7d6944c571894da5ac |
| OPS / operations-management | 2026-09-05-rev-d514a6fc | 5d2ff495c0a6fff809092c8e36c826ae3a6d94860cf58d63ef61a41feaeedd87 |
| SDLC / sdlc | 0.1.0 | eb6e5b1e69ee8192fbcd73acf05bca3484ac2637f79abb810e63d06e3a25f7da |

Производная адаптация iEWR, 2026-09-10: русская ориентация по авторским
оглавлениям/practical entries; это не полный пересказ. Пять upstream источников:
Anatoly Levenchuk, 5 September 2026, commit `d514a6fcb7908af8e773ed054b9582394f755caf`,
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) с [third-party limits](../../frameworks/dpf/NOTICE.md).
Статусы оригиналов и ограничения их claims сохранены; сам путеводитель не
устанавливает пригодность каждого метода для конкретной задачи.
