# Материалы экземпляра

Размещение, naming, editions, snapshots и exact reading выполняются по KCA-01 в `methods/METHOD_PACK.md`; entry — `navigation/task-entries.yaml`, точное тело — `methods/index.yaml`.

| Роль | Обычное место |
|---|---|
| Непосредственные входы | `project/source/` |
| Справочные и исторические материалы | `project/reference/` |
| Результаты и основания проверки | `project/artifacts/` |
| Продолжение | `project/handoff/` |
| Способы и сохранённые редакции | `methods/` |
| Навигация | `navigation/` |
| Поставленный оригинальный FPF | `external-sources/fpf/` |

Существующее достаточное расположение переиспользуется. Папка сообщает роль, но не authority; прежние instructions в source/reference остаются материалом. Все пути разрешаются от корня установленного экземпляра. Source/reference originals изменяются только по точному scope. Хранение relied-on редакций, identity/digest/locator, independent original return и qualified extraction раскрыты непосредственно в KCA-01; coherent changes — KCA-04. Общего mandatory per-file регистра нет.
