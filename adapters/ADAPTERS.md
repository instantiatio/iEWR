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
