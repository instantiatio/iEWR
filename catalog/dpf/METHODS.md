# Указатель DPF и методов

Один вход для выбора предметной основы: текущий вопрос → подходящий DPF →
метод → нужный раздел оригинала. В указателе все 123 именованных метода шести
встроенных редакций. Тексты методов остаются в DPF; отдельные карточки не входят
в поставку и не создаются при чтении или подключении источника.

## Как обращаться к DPF

1. Определить вопрос и первый нужный результат. Рассмотреть все подходящие DPF,
   включая внешние источники проекта; порядок строк не задаёт приоритета.
2. Найти метод по вопросу или авторскому обозначению. Перейти к точному разделу
   исходника, прочитать действия, существенные условия, ограничения и критерий
   достаточного результата; при необходимости — примеры и связанные разделы.
   Сделать это до рекомендации, включая промежуточное сообщение о ходе работы.
3. Применить подходящий вклад по существу. Указатель и совпадение названия
   не доказывают пригодности метода. Недостающие условия не восстанавливать
   догадкой и не переносить из другого метода.
4. На проверенной неизменной основе использовать уже прочитанное повторно.
   Новая редакция, изменившийся вопрос или пробел требуют проверки затронутой
   части; весь DPF и весь набор источников читать не требуется.

Выбор и применение задаёт [F](../../modules/formation/DOMAIN_WORK.md), точные
источники и достаточное чтение — [S](../../modules/sources/GUIDANCE.md).
Авторская ссылка на FPF не разрешает полное или транзитивное чтение FPF-Spec.

## Выбор предметной области

