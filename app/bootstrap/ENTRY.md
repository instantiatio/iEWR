# Явный bootstrap entry

В продукт входит `operation.py`: одна requested source-registration или
exact-artifact operation с явно заданным workspace и independently established
direct decision/Method bindings. One call, no queue, no decision generation,
no automatic retries. `--adapter` выбирает technical operation port, не DPF route.

`operation.py` требует serialized OperationBasis на stdin, decision path + exact
hash, method path и direct channel basis ref. Host/agent предварительно
устанавливает direct source и scope по G guidance; parameter не аутентифицирует
Human и не создаёт authority. JSON transport сохраняет producer-owned values
через `$type`/`$bytes`. Permission/Method и expected target проверяются перед
commit. Самосозданный decision JSON не является independent grant.

Owner records выбранного project находятся в `project/process/ewr/<owner>/`;
каждый namespace имеет одного writer. Они не обязательны для всякого analysis.
R получает bounded OwnerStore.snapshot queries.

Synthetic `invoke.py`, его B1/X04 tests и `tests/.work` относятся только к
development test окружению, расположены вне продукта. Их fixture instructions
в сохранённых exact CONTRACT.md не задают дополнительный продуктовый entry.
Старые state/<owner> fixtures не мигрируют автоматически в user history.

Чистый состав проверен local POSIX subprocess tests с synthetic direct channel.
Проверены bounded operation/reuse/denial cases; это не полная host qualification.
Live authentication, host-wide enforcement и unattended runner не заявлены. Outside authorized tool/filesystem
envelope — affected hold. Справка: `python3 -I -S -B app/bootstrap/operation.py --help`.
