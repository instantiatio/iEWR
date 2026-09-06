# C — явная передача запроса

C не workflow engine: нет stages, queue, durable scheduler, event bus,
completion listeners, automatic successors или Method/source selection.
`dispatch` выполняет ровно один explicitly requested public owner operation.
Caller задаёт current question/use/scope и stop/return, не status→next table.

F выбирает intended basis, G работает с direct grounds, X инициирует action,
E реализует/account effects, L assess exact use, R восстанавливает three accounts.
Correlation восстанавливается из owner refs; C не имеет своего truth store.
I обращается к C, не напрямую к X/E/G. Bootstrap связывает C/I/P без чтения
decisions при construction. Public values сохраняют producer ownership.

Functional DAG: S→∅; G→S; E→G; L→S/G/E(query); F→S/L;
X→F/G/E; R→S/F/G/X/E/L(query/assessment); C→S/F/G/X/E/L/R; I→C.
P импортирует consumer-owned ports/value types, не выбирает business semantics.
Нет X→R/C, E→X, S→G/X, I→P actuation. Intra-module imports допустимы.

Mixed package: bounded deterministic helpers не заменяют semantic/domain
reasoning. Historical CONTRACT.md B1 — ограниченные первые seam/Method
descriptions, не объявление последующих capabilities отсутствующими и не новая
global policy. Current module guidance указан entry; Method hash конкретного
старого действия сохраняет прежний смысл.
