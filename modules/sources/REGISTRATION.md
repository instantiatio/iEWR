# S — external DPF registration и direct source use

Source text/edition остаётся у direct owner. Discovery не выбирает applicability:
package и project entries — один qualified набор кандидатов без precedence.
Unregistered exact source допускается через SourceReader/inspect_binding; index
не обязателен для чтения. FPF/DPF/LPF не являются capability routes или plugins.

Для внешнего DPF стандартный пользовательский locus — `source/external-dpf/`.
Пользователь скачивает файл, желательно сохраняет original filename и просит
зарегистрировать exact path обычным текстом. Agent inspect source in-place,
определяет identity/edition по source, фиксирует raw digest и необходимые
explicit metadata с собственными claim loci. Старые source loci в `project/dpf/`
остаются допустимы; перенос или вторая копия для регистрации не требуются.

F формирует минимально достаточную intended basis текущей операции: direct
request, exact source/digest, metadata, target и receiving use. Регистрация
сама по себе не требует отдельного MethodDescription, Method Engineering
или formal Work claim. Method/MethodDescription нужны только по потребности
текущей Work; достаточную существующую инструкцию можно переиспользовать.
G восстанавливает direct permission; X инициирует точную E/P operation.
S.read port не экспортирует register/unregister. Ни registration_basis string,
ни output helper не выдаёт authority.

Текущий bounded JSON consumer имеет собственный transport contract:
OperationBasis требует `method` Binding с role `method_description`. При выборе
этого consumer сохранять его contract и привязывать реально выбранную достаточную
инструкцию; не выдумывать основание и не требовать от пользователя отдельной
разработки MethodDescription ради source registration. Если нужного binding
или host controls нет, удерживается этот consumer use. Его обязательное поле
не вводит universal semantic gate для instruction-led работы, которая допускается
[P instructions](../../adapters/ADAPTERS.md) без обязательного JSON workflow.

E/P пишет только project/dpf/REPERTOIRE.yaml in place: source не меняется.
Это граница repertoire operation, а не всего пользовательского поручения.
При обычном постоянном подключении instruction-led агент дополняет один
существующий проектный указатель либо project/artifacts/dpf/GUIDE.md:
точный source_id/edition/digest и краткую ориентацию по предметным вопросам.
Сначала проверить авторское оглавление: оно охватывает все именованные методы
этой редакции и ведёт к существующим разделам. Если этого достаточно для поиска,
дать одну ссылку на полное оглавление и явно назвать охват; не переписывать
его таблицу в проектный указатель. Полный собственный перечень составлять лишь
при недостаточной авторской навигации, обозначив конкретный пробел. Для такой
проверки достаточно оглавления и заголовков/якорей; тела методов читаются при
выборе их вклада в задачу. Существующие записи и правки пользователя
сохранять; не заводить отдельный файл для каждого источника или метода.

Это отдельный локальный artifact effect под тем же поручением через F/G/X/E/P;
JSON register сам его не выполняет. При ограничении «только индекс» записывать
только repertoire; при запрете записи соблюдать его. Прямое чтение не требует
регистрации или создания указателя. Карточки при подключении, первом чтении
и последующем применении не создаются.

Новую редакцию подключать с проверкой перечня и условий, затрагивающих
текущий результат; обновить нужную навигацию. Прежние источники и необходимые
основания сохранять, изменившиеся условия не считать проверенными по одному
совпадению номера метода или новой контрольной сумме.

Запись repertoire и обновление указателя имеют отдельные фактические результаты.
Ошибка указателя не отменяет записанную регистрацию и не требует повторять её.
При запрете записи или недоступном файле продолжить разрешённое прямое чтение
и назвать незавершённую часть. Полноту поручения с необходимой, но неготовой
навигацией не заявлять. Не изменять и не переносить исходник.
Регистрация добавляет persistent discovery, не applicability/precedence/authority.
Agent применяет только contributions, подходящие текущему вопросу, через
обычный S → F → runtime owners. New edition регистрируется явно и не переключает
active use; same identity/edition с другим digest отклоняется.
После записи проверить схему реестра, привязку источника, сохранённые ссылки
и фактические эффекты; на достаточном результате завершить поручение.
Не повторять сбор метаданных и разработку навигации после успешной сверки.
При повторном подключении сверить точную запись и неизменность источника/указателя;
если прежний охват проверен и байты совпадают, переиспользовать проверку полноты
без повторного разбора всех методов. Недостающий указатель дополнить отдельно,
достаточный пользовательский указатель не переписывать ради сокращения.
Повторная registration может вернуть уже существующую запись без rewrite index.
Unregister меняет будущую discovery, не bytes/history. Partial/post-write source
drift сохраняет actual repertoire effect и удерживает dependent use.

Package required slots и distribution/inventory checks принадлежат
tools/package/integrity.py. Generic source reader не назначает semantic precedence
по required_slot; неизвестный slot — bounded package-profile question. Fixed
package composition проверяется отдельно. Integrity не distribution permission.

External registration не добавляет источник в bundled baseline. Его maintenance
выполняется по отдельному exact scope согласно
[product maintainer guide](../../docs/BUNDLED_DPF_BASELINE_REFRESH_AND_INTEGRATION_GUIDE.md).
Direct source use не требует регистрации, а регистрация не требует применения
source ко всем следующим вопросам. Помещение файла в пользовательский каталог
само по себе не выполняет ни регистрацию, ни применение.

Legacy helper/CLI сохранён как bounded comparison consumer в tools/compatibility;
normal modular runtime использует отдельные S read и E write ports. Exact old
78-case assertions сохранены; изменены только import/CLI/package wiring.
