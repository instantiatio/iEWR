# iEWR 5.2.1-beta — candidate для Human acceptance

Исходный baseline — принятая локальная 96-file поставка iEWR 5.2.0-beta.
ZIP SHA-256: `3d6eb16840e1d36b48825bced4f880eb23bda713d7de60925cb4c1c045db0f1d`.
Принятые ZIP и evidence сохранены неизменными. Candidate labels внутри прежнего
snapshot описывают момент его подготовки; последующее принятие записано отдельно.
Новая поставка ещё не принята. `distribution_ready=false`, Closed Beta,
not a public release; GitHub publication не выполнялась.

## Изменение и совместимость

[I](modules/interaction/HUMAN_INTERACTION.md) уточняет ожидание без нового
результата, своевременное предъявление существенных допущений, возможности
вмешательства host, проверяемое основание и вклад выбранного источника,
decision-changing unknown и различие содержания/формы. Сохраняется соразмерная
подача без обязательного вступления, timer, response template или новых согласований.

[Поддержка саморазвития](modules/self_development/GUIDANCE.md) добавляет короткий
критерий проверки content/form; он действует только при explicit развитии iEWR.
Ordinary tasks не получают процедуру исследования, acceptance или package lifecycle.

Core Contract 1.0 RC, owner APIs, Python code, import DAG, runtime semantics,
adapters и source-selection S/F сохранены. Нет нового состояния, workflow engine,
прямого I → X/E, DPF routes, universal Verification → Human Admission или
обязательных ladders. Bundled DPF/licensing/local SDLC не менялись; overlap audit
не начинался. Inventory остаётся 96 files.

**5.2.1-beta** — patch к уже введённому в 5.2.0 поведению: адресные уточнения
инструкций и способа их проверки, без новой capability/API или Core semantics.
Version metadata в AGENTS/README/manifest/configuration согласованы с новым
предметом; discovery routing не менялся. В принятой 5.2.0 configuration поля
version/package_id/source_baseline_id оставались от прежнего выпуска. В новой
конфигурации это исправлено; hashes прежних bytes и принятие не переписаны.

## Qualification этой конфигурации

Выполнены четыре fresh-context initial tasks: один accepted-baseline comparator
и три candidate cases; два уточнения доставлены во время active turns, один
отдельный follow-up проверил resume. Наблюдены раннее допущение, смена направления,
проверяемый итог, простая правка без self-development и explicit proposal-only
развитие без реализации. Оба инженерных прототипа прошли по 20 собственных
локальных tests; parent независимо проверил семь свойств итоговых данных.
Failures и их разрешение сохранены в evidence. Это bounded interaction cases,
не production qualification импортёра и не семь независимых trials.

Семь affected helper regression cases прошли; final selected package проверяется
из чистой extraction с теми же runtime bytes. Проверены configuration/import DAG,
точный 7-file delta, согласованность version metadata, inventory/manifest hashes,
owned links и полный текст при renderer loss. Final status/hash metadata имеет
отдельный byte bridge к trial; behavior instructions не менялись.

В B между существенными сообщениями наблюдалась пауза 3 мин 52 с; у comparator
4 мин 56 с. Поэтому устойчивое сообщение при долгом ожидании не квалифицировано;
универсальная cadence, causal superiority и удобство для человека не заявлены.
Обе конфигурации дали достаточные инженерные решения. Представления отдельно
проверены прямой сверкой claims; выигрыш формы не приписан новым условиям.
Исследование и разбор прежних traces не подтвердили универсальное молчание до
финала. Подтверждены более узкие пробелы явности инструкции и evidence о ходе
длительной работы, вмешательстве и отдельном влиянии содержания/формы.
Доказательства прежней 5.2.0 сохраняют прежний scope и не объявляются новыми runs.

## Сохранённые пределы

Instruction-led агент на cooperative local host использует доступные tools и
прямые основания действий. Текст инструкции не обеспечивает поведение любого
host/model; no scheduler и нет гарантии немедленного получения вмешательства
во время blocking tool call. Human usability, causal superiority, general
transfer и полный host matrix не устанавливаются несколькими agent observations.
Подлинные Human review и acceptance отдельны от agent/fixture evidence.

Portable maintainer checks на Windows не квалифицируют POSIX no-follow/flock
runtime adapter. Live JSON direct-channel authentication, unattended E.16,
hostile-writer/ABA enforcement и external consumers не квалифицированы.
Source remote anchors и full domain/FPF conformance этим изменением не проверяются.
Frozen source links имеют исходный scope; owned packaged links проверяются отдельно.

Пять upstream DPF имеют прежнюю exact CC BY 4.0 licensing basis с third-party
boundaries; local SDLC остаётся experimental project-authored local trial.
Это не whole-package distribution readiness. Historical decisions, gaps и
failed attempts сохраняются в исходном evidence. Exact состав —
[PACKAGE_MANIFEST](PACKAGE_MANIFEST.md); identities и результаты проверки
предъявляются вне product payload вместе с новой поставкой.
