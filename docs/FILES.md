# Файлы комплекта iEWR

Карта фактического состава этой поставки. Ссылки относительные: они работают после переноса всей папки. Размеры указаны без сжатия; КБ = 1024 байта. Число строк включает пустые строки.

Папки project/source/, project/reference/, project/artifacts/ и project/handoff/ пусты. Они предназначены для материалов и работы нового проекта.

**Корень iEWR/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [AGENTS.md](../AGENTS.md) | Рабочие инструкции агента | 30 | 7,6 |
| [ARCHITECTURE.json](../ARCHITECTURE.json) | Функции, связи и слои архитектуры | 557 | 30,7 |
| [INSTALLATION.json](../INSTALLATION.json) | Состав поставки и SHA-256 файлов | 151 | 5,3 |
| [LICENSE](../LICENSE) | Лицензия MIT для собственных частей iEWR | 21 | 1,1 |
| [ORIGINS.json](../ORIGINS.json) | Источники методов, авторство, точные редакции и SHA-256 | 215 | 19,7 |
| [PACKAGE.json](../PACKAGE.json) | Имя, версия и состав комплекта | 52 | 2,3 |
| [README.md](../README.md) | Назначение и начало работы | 52 | 7,3 |
| [RELEASE_NOTES.md](../RELEASE_NOTES.md) | Содержание и условия поставки | 21 | 3,2 |
| [START.txt](../START.txt) | Короткий вход к AGENTS.md | 1 | 0,2 |
| [STATUS.md](../STATUS.md) | Область проверок и пределы использования | 11 | 2,3 |
**docs/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [BASE_METHODS.md](BASE_METHODS.md) | Прямые FPF-поставщики семи функций | 13 | 0,8 |
| [DPF_CREATION.md](DPF_CREATION.md) | Вход в создание DPF по каноническому FPF | 40 | 10,5 |
| [FILES.md](FILES.md) | Карта фактического состава комплекта | 71 | 5,8 |
| [FPF_INDEX.md](FPF_INDEX.md) | Использование структурного индекса FPF | 41 | 5,8 |
| [IEWR_CONOPS.md](IEWR_CONOPS.md) | Концепция работы среды | 100 | 20,1 |
| [MATERIALS.md](MATERIALS.md) | Роли каталогов и организация материалов | 15 | 1,5 |
| [METHODPACK_CHECK.md](METHODPACK_CHECK.md) | Проверка, подключение и восстановление MethodPack | 56 | 11,7 |
| [METHODS.md](METHODS.md) | Каталог действующих методов | 45 | 6,8 |
| [METHOD_SOURCE_NOTICES.md](METHOD_SOURCE_NOTICES.md) | Авторство, лицензии и статусы источников | 142 | 15,2 |
| [MINI_CONOPS.md](MINI_CONOPS.md) | Краткая архитектура и сценарий работы | 100 | 15,4 |
| [NEW_PROJECT.md](NEW_PROJECT.md) | Начало проекта и перенос существующего | 11 | 2,9 |
| [PROJECT_METHODS.md](PROJECT_METHODS.md) | Применение и развитие репертуара | 17 | 3,3 |
| [SELF_DEVELOPMENT.md](SELF_DEVELOPMENT.md) | Порученное изменение самой среды | 32 | 8,8 |
**external-sources/fpf/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [FPF-Spec.md](../external-sources/fpf/FPF-Spec.md) | Точный оригинал методологической основы FPF | 132247 | 17567,3 |
| [LICENSE](../external-sources/fpf/LICENSE) | Лицензия оригинального FPF | 395 | 18,2 |
| [LICENSING.md](../external-sources/fpf/LICENSING.md) | Условия сторонних материалов FPF | 29 | 3,4 |
| [SOURCE.json](../external-sources/fpf/SOURCE.json) | Редакция, происхождение и digest оригинала FPF | 35 | 2,3 |
**methods/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [METHOD_PACK.md](../methods/METHOD_PACK.md) | Текущая книга 37 прикладных методов | 1347 | 396,9 |
| [index.yaml](../methods/index.yaml) | Поиск точных тел, редакций, условий и связей | 4261 | 197,3 |
**methods/snapshots/base-v3.4/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [METHOD_PACK.md](../methods/snapshots/base-v3.4/METHOD_PACK.md) | Неизменяемый снимок поставляемой книги | 1347 | 396,9 |
| [index.yaml](../methods/snapshots/base-v3.4/index.yaml) | Точный индекс исходной пары снимка | 4261 | 197,3 |
**navigation/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [fpf-index.yaml](../navigation/fpf-index.yaml) | Структурный индекс разделов оригинала FPF | 120985 | 2618,7 |
| [task-entries.yaml](../navigation/task-entries.yaml) | Входы по задачам к исходным методам | 1423 | 52,1 |
**tools/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [build_fpf_index.py](../tools/build_fpf_index.py) | Генерация и проверка структурного индекса FPF | 229 | 9,1 |
| [methodpack.py](../tools/methodpack.py) | Проверка, подключение и восстановление пары MP | 424 | 25,7 |

При развитии проекта эта карта и инвентаризация сохраняют область исходной поставки. Новый состав учитывается по необходимости; история собственного применения начинается с работы проекта.
