# Материалы текущего проекта

| Каталог | Назначение |
|---|---|
| `source/` | Переданные исходные материалы: например, original product ZIP или исходные данные. Сохранять original bytes/provenance, читать in-place |
| `reference/` | Handoff, прежние результаты и материалы сравнения. История источника не является историей текущей инициативы; прежние permissions имеют прежний scope |
| `artifacts/` | Полученные результаты, проверенная candidate поставка и нужное evidence. `process/<initiative>/` создаётся только для реально нужного durable account |

Иные каталоги создавать по фактической потребности. Для persistent DPF discovery
индекс располагается в `project/dpf/REPERTOIRE.yaml`; стандартный внешний DPF
source locus остаётся [source/external-dpf/](../source/external-dpf/), прежний
`project/dpf/` также поддерживается. Перенос или копирование для direct use не
нужны. Помещение DPF в project/source/ само его не регистрирует; текущий
registration consumer имеет свои [допустимые paths](../modules/sources/REGISTRATION.md).

Пустые каталоги не инициируют работу. Наличие файла не даёт authority, не
переключает relied basis и не включает self-development. Поставляется только
этот README и три пустых `.gitkeep`; реальные пользовательские материалы,
baseline ZIP, handoff и development evidence в product inventory не включаются.
