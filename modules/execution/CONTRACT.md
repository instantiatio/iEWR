# X — одна bounded попытка, B1

Public `attempt_action(EditBasis)`, `read_execution(target)`. X проверяет current
basis/permission и local boundary, observed before, сохраняет pending до вызова
E. Только X инициирует effect operation. ExecutionStore — consumer-owned port;
P реализует namespace state/execution, один writer X. Basis/direct refs не
становятся universal RuntimeState или утверждением U.Work по наличию записи.

Pending/unknown для того же target блокирует последующие attempts, включая
fresh process и другой запрос. Нет replay по отсутствию transcript. Complete R
не реализован: unresolved outcome требует bounded return, а не repair здесь.
Если запись completion не подтверждена, даже observed applied receipt не даёт
заявить обычное завершение dependent use. Current source/window проверяются
снова E/G перед commit. No silent retry или background continuation.

Для formal Work требуется `A.13 → independent full A.15.1 → conditional F.6`;
Python record не восполняет admitted System, assignment, enacted Method,
temporal/containing-System и другие direct facts. B1 сообщает technical
performance observations, formal Work admission не утверждает.

Allowed imports: F/G/E. X не вызывает C/I/R. Internal owner writes под тем же
разрешённым storage boundary; missing/unknown storage удерживает action.