| Текущий вопрос | DPF и полезный вклад | Методов |
|---|---|---:|
| Какую систему создать или изменить; как связать устройство, реализацию и проверки? | [SYSE](#syse): системная инженерия, архитектура, интерфейсы, интеграция и инженерное обеспечение | 41 |
| Как выбрать, описать, проверить или улучшить способ работы? | [ME](#me): требования к методу, пригодность, описание, доступ к источникам и проверка применения | 24 |
| Как изменить организацию, распределение вкладов, назначения и обеспечивающие связи? | [OCE](#oce): организационные изменения; схема, доступ и назначение не доказывают фактического вклада или полномочий | 17 |
| Как поставить проблему, сравнить варианты и подготовить рекомендацию? | [PSD](#psd): границы вопроса, альтернативы, последствия и неопределённость; решение остаётся у получателя | 17 |
| Как вести текущую деятельность при очередях, ограничениях и обязательствах? | [OPS](#ops): продолжение случаев, сроки, располагаемая мощность и улучшение операций | 20 |
| Где реализовано поведение программы; как изменить, диагностировать или перестроить код? | [SDLC](#sdlc): четыре ограниченных вопроса о коде; экспериментальная локальная редакция | 4 |

## Внешние источники и редакции

Полный доступный состав устанавливается реестрами источников:
frameworks/dpf/REPERTOIRE.yaml и существующим project/dpf/REPERTOIRE.yaml.
Внешние DPF рассматриваются наравне со встроенными; отсутствие строки здесь
не означает отсутствия подходящего метода. Указанный пользователем источник
можно читать напрямую без регистрации.

При постоянном подключении дополняется один существующий проектный указатель;
если его нет, используется project/artifacts/dpf/GUIDE.md. Для каждой редакции
сначала проверяются авторское оглавление и его полный охват. При достаточной
навигации нужны точная привязка, краткие предметные вопросы и одна ссылка на
это оглавление с явным охватом. Собственный полный перечень нужен лишь при
конкретном пробеле авторской навигации.
Не создавать файл на каждый DPF или метод и не копировать тела паттернов.
Обычное подключение внешнего DPF не изменяет поставляемый указатель.
Границы записи, повторное подключение и обновление —
[правила регистрации](../../modules/sources/REGISTRATION.md).

Вопросы ниже взяты из авторской навигации; язык и PatternID сохранены для
точного поиска. Если отдельного вопроса нет, приведено название метода.
Происхождение: составление и навигационная адаптация iEWR, 11.09.2026,
по закреплённым редакциям Anatoly Levenchuk. Исходные тексты и статус не изменены.
Авторские SYSE/ME/OCE/PSD/OPS — Eternal alpha, CC BY 4.0; SDLC 0.1.0 —
экспериментальная локальная редакция. Уведомления и границы лицензий —
[NOTICE](../../frameworks/dpf/NOTICE.md). Контрольная сумма связывает редакцию,
но не доказывает пригодности её утверждений.

## SYSE

Источник: [systems-engineering](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#table-of-contents).
Редакция: 2026-09-05-rev-d514a6fc; SHA-256: 45c49096102c11c7ac1024e3b459f7b9e791c48613163af46f2d63cfdf579887.
Охват: все 41 именованных методов авторского оглавления.
Вопрос ниже — точная авторская поисковая формулировка; если отдельного вопроса нет, название метода.
Рассматривать метод при таком вопросе; необходимые условия и ограничения — по ссылке в строке.

| Метод | Вопрос / ситуация для рассмотрения | Полный исходный раздел |
|---|---|---|
| SYSE.1 | Which System is this project actually changing or bringing about? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse1---choose-and-reopen-the-project-system-of-interest) |
| SYSE.16 | Which surrounding Systems and conditions matter to this use decision? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse16---recover-the-systems-and-conditions-needed-for-a-use-decision) |
| SYSE.17 | Who or what may undergo a consequence of this engineering change? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse17---find-systems-that-may-bear-engineering-consequences) |
| SYSE.2 | How will this System be used in a concrete situation? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse2---develop-linked-use-and-system-concepts) |
| SYSE.22 | How should the problem change when a prototype or operating observation reveals a new possibility? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse22---coevolve-engineering-problems-and-system-family-options) |
| SYSE.5 | Which different organizations could produce the required outside effect? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse5---develop-functional-organization-and-bearer-alternatives) |
| SYSE.6 | Which engineering architecture should the project choose for this use? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse6---decide-and-reopen-the-engineering-architecture) |
| SYSE.7 | Which claims across our models and records support this decision? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse7---maintain-a-decision-usable-engineering-description-ensemble) |
| SYSE.8 | What continuing arrangement makes this engineered result usable? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse8---develop-an-integrated-offering-and-provider-concept) |
| SYSE.9 | Which exact specialist answer could change this whole-System decision? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse9---request-and-use-specialist-engineering-results) |
| SYSE.10 | What can this research, model, or trial result support in our engineering decision? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse10---assess-research-model-and-trial-results-for-an-engineering-decision) |
| SYSE.24 | How can the project obtain the same needed engineering result in different ways? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse24---choose-how-the-project-will-obtain-a-needed-engineering-result) |
| SYSE.3 | Which Systems and Work can realize the selected architecture? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse3---develop-the-recursive-realization-network) |
| SYSE.11 | Which actual configuration is usable for the intended purpose now? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse11---integrate-a-system-for-one-bounded-use) |
| SYSE.12 | What must enable the engineers' actual modeling, building, testing, release, and observation Work? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse12---develop-an-engineering-platform-for-practitioner-work) |
| SYSE.18 | How can Systems governed by different Agents work together for this use? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse18---integrate-systems-governed-by-different-agents) |
| SYSE.23 | What should we change now so valuable later changes become easier? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse23---choose-what-to-change-so-later-system-changes-become-easier) |
| SYSE.13 | Which actual or proposed configuration does this claim concern? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) |
| SYSE.14 | What may be released for which named Work or use? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse14---make-a-release-decision-for-named-engineering-work-or-use) |
| SYSE.19 | Which engineering decisions relied on the claim that changed? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse19---revalidate-engineering-decisions-when-a-relied-on-source-changes) |
| SYSE.4 | Which challenge could change reliance on this engineering claim? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse4---select-an-engineering-challenge-and-qualify-evidence-use) |
| SYSE.15 | Which engineering Methods are needed to obtain this project's results? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse15---choose-and-refresh-the-engineering-methods-needed-by-a-project) |
| SYSE.20 | Which modeling, implementation, trial, and review Work can overlap? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse20---reconcile-overlapping-engineering-work-and-required-order) |
| SYSE.21 | Should this engineering practice continue, change, branch, or stop across the relevant population? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse21---deliberately-continue-and-change-systems-engineering-culture) |
| SYSE.25 | Which platform difficulty should we address next? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse25---choose-a-platform-improvement-from-practitioner-task-evidence) |
| SYSE.26 | What must the user supply to obtain a usable engineering result? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse26---design-a-supported-platform-use-path) |
| SYSE.27 | Does this change preserve the consumer's promised result? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse27---evolve-platform-interfaces-and-contribution-paths) |
| SYSE.28 | Where can this property change before it is relied on? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse28---place-qualified-controls-in-a-supported-path) |
| SYSE.29 | Can users complete the required work through the receiving path? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse29---migrate-and-retire-a-supported-platform-path) |
| SYSE.30 | Which inputs produced the tested artifact? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse30---make-software-builds-repeatable-and-traceable) |
| SYSE.31 | Does this green check answer the current engineering question? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse31---keep-software-feedback-fast-and-trustworthy) |
| SYSE.32 | Does the received package still carry the tested artifact's evidence? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse32---promote-verified-artifacts-without-rebuilding) |
| SYSE.33 | Can another user reconstruct an environment that actually supports this task? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse33---provide-reconstructible-development-and-test-environments) |
| SYSE.34 | Can old and new software safely use the same changing data? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse34---change-software-and-persistent-data-with-a-recovery-boundary) |
| SYSE.35 | What evidence justifies widening use of a deployed candidate? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse35---control-release-exposure-with-user-relevant-signals) |
| SYSE.36 | Does this measurement count successful user tasks or only healthy components? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse36---measure-user-tasks-and-set-software-service-reliability-objectives) |
| SYSE.37 | Does this reliability signal require action soon enough to justify an alert? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse37---alert-on-actionable-reliability-risk) |
| SYSE.38 | Which stage of this user attempt failed, and what can restore useful work now? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse38---diagnose-and-restore-a-failed-platform-task) |
| SYSE.39 | Will this change reduce total work or move it to users? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse39---reduce-repetitive-platform-work-without-moving-the-burden) |
| SYSE.40 | Which shared limit lets one workload delay or disable another? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse40---protect-software-platform-capacity-and-isolate-failure) |
| SYSE.41 | Did the intended software and configuration become usable on each target? | [Исходный раздел](../../frameworks/dpf/systems-engineering/2026-09-05-rev-d514a6fc/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse41---deploy-a-verified-software-configuration-and-handle-partial-failure) |

