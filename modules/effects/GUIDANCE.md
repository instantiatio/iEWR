# E — technical boundary и accounting effects

E получает уже initiated X action с exact scope/current G grounds. Он не
инициирует Work/action, retry/repair/observation по собственному receipt, budget
или timeout. Normal C не экспортирует E actuation; L/R используют только queries.

Различать semantic requirement, observed host/tool/configuration, control,
authorized action и actual effect. `declared / enforced / compensated /
unsupported` описывают конкретную связь, не рейтинг tool. Enforced требует
observed control; compensated — мера, owner/evidence/residual risk. Неподдержанный
обязательный control удерживает dependent effect. Host product name не доказательство.

Для файлов [общий порядок](../../project/README.md) применяется и при ordinary
host tools: read-before-write не объявляется защитой от любой гонки. Установить
доступную условную запись/блокировку либо действующую очередность; неизвестный
writer при недостаточном контроле удерживает опасную замену. После возможной
записи reconcile effect до retry; новая редакция не разрушает сохранённую прежнюю.
Temporary/старый файл disposable только по поручению и при отсутствии unique
edits/downstream reliance. Атомарная замена файла не транзакция комплекта.

До отправки persist recoverable intent, если без него нельзя reconcile effect.
После — receipt/partial/unknown и disposition. External success/local crash
может оставить unknown; idempotency key не exactly-once guarantee. Outcome
storage failure не отменяет уже materialized bytes. Cross-owner transaction и
универсальный rollback не обещаются. E state один writer, external SoR первичен.

Каждый material durable effect к closure/handoff: represented in current
result/baseline, authoritative external SoR, disposable без downstream reliance
либо explicit unresolved с hold только dependent use. Persistence не adequacy.
Reconciliation/новое наблюдение получает отдельный explicit X/G basis; R лишь
возвращает demand. Ни repair, ни profile successor автоматически не появляются.

Текущий local P: POSIX no-follow, size bounds, cooperative lock, expected bytes,
precommit G/current parent, atomic replace/readback. Overall compensated single
cooperative writer, не host sandbox/hostile-writer CAS. Store writes не создают
бесконечную ledger-of-ledger. Supported observed substrate: macOS ARM64 Python
3.14.6; Python ≥3.10 interface floor не доказанная полная version matrix.
