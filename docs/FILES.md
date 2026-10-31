# Файлы комплекта iEWR

Карта фактического состава этой поставки. Ссылки относительные и работают после переноса всей папки. Размеры без сжатия; КБ = 1024 байта. Число строк включает пустые строки.

Папки project/source/, project/reference/, project/artifacts/ и project/handoff/ пусты: материалы и история применения появляются по работе нового проекта.

**Корень iEWR-7.0.1-Eternal-Alpha/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [AGENTS.md](../AGENTS.md) | Рабочие инструкции агента и входы к способам | 40 | 9,5 |
| [ARCHITECTURE.json](../ARCHITECTURE.json) | Семь функций, связи и слои архитектуры | 567 | 31,3 |
| [INSTALLATION.json](../INSTALLATION.json) | Опись поставки, размеры и SHA-256 файлов | 156 | 5,6 |
| [LICENSE](../LICENSE) | Лицензия MIT для собственных частей iEWR | 21 | 1,1 |
| [ORIGINS.json](../ORIGINS.json) | Источники методов, авторство, точные редакции и SHA-256 | 215 | 19,7 |
| [PACKAGE.json](../PACKAGE.json) | Версия, статус и непосредственная основа комплекта | 65 | 3,2 |
| [README.md](../README.md) | Назначение и начало работы | 54 | 9,3 |
| [RELEASE_NOTES.md](../RELEASE_NOTES.md) | Изменения и условия локального кандидата | 17 | 3,0 |
| [START.txt](../START.txt) | Короткий вход к AGENTS.md | 1 | 0,2 |
| [STATUS.md](../STATUS.md) | Область проверок и пределы использования | 17 | 4,3 |

**docs/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [BASE_METHODS.md](BASE_METHODS.md) | Прямые поставщики FPF для семи функций | 13 | 0,8 |
| [DPF_CREATION.md](DPF_CREATION.md) | Вход в создание DPF по каноническому FPF | 40 | 10,5 |
| [FILES.md](FILES.md) | Карта фактического состава и размеров комплекта | 78 | 6,1 |
| [FPF_INDEX.md](FPF_INDEX.md) | Использование структурного индекса FPF | 56 | 11,3 |
| [IEWR_CONOPS.md](IEWR_CONOPS.md) | Концепция работы среды | 102 | 20,8 |
| [MATERIALS.md](MATERIALS.md) | Роли каталогов и входы в организацию материалов | 17 | 1,9 |
| [METHODPACK_CHECK.md](METHODPACK_CHECK.md) | Проверка, подключение и восстановление MethodPack | 60 | 13,2 |
| [METHOD_CATALOG.md](METHOD_CATALOG.md) | Каталог 37 действующих методов | 45 | 7,3 |
| [METHOD_SOURCE_NOTICES.md](METHOD_SOURCE_NOTICES.md) | Авторство, лицензии и статусы источников | 142 | 15,2 |
| [MINI_CONOPS.md](MINI_CONOPS.md) | Краткая архитектура и сценарий работы | 102 | 16,4 |
| [NEW_PROJECT.md](NEW_PROJECT.md) | Начало проекта и перенос существующего | 13 | 3,9 |
| [PORTABILITY.md](PORTABILITY.md) | Возможности и пределы без Python/POSIX | 34 | 8,1 |
| [PROJECT_METHODS.md](PROJECT_METHODS.md) | Применение и развитие репертуара | 19 | 4,1 |
| [SELF_DEVELOPMENT.md](SELF_DEVELOPMENT.md) | Порученное изменение самой среды | 34 | 9,7 |

**external-sources/fpf/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [FPF-Spec.md](../external-sources/fpf/FPF-Spec.md) | Точный неизменённый оригинал FPF | 132247 | 17567,3 |
| [LICENSE](../external-sources/fpf/LICENSE) | Лицензия оригинального FPF | 395 | 18,2 |
| [LICENSING.md](../external-sources/fpf/LICENSING.md) | Условия сторонних материалов FPF | 29 | 3,4 |
| [SOURCE.json](../external-sources/fpf/SOURCE.json) | Редакция, происхождение и контрольная сумма FPF | 35 | 2,3 |

**methods/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [METHOD_PACK.md](../methods/METHOD_PACK.md) | Текущая книга 37 прикладных методов | 1403 | 613,1 |
| [index.yaml](../methods/index.yaml) | Поиск точных тел, редакций, условий и связей | 4274 | 230,1 |

**methods/snapshots/base-v3.10/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [METHOD_PACK.md](../methods/snapshots/base-v3.10/METHOD_PACK.md) | Неизменяемый исходный снимок поставляемой книги | 1403 | 613,1 |
| [index.yaml](../methods/snapshots/base-v3.10/index.yaml) | Точный индекс исходной пары снимка | 4274 | 230,1 |

**navigation/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [fpf-index.yaml](../navigation/fpf-index.yaml) | Структурный индекс разделов оригинала FPF | 120985 | 2618,7 |
| [task-entries.yaml](../navigation/task-entries.yaml) | Входы по задачам к исходным способам | 1423 | 52,2 |

**tools/**

| Файл | Назначение | Строк | КБ |
|---|---|---:|---:|
| [build_fpf_index.py](../tools/build_fpf_index.py) | Генерация и проверка структурного индекса FPF | 229 | 9,1 |
| [methodpack.py](../tools/methodpack.py) | Проверка, подключение и восстановление пары MP | 424 | 25,7 |

Карта и INSTALLATION.json описывают исходную поставку. После развития проекта новый состав учитывается по необходимости; обязательного реестра каждого рабочего файла нет.