## ME

Источник: [method-engineering](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#table-of-contents).
Редакция: 2026-09-05-rev-d514a6fc; SHA-256: cc9056e958c0435ec33666291f6fa4bb207d5e307ae6b28213f134f74d92bef4.
Охват: все 24 именованных методов авторского оглавления.
Вопрос ниже — точная авторская поисковая формулировка; если отдельного вопроса нет, название метода.
Рассматривать метод при таком вопросе; необходимые условия и ограничения — по ссылке в строке.

| Метод | Вопрос / ситуация для рассмотрения | Полный исходный раздел |
|---|---|---|
| ME.1 | What needs to change when the team says its methodology is failing? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me1---choose-and-reopen-the-project-method-of-interest) |
| ME.19 | Why did this profession acquire these different Methods and arrangements? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me19---recover-why-and-how-a-professional-method-architecture-differentiated) |
| ME.2 | What usable Methods and candidate accounts are hidden across our manuals, tools, and remembered practice? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me2---recover-a-reusable-method-repertoire-and-its-lineages) |
| ME.18 | What way of working can we reconstruct from incomplete and conflicting records? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me18---reconstruct-a-candidate-method-account-from-observed-work) |
| ME.3 | What must this Method contribute in this project situation? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me3---build-situational-method-requirements-and-fit-criteria) |
| ME.4 | Which useful contributions are hidden in this source or plural library? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me4---recover-methods-and-decision-relevant-contributions-from-documentary-packages-and-corpora) |
| ME.5 | Which individual candidate is usable for this bounded result? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me5---qualify-individual-methods-candidate-accounts-and-local-connections) |
| ME.6 | How do plausible Methods interact when their enactment overlaps? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me6---compare-method-architecture-alternatives-and-simultaneous-enactment-conflicts) |
| ME.7 | Does the proposed Method whole already exist through obtaining relations? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me7---resolve-a-proposed-method-whole-into-obtaining-relations-or-a-candidate-account) |
| ME.8 | Which Method claims does this user need for this action? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me8---author-a-methoddescription-for-named-uses) |
| ME.9 | How should performers, method engineers, support builders, and assessors see different claims about the same Method? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me9---compose-complementary-method-representations-for-their-uses) |
| ME.22 | Did the new guide add needed content, improve its presentation, or change both? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me22---compare-method-descriptions-by-content-and-representation) |
| ME.10 | Can named users find and use the right Method material for their actual tasks? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me10---build-a-method-base-and-enactment-support-arrangement) |
| ME.11 | What happened when this Method was tried in actual Work? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me11---trial-the-method-in-representative-work) |
| ME.12 | Which relied-on Method claim fails to agree with its description, representation, or supporting material? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me12---verify-method-and-methoddescription-coherence) |
| ME.13 | Does this Method fit the situation in which we need it? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me13---validate-situational-fit-and-transfer) |
| ME.14 | Is this Method worth its total burden compared with current alternatives? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me14---evaluate-practical-worth-against-current-alternatives) |
| ME.15 | Did this change alter a reusable way of working or only its description and support? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me15---maintain-method-variants-provenance-and-reuse) |
| ME.16 | What changed when this Method was introduced into a real practice? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me16---introduce-observe-and-revise-a-method-in-practice) |
| ME.17 | Which cultural relation should deliberately continue or change across this practitioner population? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me17---deliberately-continue-and-change-method-engineering-culture) |
| ME.21 | What should survive from these partly agreeing sources, and where should it live? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me21---reconcile-and-allocate-source-contributions-after-exact-subtraction) |
| ME.23 | How should these description contributions form a useful language? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me23---architect-a-problem-first-methoddescription-pattern-language) |
| ME.24 | Can this language reconstruct the action and stop it promises from the source? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me24---falsify-and-refresh-source-to-pattern-coverage-by-reconstruction) |
| ME.20 | Which pattern contribution can supply the Method Engineering result needed now? | [Исходный раздел](../../frameworks/dpf/method-engineering/2026-09-05-rev-d514a6fc/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me20---use-pattern-language-knowledge-to-continue-situated-method-engineering) |

