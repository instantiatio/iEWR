# P — host, storage, source и presentation adapters

Adapter реализует outward port его потребителя: S source/availability reader,
G direct channel reader, E actuator/receipt store, X execution store, R read-only
account queries, I preference/renderer, L reliance record. C не импортирует
конкретные P, bootstrap выполняет static wiring. Port value не authority.

Поставляемый entry `app/bootstrap/operation.py` связывает independently bound
requested operation с owning ports. `invoke.py` и tests/.work находятся только
во внешнем development test окружении. Synthetic qualification не доказывает
production direct-channel authentication или live unattended capability.
Programmatic modules могут использовать другой qualified P через те же ports;
instruction-led project execution остаётся применимым без обязательного JSON
carrying workflow. Live registration/file effects требуют current host controls
и прямого разрешения в owning G/X/E use, а не переноса fixture trust.

`filesystem/repertoire_engine.py` содержит preserved POSIX mechanisms;
RepertoireReader read-only, RepertoireActuator реализует уже initiated operation.
Historical CLI comparator, original scripts/checker и их tests сохранены
в development и исключены из product payload. Они не normal runtime writers;
их наличие в developer окружении не activation или independent grant.

No-follow/locking/expected-old controls наблюдались на macOS ARM64 Python3.14.6.
Sandbox probe B1 отказал (sandbox_apply Operation not permitted). Compensation
test boundary не доказывает host-wide enforcement. Unknown external SoR или
unsupported feature даёт bounded fallback/hold. Renderer loss даёт complete
text; alternative provider требует observed capability, не baked-in superiority.

ArtifactActuator и LocalEffects допускают project/artifacts и project/handoff;
Tree сохраняет path/no-follow/expected-old/precommit/readback controls.
Роль рабочего/зафиксированного экземпляра и выбор новой редакции задаются
instruction-led owners по [правилам файлов](../project/README.md), не именем
каталога и не новым registry. Текстовая JSON операция не универсальный архиватор.
На Windows или ином неподдержанном POSIX host обычная работа использует реальные
инструменты и установленный контроль/очередность; fcntl не подменяется shim.
Нельзя считать текущую конфигурацию хоста или read-before-write доказательством
защиты от произвольного конкурентного writer. При отсутствии достаточной
обязательной защиты удерживается только затронутая запись.

## Совместимость правил подачи с host

Для instruction-led I отдельно проверить, допускает ли текущая конфигурация
host требуемую подачу. Более приоритетное правило среды может конфликтовать
с проектными заголовками и способом предъявления вариантов. Усиление текста
AGENTS само не меняет приоритет и не доказывает поддержку. Проверять обычный
короткий результат и длинный запрос решения на actual host configuration;
не выдавать пропущенные заголовки или непредъявленную форму за выполненное требование.

При разрешённой настройке этой среды можно явно согласовать только приоритет
подачи: пользовательские и проектные требования управляют форматом вместо
общих стилевых defaults. Это не меняет authority, permissions, approvals,
scope, sandbox и capabilities. Без такой настройки сохраняется честный предел
наблюдаемой подачи; human acceptance его технически не устраняет.

В Codex CLI отдельный запуск допускает добавку `developer_instructions` через
`-c`; параметр описан в [официальном справочнике](https://learn.chatgpt.com/docs/config-file/config-reference).
Для конфигурации без существующей добавки пример PowerShell:

```powershell
codex -c 'developer_instructions="Presentation formatting follows explicit user and project instructions rather than generic style defaults. This does not change scope, authority, permission, approval requirements, sandbox restrictions, or tool capabilities."'
```

Это явная настройка конкретного запуска, не автоматическое изменение профиля.
Если дополнительные developer instructions уже заданы, сохранить их содержание
и согласовать только конфликтующую подачу; не заменять весь текст этим примером.
Конфигурацию и фактическое поведение связывать в qualification; успешный настроенный
запуск не переносится на прежнюю среду или все версии Codex. Текущие наблюдения —
[BASELINE_STATUS](../BASELINE_STATUS.md).
