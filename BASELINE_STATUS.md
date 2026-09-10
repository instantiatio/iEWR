# iEWR 5.2.2-beta.3 — candidate для Human acceptance

## Редакция документации 2 — 11 сентября 2026 года

По поручению пользователя основной README изложен инженерным русским,
сопровождающий список изменений сокращён. Программная версия — 5.2.2-beta.3;
идентификатор новой поставки — `iEWR-5.2.2-beta.3-docs.2`.
Исходный архив beta.3 сохранён, SHA-256:
`a21ffab8bb259dd2ae4abe4b0035e7abc50edc64aceb3df6d0061f72c3e67b6c`.
До правки все 100 файлов продукта совпадали с этим архивом.

Изменены только README, эта запись и сведения о составе и контрольных суммах.
Код, инструкции модулей, AGENTS, источники, права и схема взаимодействия
модулей сохранены. Проверены соответствие смысла, подписи и связи схемы,
команды, ссылки, состав, контрольные суммы и распакованный архив.
Предыдущие агентные испытания ниже относятся к названным там конфигурациям;
редактура не считается их повторным выполнением. Ограничения подачи в Codex
и технических средств POSIX сохраняются. Приёмка и публичная публикация
этой редакции не выполнялись.

## Исходная beta.3: изменения и результаты испытаний

Третья тема: понятное ведение, продолжение и завершение поручения. Исходная
конфигурация — file-preservation candidate 5.2.2-beta.2, 100 файлов, ZIP SHA-256
`20482de5ed3641bbb4c63837e36f21ce8b6fd1dab708675224877887c0f2b431`.
До изменения portable diff подтвердил нулевой product delta. Прежние пакеты
и их наблюдения сохранены; переход к новой теме не объявляется их приёмкой.
Новая поставка ещё не принята; `distribution_ready=false`, not a public release.

## Изменение и совместимость

Достаточность результата теперь явно относится ко всему текущему поручению.
Необходимые разрешённые действия после промежуточного результата продолжаются
без нового «продолжай»; существенная развилка возвращается человеку до зависимого
действия. При препятствии выполняется доступная независимая работа; показываются
точный пробел и условие возобновления. Завершение явно и не создаёт новой задачи.

[I interaction](modules/interaction/HUMAN_INTERACTION.md) задаёт смысловые
заголовки, «Требуется решение» с реальными нумерованными альтернативами,
рекомендацией и последствиями, «Кратко» непосредственно перед длинным запросом
решения и явное ожидаемое участие. Номера стабильны по вопросу/редакции,
свободный ответ и условия сохраняются. AGENTS/README/F/X/C/R/G согласованы;
единичный dispatch, independent grounds и owner DAG не изменены.

**5.2.2-beta.3** — следующая patch candidate редакция instruction support.
Python code, Core, источники, DPF aids и scaffold неизменны относительно beta.2.
Нового PM owner, планировщика, универсального плана/журнала или grants нет.
Сохранены [общие правила файлов](project/README.md): source/handoff/artifacts,
неограниченное по умолчанию хранение оригиналов/редакций/оснований, обоснованная
достаточность метаданных и прежние границы файловых controls. Перенос reference,
очистка пользовательских материалов и публикация не выполняются.

## Qualification третьей темы

11 сентября 2026: выполнены portable configuration/DAG, selected inventory,
source/Core/Python preservation и local-link checks. 16 actual fresh CLI
observations: два baseline contrasts и 14 candidate случаев в трёх configurations.
Multi-step поручение доведено до достаточного комплекта, независимая работа при
blocker выполнена, условия/собственный ответ/номера сохранены, неоднозначный ответ
не угадан, unknown отправка не повторена. Простая правка не создаёт новых файлов,
планов или согласований. Код не изменён; старые unit/host observations ниже
остаются историческими и не выдаются за повторные проверки.

Подача в default Codex CLI 0.153.4 (configured gpt-6-astra, pragmatic, без model
override) соблюдалась непоследовательно. После pre-send refinement длинный ответ
получил требуемую структуру, два коротких снова не имели заголовков. В cached
metadata модели обнаружены общие конфликтующие style defaults; это не захваченный
live prompt и не доказательство единственной причины каждого пропуска.