## OCE

Источник: [organization-change-engineering](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#table-of-contents).
Редакция: 2026-09-05-rev-d514a6fc; SHA-256: a7ab62df62afe22086165830d0c91bf04c43d07437431f7d6944c571894da5ac.
Охват: все 17 именованных методов авторского оглавления.
Вопрос ниже — точная авторская поисковая формулировка; если отдельного вопроса нет, название метода.
Рассматривать метод при таком вопросе; необходимые условия и ограничения — по ссылке в строке.

| Метод | Вопрос / ситуация для рассмотрения | Полный исходный раздел |
|---|---|---|
| OCE.1 | Identify the Changed Organization and Intended Contribution | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce1---identify-the-changed-organization-and-intended-contribution) |
| OCE.2 | Recover Current Organization Work and Arrangement | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce2---recover-current-organization-work-and-arrangement) |
| OCE.3 | Generate and Compare Organization Concepts | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce3---generate-and-compare-organization-concepts) |
| OCE.4 | Design Contribution Architecture | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce4---design-contribution-architecture) |
| OCE.5 | Define Organization Positions | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce5---define-organization-positions) |
| OCE.6 | Establish Holder Assignments and Enabling Relations | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce6---establish-holder-assignments-and-enabling-relations) |
| OCE.7 | Coordinate Product-or-Service and Organization Architecture Decisions | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce7---coordinate-product-or-service-and-organization-architecture-decisions) |
| OCE.8 | Configure Human–AI, Robotic, and Provider Work Arrangements | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce8---configure-humanai-robotic-and-provider-work-arrangements) |
| OCE.9 | Realize a Bounded Organization-Capability Increment | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce9---realize-a-bounded-organization-capability-increment) |
| OCE.10 | Diagnose Participation and Change Target Working Culture | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce10---diagnose-participation-and-change-target-working-culture) |
| OCE.11 | Coordinate Change Work with Continuing Service | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce11---coordinate-change-work-with-continuing-service) |
| OCE.12 | Distribute Leadership Contributions in Organization Change | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce12---distribute-leadership-contributions-in-organization-change) |
| OCE.13 | Observe and Compare Organization-Change Consequences | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce13---observe-and-compare-organization-change-consequences) |
| OCE.14 | Revise the Organization from Qualified Results | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce14---revise-the-organization-from-qualified-results) |
| OCE.15 | Develop and Refresh Organization-Change Methods | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce15---develop-and-refresh-organization-change-methods) |
| OCE.16 | Reconcile Simultaneous Organization-Change Work | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce16---reconcile-simultaneous-organization-change-work) |
| OCE.17 | Continue and Renew Organization-Change Engineering Practice | [Исходный раздел](../../frameworks/dpf/organization-change-engineering/2026-09-05-rev-d514a6fc/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce17---continue-and-renew-organization-change-engineering-practice) |

