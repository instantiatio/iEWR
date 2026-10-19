# Источники DDB и SVV

Основа изготовления редакций 0.1.1 от 19.10.2026. Таблица указывает использованные источники, их редакции и SHA-256 сохранённых байтов. Это происхождение и маршрут повторного получения, а не утверждение, что источник уже дал результат конкретной программной задачи.

## FPF и DPF

Оригинальный FPF: [commit cc2e8aa9e6183481a00300c3a987a1478ecf5860](https://github.com/ailev/FPF/blob/cc2e8aa9e6183481a00300c3a987a1478ecf5860/FPF-Spec.md), SHA-256 `07b2f6339ec5a8add1d0a28613cd1ea8a1696fc6200d3be6774924967d09c26e`. Адресно применены E.4.DPF/E.4.PFAD, E.8, E.11.PFP, E.21, E.19, E.4.DPF.DA, F.19 и нужные зависимости; маршрут в сохранённых оценках. Полное чтение FPF не выполнялось.

| Источник | Использованная редакция и вклад | SHA-256 сохранённого текста |
|---|---|---|
| [SYSE](https://github.com/ailev/FPF/blob/cc2e8aa9e6183481a00300c3a987a1478ecf5860/DPFs/Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md) · [использованный экземпляр](https://github.com/instantiatio/iEWR/blob/efec4b278404c6b5ad0965247a38379668b8aa53/frameworks/dpf/systems-engineering/2026-10-15-rev-b40c9df9/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md) | 2026-10-15-rev-b40c9df9; SYSE.6, SYSE.13, SYSE.19, SYSE.36, SYSE.53 | `0ad7d10887375a2a8411c01784835763bfbd97706f3848580a791968b984e235` |
| [ME](https://github.com/ailev/FPF/blob/9e1c48349bd0a06d8d49e2de45fbcff386d47ae5/Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md) · [использованный экземпляр](https://github.com/instantiatio/iEWR/blob/efec4b278404c6b5ad0965247a38379668b8aa53/frameworks/dpf/method-engineering/2026-09-20-rev-9e1c4834/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md) | 2026-09-20-rev-9e1c4834; ME.6, ME.21 | `15e74fa6fcc5aeed7492cda684f04a619e333c99df3a50931c1f873d832851f6` |
| [ISDLC](https://github.com/instantiatio/iEWR/blob/efec4b278404c6b5ad0965247a38379668b8aa53/frameworks/dpf/instantiatio-sdlc/0.3.0/DPF.md) | 0.3.0-package-5.7.1; ISDLC.1, ISDLC.2, ISDLC.3, ISDLC.4, ISDLC.5, ISDLC.6, ISDLC.7, ISDLC.8, ISDLC.10, ISDLC.11, ISDLC.12, ISDLC.13, ISDLC.16, ISDLC.18, ISDLC.15 | `87084e9a6d11e85bf11e3b2d38427b7e3aa9655aef24a285f23e626147be909c` |
| [RMP](https://github.com/ailev/FPF/blob/cc2e8aa9e6183481a00300c3a987a1478ecf5860/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md) · [использованный экземпляр](https://github.com/instantiatio/iEWR/blob/efec4b278404c6b5ad0965247a38379668b8aa53/frameworks/dpf/research-method-practice/2026-10-15-rev-b40c9df9/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md) | 2026-10-15-rev-b40c9df9; RMP.1, RMP.2, RMP.7, RMP.8 | `fb5dff009015f2c137e24d6c44a2a6aa662ff125e272457f1a2f38a3b99061b2` |
| [SIE](https://github.com/ailev/FPF/blob/cc2e8aa9e6183481a00300c3a987a1478ecf5860/DPFs/Engineering%20DPF%20Suite/SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK.md) · [использованный экземпляр](https://github.com/instantiatio/iEWR/blob/efec4b278404c6b5ad0965247a38379668b8aa53/frameworks/dpf/semantic-integration-engineering/2026-10-15-rev-b40c9df9/SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK.md) | 2026-10-15-rev-b40c9df9; SIE.3, SIE.5, SIE.10 | `750c1aee8861b490d22fa9fc05b109b319a966994e52d86e024a17d68f768d40` |
| [CHK](https://github.com/ailev/FPF/blob/9e1c48349bd0a06d8d49e2de45fbcff386d47ae5/Engineering%20DPF%20Suite/CHECKLIST-PRINCIPLES-FRAMEWORK.md) · [использованный экземпляр](https://github.com/instantiatio/iEWR/blob/efec4b278404c6b5ad0965247a38379668b8aa53/frameworks/dpf/checklist/2026-09-25-rev-9e1c4834/CHECKLIST-PRINCIPLES-FRAMEWORK.md) | 2026-09-25-rev-9e1c4834; CHK.6 | `503da6fef65ee02de0e8ce41c2600479a2ce7e6163f3cb5ea6f09d6c026ce679` |
| [VID](https://github.com/instantiatio/dpf-lab/blob/bd1cabb2e0e1757801aab142d44184ee195034ce/DPFs/VID.md) · [использованный экземпляр](https://github.com/instantiatio/iEWR/blob/efec4b278404c6b5ad0965247a38379668b8aa53/frameworks/dpf/instantiatio/5.8.1/VID.md) | 0.3.0-package-5.8.1; VID.10, VID.11 | `8a72afd59c3cf0764c62f07f4d3c4f8f9bf9745d3b406513eaba58e1f7de1112` |
| [CMP](https://github.com/ailev/FPF/blob/cc2e8aa9e6183481a00300c3a987a1478ecf5860/DPFs/Foundational%20Thinking%20DPF%20Suite/COMPUTATIONAL-THINKING-DPF.md) | 2026-10-14-rev-cc2e8aa9; CMP.10, CMP.13 | `968a680407440693179cbebdf150460532495b70ca61ce0cf2a56293256c2a57` |

Упакованные экземпляры могли получать переносимые адреса ссылок: digest относится к указанному использованному экземпляру, а не автоматически к upstream carrier.

Точный ISDLC-базис — 0.3.0 из поставки iEWR, а не текущая 0.3.1-candidate. В SVV.4 отдельно и ограниченно использованы уточнения .5/.7/.11 из [ISDLC 0.3.1-candidate](../../DPFs/ISDLC.md), первоначальный Git commit `10a94c403ff9fd70e6e69a2db93d68e585bfef0f`, SHA-256 `d0a150818cbb089edc45100ddf142d9b5abdb9d9d9368208176ee0ab16887208`. Будущее изменение текущего ISDLC не переключает этот use автоматически.

DPF остаются самостоятельно применимыми. DDB передаёт модель, инварианты и механизм изменения; SVV при необходимости возвращает наблюдения, дефекты и границы вывода. SIE, CHK, SYSE, RMP, CMP и VID используются по нужному вопросу. Ссылка на их guidance не является уже полученным предметным результатом.

## Предметные источники

Снимки получены 19.10.2026; версия платформы и точный digest перечислены отдельно. В библиотеку не переносятся страницы/PDF и копии сторонних DPF. Веб-страница по прежнему URL может измениться: при зависимом новом применении сверяют нужный фрагмент и условия. Первоначальные captures остаются в исходном проекте.

| ID | Источник и использованный вклад | SHA-256 capture |
|---|---|---|
| N01 | [PostgreSQL 18 Chapter 11 Indexes](https://www.postgresql.org/docs/18/indexes.html) | `133053a3a56f926d9868a9fc508082634be3f8c8c88b60d84508c332cf6fb27e` |
| N02 | [PostgreSQL 18 Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html) | `209f1abff4501a009799d186b517ce0b05637a97faef3cc2d663086ae9972e6e` |
| N03 | [ISTQB CTFL Syllabus 4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf) | `3b072f81db5c7671aadacc42553e726faa93913a969cc7a89e9dc28c2318d1f1` |
| N04 | [SQLite Transaction](https://www.sqlite.org/lang_transaction.html) | `b65dc308fd9e0ce471844c97366a4f5ad3a1f42833a3b19486ad7d6555a8e24e` |
| N05 | [SQLite Isolation](https://www.sqlite.org/isolation.html) | `23395653f04984e4310b287ed548202d874e06ecd2cba17f32b2714e5b7ebef7` |
| NF | [Ramakrishnan/Gehrke — Schema Design and Normal Forms](https://www.cs.cornell.edu/courses/cs432/2004fa/slides/2004-11-10-NormalForms.pdf) | `3136da5266f50c2e58978b7577f28cddd7d51f146d9526875bdca2ac3568caea` |
| S05 | [Relational constraints](https://www.postgresql.org/docs/18/ddl-constraints.html) | `dbad83503774b48b2a33f70bbc9e3b21cbea40949680e1c4f6d29c206048c1aa` |
| S06 | [Transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html) | `0b5013fde5e842c82664f2d9fe599f1c8ef7756e8c3ecc254b589e3be9e0d356` |
| S10 | [Small code changes](https://google.github.io/eng-practices/review/developer/small-cls.html) | `0637b70bbb8235a8a3dfe86041e206bd91db35b4b8a4c34cb938f4d8fd6bf5c3` |
| S11 | [Property based testing](https://hypothesis.readthedocs.io/en/latest/quickstart.html) | `2bb41561075b9dab5462356b04eb4a017faede5a750ce91df2704297b747e828` |
| S12 | [User validation](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing) | `3e1bb2481af3ddbf74a1af8d1e9c03e44a1e204925d5a84fd4038430894b1152` |
| S16 | [Database evolution](https://martinfowler.com/articles/evodb.html) | `df80af1db6661e2599a094ec5b6e9dfda0c4581c7b61c647d73d124e0449559b` |

NF поддерживает различение lossless join и dependency preservation в отношениях-множествах; SQL NULL/дубликаты проверяются отдельно. PostgreSQL/SQLite описывают конкретные механизмы, не все СУБД. CTFL поддерживает V&V и способы вывода случаев; Hypothesis — свойства и генерацию, но не истину oracle. GOV.UK — получение наблюдений пользователей; EVO — совместную эволюцию схемы и кода. Сравнения и мутации привязаны к :11 и Solution соответствующих паттернов.

## Исследование

Предварительное [исследование 17 направлений](Research/REPORT.md), [карта покрытия](Research/COVERAGE_MAP.json) и [содержательные находки по 20 источникам](Research/SOURCE_FINDINGS.json) сохранены как история выбора предметных направлений. SOURCE_FINDINGS содержит исходные URL, роли, прочитанные вклады, hashes и ограничения; локальные исходные пути в этой исторической записи не объявляют файлы частью dpf-lab. Сами captures не перенесены.

## Атрибуция и пересмотр

Оригинальный FPF и заимствуемые вклады DPF Anatoly Levenchuk сохраняют его атрибуцию и применимые условия CC BY 4.0; [условия точной редакции FPF](https://github.com/ailev/FPF/blob/cc2e8aa9e6183481a00300c3a987a1478ecf5860/LICENSING.md). Материалы третьих лиц сохраняют собственные условия. Новая общая лицензия на собственный текст DDB/SVV не назначается.

При изменении источника, доступности нужного поставщика, механизма, требований или назначения восстанавливают границу влияния и пересматривают зависимые действия и выводы. Наличие URL, hash и успешная загрузка сами не квалифицируют метод или приложение.
