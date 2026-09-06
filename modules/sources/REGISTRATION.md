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
Регистрация добавляет persistent discovery, не applicability/precedence/authority.
Agent применяет только contributions, подходящие текущему вопросу, через
обычный S → F → runtime owners. New edition регистрируется явно и не переключает
active use; same identity/edition с другим digest отклоняется.
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
