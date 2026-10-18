# C — один explicit dispatch, B1

`dispatch(owner, operation, **values)` вызывает ровно одну публичную операцию
и возвращает её результат. Static owner construction не выполняет reads/actions.
Нет workflow engine, loop, queue, phase/status progression, completion listener,
Method/DPF choice или собственной durable записи. Pending demand относится к
F/G/X/L/R; в B1 durable unresolved action хранится только у X/E по своим фактам.

Unknown operation/version → protocol blocker. После результата C ничего не
делает. Следующий вызов предъявляет host/agent по current question, explicit
owner result/demand и уже имеющемуся scope, а не по таблице стадий C. Operator
может остановиться на reuse/hold. E actuation не входит в public dispatch table;
материальную операцию инициирует X в рамках конкретного запроса.

Allowed imports: S/F/G/X/E/L/R public contracts; R отсутствует в B1. Нет P
imports/private internals. Public values re-exported I сохраняют producer owner.
