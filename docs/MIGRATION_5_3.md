# Переход с 5.2.2 через линию 5.3 к iEWR 5.5.2 Beta

## С 5.5.1 к 5.5.2

Новая конфигурация содержит 11 DPF: добавлены RMP/SIE/STR, семь прежних
источников получили новую явно закреплённую revision. Не переписывать старые
source bindings и проверки под новые bytes; незатронутые результаты можно
переиспользовать в прежнем scope. Старые публикации сохраняются в исходной
поставке и истории разработки, а не выбираются по дате последнего файла.

Для готового результата на утверждение специалисту агент сразу готовит
переносимый Decision View с материалами. Само представление не вводит gate;
явный выбор человеком иной формы и достаточный текстовый fallback сохраняются.
Старые HTML/ответы не пересобирать поверх прежних. Core, runtime API, схемы и
механизм ответа остаются совместимыми.

## С 5.5.0 к 5.5.1

Исправлены локальные URL новых Decision View, облегчена подача Human Views,
добавлены метка режима, порядок чтения и отдельная техническая трассировка.
Входные schemas/CLI и механизм ответа сохраняются. Новые зависимости не нужны.
Сохранённые HTML и ответы не пересобирать поверх прежних файлов. Если старый
Decision содержит `%5C`, создать новую редакцию с корректными ссылками, сохранив
старую пару вопрос/ответ. Старые ответы не переносятся на новый documentId.

## С 5.4.0 к 5.5.0

Старые вопросы/ответы и JSON/CLI Decision View сохраняются. Human Views добавляют
пять необязательных композиций для чтения, [выбор и сборка](../tools/human_view/README.md).
Обычный разговор достаточен для малого вопроса. Новый стиль применяется при
новой сборке; прежние snapshots не переписывать. Review/Result не означают
приёмку и не создают ответа. Core/runtime API и состав DPF не меняются.


Новая candidate-конфигурация развивает Human–AI инструкции, обновляет пять и добавляет два
авторских DPF и меняет публичный путь внешних проектных источников. Core Contract
1.0 RC, functional DAG, direct authority, существующие runtime schemas и локальный
экспериментальный SDLC не меняются. Minor version отражает новые доступные
contributions и миграцию пути; это не новая архитектура и не приёмка.

## Дополнение 5.4

Необязательный список ожидаемых решений не требует преобразования прежних
вопросов, ответов или owner records. Для его использования подготовить явную
проекцию по [руководству](../tools/decision_view/README.md#список-ожидаемых-решений).
Старые Decision Views продолжают использоваться. При отказе от списка достаточно
вернуться к ним; история ответов и фактические эффекты сохраняются. Снимок списка
не переносит согласие на изменённый вопрос и не возобновляет действие сам.

## Каталог внешних источников

Новый root — `external-sources/`, стандартный DPF locus —
`external-sources/external-dpf/`. `project/source/` по-прежнему хранит входящие
материалы проекта. `project/dpf/REPERTOIRE.yaml` остаётся repertoire writer locus;
старый допустимый source locus `project/dpf/` сохраняется.

Для разрешённой миграции сохранить source bytes и прежний repertoire, перенести
корневой каталог целиком, изменить current source_locus/normative_loci и loci
source claims в project repertoire, затем сверить SHA-256 и фактическое чтение.
Не менять source identity/edition/digest только из-за нового адреса. Исторические
bindings и решения не переписываются; старая source basis восстанавливается по
прежнему сохранённому комплекту и mapping old→new. Неизвестный внешний consumer
остаётся явно непроверенным; historical paths не считаются current roots.

Новая регистрация принимает новый root; `source/external-dpf/` отвергается.
Package helper читает старый scaffold только внутри historical ZIP для diff,
не включает произвольные внешние DPF в новую поставку. Подключение источника
по-прежнему не создаёт permission, applicability или execution.

## Перенос полезного legacy

Два корневых guide исключены из чистого комплекта после сверки вкладов. Они
доступны в неизменном исходном ZIP 5.2.2 и history проекта разработки. Старые
пути читаются как historical references; на новой поставке используются owners:

| Legacy вклад | Current locus |
| --- | --- |
| Formation, first useful result, adequate reuse, Method question, optional WorkPlan | [F](../modules/formation/DOMAIN_WORK.md) |
| Bounded source set, contributions, conflicts, source change, registration | [S](../modules/sources/GUIDANCE.md), [registration](../modules/sources/REGISTRATION.md) |
| Scope, permission, authority, competence, conditional response | [G](../modules/governance/GUIDANCE.md) |
| Direct execution, formal Work order, readiness, profiles, steering, provider mapping | [X](../modules/execution/EXECUTION_BASIS.md) |
| Technical boundary, effects, recovery before retry | [E](../modules/effects/GUIDANCE.md), [R](../modules/recovery/CONTRACT.md) |
| Conditional Verification, evidence, decision, actual reliance | [L](../modules/reliance/RECEIVING_USE.md) |
| Human interaction, view, material disclosure, optional carriers | [I](../modules/interaction/HUMAN_INTERACTION.md), [Decision View](../modules/interaction/DECISION_VIEW.md) |

Рабочий процесс/Working Process — optional derived view по действующим direct
grounds, не новый owner, Method, WorkPlan или authority. Legacy Loop может быть
кандидатным описанием способа только по содержанию; Task — request/intended-item
carrier; Run — запись execution; Candidate — label unresolved use. Admission
record отражает прежнее exact решение, а Relied-on — конкретный receiving use.
Ни filename, ни status не устанавливают FPF kind. CAP — прежний alias bounded
profile без grant; STATE_INDEX — необязательная навигация, stale игнорируется.
Массовая конверсия истории и повторный Admission не требуются.

Каталоги engineering views и working-process cues, их optional templates и
CONTRACT B1 сохранены: они дают ограниченные вопросы, интерфейсные references
и compatibility content, а не обязательный lifecycle. Их historical citations
не становятся актуальным endorsement; source access — по S. Отдельный общий
registry, scheduler, automatic successor и обязательный review не добавлены.