Три повторных случая на configured host с разовой добавкой приоритета project/user
presentation прошли: короткий результат, смешанный результат/нужные данные,
длинный разбор с «Кратко» непосредственно перед «Требуется решение», нумерованными
вариантами, рекомендацией и последствиями. Добавка и [пример запуска](adapters/ADAPTERS.md)
не меняют permissions, scopes, approvals, sandbox или capabilities. Постоянный
профиль пользователя не изменялся. Эти наблюдения не переносятся на прежний
host: его failures сохраняются, безусловное соблюдение формата не заявляется.

Trial configurations до обновления qualification:
`441e919145c3e986b134d3067c0b6a28ea50e63096ed04c868adc9eca94e66c1`
(initial), `7d24bcfa0aab9eafc670f962e1164e5131c567ff2451933f506ede0d22acf681`
(pre-send refinement), `9c4310f62603d2e92b171894ef39fcecc594dbcbb0baa530b601683c7763f26a`
(P/host binding). После последнего trial меняется только qualification и её
configuration/manifest hashes. Commands/events, ответы, before/after, исключённая
подготовка с Windows long-path failure и точное сопоставление revisions сохранены
во внешнем delivery evidence. Ошибки read-only команд и transport fallback
включены в наблюдения, а не скрыты.

Ни один из 16 completed процессов не изменил product/source bytes или удалил
файлы; проверены expected file effects и сохранённая история recovery. Это
bounded synthetic project trials, не статистическая надёжность, universal
Human usability, самостоятельная внешняя отправка или crash/race qualification.
Первый baseline contrast также выполнил multi-step поручение; улучшение stop
не выводится причинно из этого сравнения. Время включает общую нагрузку и
fallback WebSocket→HTTPS; общая экономия времени/токенов не установлена.

## Сохранённая первая тема

[F](modules/formation/DOMAIN_WORK.md) теперь явно требует самостоятельно
рассматривать доступную предметную основу до существенной постановки, критериев
и способа работы и содержательно применять пригодные методы с нужным вкладом.
Достаточная основа переиспользуется; mechanical edits не требуют нового поиска.
[S](modules/sources/GUIDANCE.md) соединяет package/project repertoire, краткие aids
и bounded original reading, сохраняет различия unsearched/unavailable/no-fit
и исключает stale aids из затронутого use. [I](modules/interaction/HUMAN_INTERACTION.md)
показывает выбор и фактический вклад до/после зависимых выводов.

[Путеводитель](catalog/dpf/GUIDE.md) охватывает шесть текущих package entries;
четыре [карточки](catalog/dpf/CARDS.md) покрывают ограниченные вопросы PSD.4,
PSD.13, ME.3 и ME.10. Это sparse prototype, не полная замена DPF. Author navigation
переиспользуется. [Правила aids](catalog/dpf/README.md) и образец описывают
происхождение, exact source bindings, сохранённые условия, source returns и
обновление только затронутых claims. Производные адаптации атрибутированы.

При обычной внешней регистрации краткая проектная ориентация является отдельным
artifact effect агента в пределах поручения. Mechanical JSON register по-прежнему
пишет только repertoire. Его успех не объявляется получением aid. Index-only
scope соблюдается; отсутствие aid не блокирует прямое чтение. MDPE служит только
внешним test input и не включён в package.

Core Contract 1.0 RC, owner APIs, import DAG и schema репертуара
сохранены. Нет новых owners, workflow engine, source execution, автоматических
grants или DPF-specific runtime routes. Bundled source bytes/licensing и local
experimental SDLC неизменны. **5.2.2-beta** — patch: уточнение существующего
instruction-led выбора/применения и поддерживающих материалов без изменения API.

## Историческая qualification DPF candidate 5.2.2-beta

Выполнены portable configuration/import-DAG, inventory/digest и package checks;
проверены 149 owned local links, 13 fragment targets новых aids, шесть source
bindings и неизменность 44 source/Core/Python files относительно baseline.
Selected inventory — 100 files (99 manifest hashes, 98 configuration rows).

Девять свежих CLI observations в изолированных selected snapshots: baseline,
новые instructions с original navigation, candidate с карточками; два варианта
внешней музыкально-танцевальной задачи; обычная и index-only регистрация;
механическая правка; mismatch aid digest с direct original fallback. Candidate
самостоятельно обнаружил и содержательно применил подходящие методы; edits
сохранили точный разрешённый scope. Контроль baseline дал разумный ответ без
DPF discovery. Неизменное продолжение и changed premise дополнительно проверены
в уже существующем контексте; это не clean discovery evidence.