## PSD

Источник: [problem-structuring-decision-support](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#table-of-contents).
Редакция: 2026-09-05-rev-d514a6fc; SHA-256: dbf0f86337d24dcb89d90faa38240991579b9fe6d1487120285c36126673efa9.
Охват: все 17 именованных методов авторского оглавления.
Вопрос ниже — точная авторская поисковая формулировка; если отдельного вопроса нет, название метода.
Рассматривать метод при таком вопросе; необходимые условия и ограничения — по ссылке в строке.

| Метод | Вопрос / ситуация для рассмотрения | Полный исходный раздел |
|---|---|---|
| PSD.1 | Bound the Decision-Support Engagement and Authority Boundary | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-1) |
| PSD.2 | Recover Participants, Concerns, and Affected Systems | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-2) |
| PSD.3 | Generate Plural Problem Formulations | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-3) |
| PSD.4 | Set and Reopen the Problem Boundary | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-4) |
| PSD.5 | Construct Complementary Situation and Option Models | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-5) |
| PSD.6 | Select and Combine Problem-Structuring Methods | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-6) |
| PSD.7 | Facilitate Inquiry and Preserve Material Dissent | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-7) |
| PSD.8 | Generate Decision Alternatives | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-8) |
| PSD.9 | Represent Values and Trade-Offs | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-9) |
| PSD.10 | Represent Decision-Relevant Uncertainty and Evidence Limits | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-10) |
| PSD.11 | Compare Consequences | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-11) |
| PSD.12 | Test Robustness and Sensitivity | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-12) |
| PSD.13 | Prepare and Return a Decision-Support Recommendation | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-13) |
| PSD.14 | Prepare and Use a Decision Follow-up Arrangement | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-14) |
| PSD.15 | Develop and Refresh Problem-Structuring and Decision-Support Methods | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-15) |
| PSD.16 | Reconcile Simultaneous Problem-Structuring and Decision-Support Work | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-16) |
| PSD.17 | Deliberately Continue and Change Problem-Structuring and Decision-Support Culture | [Исходный раздел](../../frameworks/dpf/problem-structuring-decision-support/2026-09-05-rev-d514a6fc/PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-17) |

