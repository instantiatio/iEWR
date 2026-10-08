# Проверка iEWR 5.7.0 Beta

Дата: 2026-10-08. Предмет — новая exact поставка на основе опубликованной 5.6.4 и сохранённого instruction candidate-r1. Исходная основа — [BASELINE_STATUS.md](BASELINE_STATUS.md), выбранные файлы — [PACKAGE_MANIFEST.md](PACKAGE_MANIFEST.md). Содержательная оценка, целостность bytes и исполнение механизма имеют разную силу; общий сертификат работоспособности не выдаётся.

## Содержательная основа

Пересмотрены текущие инструкции и связи S/F/G/X/E/L/R/C/I/P. Применены нужные положения закреплённого оригинального FPF: F.19 для формулировок, E.16 для действия/исполнения; ME.12/.22, CHK.1/.6, SYSE.46/.49 для согласованности и проб. ISDLC.4/.5/.11/.12/.16 использованы для хранения истории, повторов, совместимости и целостной правки; SYSE.41 — для exact передачи и partial effects. Полное чтение FPF и всех тел 242 методов не выполнялось.

Две проверки candidate-r1 нашли конкретные дефекты. Обе познакомились с историческими сведениями внутри комплекта вопреки условию слепого чтения. Эти сведения не засчитаны evidence собственных проб; полностью слепая независимость не заявляется. Замечания закрываются исправлениями и наблюдениями текущих bytes. Отчёты, точные входы, журналы и scripts сохраняются вне product payload в evidence выпуска.

## Наблюдённые локальные проверки

26 именованных regression-проверок завершились успешно на macOS ARM64, Python 3.14.6; Markdown renderer использовал Node 24.18.0. Это 26 тестовых функций с дополнительными controls, а не 26 независимых пользовательских опытов. Direct channels, authority и permissions заданы synthetic premises.

| Предмет | Наблюдение и предел |
|---|---|
| Ответы | Single yes/no, явная поддержанная часть, полный одинаковый effect group. Subset и supplied unambiguous label не снимают ambiguity. Вырезанный положительный span не удаляет условие/запрет полного ответа. Expiry, subject drift, conditions и source collision удержаны. |
| История интерпретаций | Новый assessment с source/predecessor refs; исходная запись и прежняя оценка byte-equal. Identical interpretation reuse без rewrite. Legacy response_evidence дополняется без миграции; changing question не rebind прежнего согласия. |
| Profile | Explicit start; потеря G прекращает тот же Profile без приращения actuals. Восстановление не resume; missing evidence/actuals при config/guard failure сохраняются gap и не оставляют active. Entry до начала и отдельный explicit successor проверены. Ledger не выполняет target action и не даёт permission. |
| Регистрация DPF | Свежий scaffold с project/dpf/ успешно создаёт index, source byte-equal. Missing parent удерживает bootstrap до X/E intent; после разрешённой подготовки independent attempt возможна. Direct adapter pre-actuation failure — not_performed. |
| Artifact и unknown | Denied/conditional/expired не меняют target. Positive и duplicate reuse проверены; user edits сохранены. Injected receipt loss после actual replace оставляет unknown; новый operation ID не обходит no-replay. |
| Decision View | Новые title/revision создают отдельные readers; прежние exact bytes и Markdown сохранены. Identical representation reuse. Hash, length и render опираются на один snapshot; injected source change при rendering удержан до reader/question write. Проверена сборка, не visual/browser или Human usability. |

До исправления пять различающих проверок воспроизвели исходные сбои на неизменном candidate-r1; сохраняемая positive/negative artifact проверка прошла на той же основе. Первая попытка новой regression обнаружила три ошибки сравнения tuple/list после JSON readback в новой assessment history; сравнение исправлено, повтор на новых bytes успешен. Неудачные попытки и outputs сохранены.

Отдельное независимое экспертное чтение новых README и RELEASE_NOTES целиком восстановило назначение, первый шаг и пределы обещаний. Прежние reports/tests/evidence/EXPERIENCE/RELEASE_HISTORY/VERIFICATION читателю не предъявлялись. Static reading выявило неполное прекращение Profile при config/guard failure без accounting, утрату условия из trimmed span и разные чтения source bytes при render. Эти замечания исправлены и повторно проверены; после сообщений автора recheck обозначен отдельно от первичного независимого чтения. Это не Human comprehension trial и не доказательство результата тестов.

## Состав и передача

142 файла: прежние 141 и пустой project/dpf/.gitkeep. Core Contract 1.0 RC, bundled sources, атрибуция и bindings byte-equal. Сохранены 14 DPF и 242 метода. Tests, owner records, пользовательские материалы, установленный оригинальный FPF и development evidence не входят в продукт. История — [RELEASE_HISTORY.md](RELEASE_HISTORY.md) и прежние exact архивы.

Configuration/import DAG и package checks проверяют selected bytes; method navigation — 242 адреса и 14 source hashes. Проверены 1489 локальных ссылок: вне frozen DPF отсутствующих targets не найдено. ZIP readback проверяет состав, CRC и каждый member. Итоговые observations и hashes сохраняются рядом с архивом в evidence выпуска. Первый package check обнаружил отдельный устаревший allowlist scaffold; после исправления повторяется на новых bytes. Эти checks не Method/Work admission, не FPF semantic conformance и не разрешение внешнего действия. Фактические main/tag/Latest/assets подтверждаются publication receipt без пересборки проверенного ZIP.

90 отсутствующих local file targets находятся в unchanged frozen DPF и установлены в исходном audit. Они не переписываются и не объявляются доступными по hash; dependent use требует доступного exact passage либо named gap. Оригиналы некоторых HUMAN_AI_SOURCE_CONTRIBUTIONS passages отсутствуют в доступном payload; прежние авторские assertions не квалифицированы заново.

## Пробы агента и границы

Прежние три fresh agent trials candidate-r1 проверили уточнение направления, выполнение двух порученных правок и honest partial result при недоступной дате. Они остаются ограниченной основой незатронутых правил, а не новыми испытаниями кода 5.7.0. Exact model/settings не раскрыты; single trial не доказывает causal improvement, надёжность популяции или понимание человеком.

Новый fresh agent в отдельной расходной копии продолжил прерванную правку памятки. Он использовал exact выбор Human из возвращённого source/candidate текущей инициативы, изменил только порученный рабочий файл, проверил его и обозначил завершение без нового согласования. Все 142 product files, source с ответом и process record byte-equal; лишних файлов нет. Это одна фактическая проба на synthetic inputs, не испытание всех вариантов recovery и не live external effect. Предыдущие авторские выводы, tests и ожидаемый маршрут агенту не предъявлялись.

Не квалифицированы live-channel authentication, hostile concurrent writers, Windows/все POSIX hosts, unattended execution и полная FPF conformance DPF. Instruction-led обязанности и helpers не перехватывают все host tools. Missing/unknown не PASS. Обычный путь сохраняется без обязательных Python/JSON records; удерживается только зависимое действие.

Для перехода сохраните старую поставку и project history, распакуйте новую отдельно, проверьте provenance source/decision/effect records и current host controls. В прежнем проекте перед выбранной программной регистрацией нужен существующий permitted project/dpf/. Ответы, readers и исходные редакции не перезаписываются; assessment history может дополняться. Завершённые и unknown операции не повторяются ради перехода.