В DPF candidate trial instruction/aid bytes совпадали с предъявленными;
после тех trials менялись только qualification-запись и configuration/manifest.
В последующих темах некоторые инструкции дополнены; прежние наблюдения не
выдаются за испытание этих новых bytes. Исходная DPF trial configuration:
`6d5df82da00f818bd7ce3deb02e989754db7cdf865bbe47df49c9299a980e6f6`.

Первые inherited-context trials и внешние fixtures с ошибочным source_id
исключены из соответствующих claims; повторные schema-valid snapshots проверены
отдельно. Ошибки подготовки и transport, commands/events, before/after и пределы
сохранены во внешнем REPORT/evidence. В двух local contrasts карточки уменьшили
returned file-output volume; общей экономии времени/токенов или causal superiority
эти пробы не устанавливают. Нет claims о full-source semantic equivalence,
наблюдённом физическом обучении или формальном Work admission.

## Историческая qualification file-preservation candidate 5.2.2-beta.2

Выполнены 17 portable unit tests: handoff/artifacts operation scope,
guard/refusal, before/after failure disposition с явными doubles; чтение двух
прежних пакетов, исключение пользовательских файлов, новый scaffold и запрет
перезаписи ZIP. Пять real POSIX IO tests пропущены на Windows: fcntl/dir_fd
и защита от реальной гонки этим не квалифицированы; shim не использован.

Десять выбранных fresh CLI observations: два baseline contrasts и восемь
candidate случаев — обычная правка, исправленная редакция, входящий/возвращённый
источник, незавершённый и завершённый ответ в форме, разрешённая очистка,
заявленный конфликт при доступной записи и восстановление после изменения
рабочей формы. В наблюдениях сохранены старые экземпляры, пользовательские
правки и условия ответа; ordinary edit не создал новых файлов/согласований.
Конфликтная запись удержана по недостаточности контроля, не по read-only sandbox.
Свежий следующий агент восстанавливал решение без предшествующей переписки.
Это bounded synthetic project observations, не human usability/hostile-writer
stress tests и не формальное Work/Method admission.

Пробы привязаны к двум exact configurations до обновления qualification:
`6c69c09c3250b361cf62b7f82e6e5bbe0a029a9957249b8de307401abde9eb64`
и `fe339db49d519d4f3476d0ca135bbfdfd3b94fe968ba1b47396676960ddaa22e`.
Между ними уточнено только согласование обозначений редакции в project/README
и пересчитаны metadata hashes; затронутое исправление проверено повторно.
Финальная qualification-запись и её configuration/manifest hashes обновлены
после trials; содержательные инструкции и runtime code далее не менялись.

Первый transport/staging batch исключён; исходная ошибка fixture status/outcome
исправлена без изменения продукта. Первая проба редакции с
сопроводительной записью и отдельный read-only conflict control сохранены,
но не подменяют выбранные повторные случаи. Полные prompts/events, before/after,
метрики, ограничения и correction history сохранены вне product payload.
Проверки выбранных bytes/DAG, исходников, ссылок и exact ZIP выполняются
при подготовке поставки. M1–M8 имеют только явно наблюдённый scope; общего
ускорения, минимальности нагрузки или универсальной надёжности не заявлено.

## Сохранённые пределы

Instruction-led поведение зависит от доступного host/model и прямых оснований
действий. Несколько локальных trials не устанавливают universal transfer,
causal superiority или Human usability. Компактность документа не доказывает
снижения общей нагрузки. Реальное применение имеет нужные direct основания;
formal Work/Method admission не выводятся из trace, файла или PASS.

Portable checks на Windows — compensated maintainer consumer, не qualification
POSIX no-follow/flock runtime adapter. Live JSON authentication, unattended E.16,
hostile writer/ABA, внешний host matrix и full FPF/domain conformance не
квалифицированы. Все ограничения baseline, не изменённые текущими evidence,
сохраняются. Точный состав — [PACKAGE_MANIFEST](PACKAGE_MANIFEST.md).