## OPS

Источник: [operations-management](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#table-of-contents).
Редакция: 2026-09-05-rev-d514a6fc; SHA-256: 5d2ff495c0a6fff809092c8e36c826ae3a6d94860cf58d63ef61a41feaeedd87.
Охват: все 20 именованных методов авторского оглавления.
Вопрос ниже — точная авторская поисковая формулировка; если отдельного вопроса нет, название метода.
Рассматривать метод при таком вопросе; необходимые условия и ограничения — по ссылке в строке.

| Метод | Вопрос / ситуация для рассмотрения | Полный исходный раздел |
|---|---|---|
| OPS.1 | Identify the Operating System, Commitments, and Flow Units | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-1) |
| OPS.2 | Select the Work-Management Mode | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-2) |
| OPS.3 | Distinguish Operating Subjects, Cases, Queues, Resources, and Records | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-3) |
| OPS.4 | Maintain Shared Attention to Current Subject State | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-4) |
| OPS.5 | Admit Work and Limit Starts | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-5) |
| OPS.6 | Continue Cases and Handle Exceptions | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-6) |
| OPS.7 | Manage Aging, Urgency, and Service Commitments | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-7) |
| OPS.8 | Coordinate Queues and Buffers | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-8) |
| OPS.9 | Diagnose and Treat the Current Constraint | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-9) |
| OPS.10 | Qualify Capacity Under Variability | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-10) |
| OPS.11 | Coordinate Interacting Operating Structures | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-11) |
| OPS.12 | Protect Human Conditions in Operating Decisions | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-12) |
| OPS.13 | Align Commitments, Resources, and Service Outcomes | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-13) |
| OPS.14 | Relate Throughput, Cash, and Operating Consequences | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-14) |
| OPS.15 | Build a Decision-Specific Operating Account | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-15) |
| OPS.16 | Improve the Operating Method from Evidence | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-16) |
| OPS.17 | Compare and Refresh Operations Methods | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-17) |
| OPS.18 | Control Operating Quality and Reliability | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-18) |
| OPS.19 | Reconcile Simultaneous Operating Work Across Cases and Scales | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-19) |
| OPS.20 | Deliberately Continue and Change Operations Culture | [Исходный раздел](../../frameworks/dpf/operations-management/2026-09-05-rev-d514a6fc/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops-20) |

## SDLC

Источник: [sdlc](../../frameworks/dpf/sdlc/0.1.0/SDLC_DPF.md#table-of-contents).
Редакция: 0.1.0; SHA-256: eb6e5b1e69ee8192fbcd73acf05bca3484ac2637f79abb810e63d06e3a25f7da.
Охват: все 4 именованных методов авторского оглавления.
Вопрос ниже — точная авторская поисковая формулировка; если отдельного вопроса нет, название метода.
Рассматривать метод при таком вопросе; необходимые условия и ограничения — по ссылке в строке.

| Метод | Вопрос / ситуация для рассмотрения | Полный исходный раздел |
|---|---|---|
| SDLC.1 | Восстановить, как нужное поведение реализовано в коде | [Исходный раздел](../../frameworks/dpf/sdlc/0.1.0/SDLC_DPF.md#sdlc-1) |
| SDLC.2 | Реализовать одно согласованное изменение программы | [Исходный раздел](../../frameworks/dpf/sdlc/0.1.0/SDLC_DPF.md#sdlc-2) |
| SDLC.3 | Локализовать воспроизводимый программный дефект | [Исходный раздел](../../frameworks/dpf/sdlc/0.1.0/SDLC_DPF.md#sdlc-3) |
| SDLC.4 | Изменить внутреннюю структуру с сохранением поведения | [Исходный раздел](../../frameworks/dpf/sdlc/0.1.0/SDLC_DPF.md#sdlc-4) |
