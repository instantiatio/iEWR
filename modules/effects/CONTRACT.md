# E — реализация и учёт effects, B1

Public `assess_boundary`, `observe_effect`, `perform_bounded_effect`. Последний
принимает exact initiated operation от X и current direct basis. Он проверяет
G, записывает effect intent, вызывает EffectActuator один раз и сохраняет receipt.
После success, exception или unknown нет вызова нового Work/action/retry/repair.
No X/R/L imports. L получает только observations; C не экспортирует actuation.

Владелец operation receipts/unknown/dispositions — E. P EffectStore реализует
state/effects. Это технические facts, не domain Result, authority или acceptance.
`applied` означает exact readback; `not_performed` — нет target effect;
`unknown` блокирует dependent closure/use. Внутренний temporary effect, если
disposable без reliance, не требует ledger о ledger. Невозможность сохранить
receipt не стирает уже возможный target change.

Local boundary: no-follow, bounded files, cooperative directory lock, expected
bytes/inode и guard перед atomic replacement, fsync/readback. Всё это не atomic
CAS против hostile writer и не sandbox host. Overall boundary compensated:
single writer, pinned basis, protected inventory. Unsupported required control
останавливает effect. Не подменять это названием OS/provider или prose.
