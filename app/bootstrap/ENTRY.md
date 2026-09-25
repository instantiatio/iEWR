# Явный bootstrap entry

## Необязательная read-only проверка Recovery

Для обычной работы по `AGENTS.md` этот entry и его schema-2 records не обязательны.
Python 3.10+ нужен только для явного программного вызова helper. Сведения без
машинных bindings могут быть отдельно проверены по [R](../../modules/recovery/CONTRACT.md);
отсутствие JSON не требует автоматической миграции или нового Human approval.

`recovery.py` связывает qualified P reader с C → R assessment. Не импортирует
POSIX Tree/actuator, не пишет records и не выполняет action. Python 3.10+:

```text
python -I -S -B -X utf8 app/bootstrap/recovery.py --workspace ABSOLUTE_ROOT --binding project/artifacts/process/INITIATIVE/reentry-v1.json --binding-sha256 EXACT_SHA256 --direct-channel-basis QUALIFIED_CHANNEL_REF
```

stdin: JSON `{ "context": CONTEXT, "observations": NORMALIZED_HOST_RECORDS }` из
доверенного host reader. Exit 0 означает полученный non-hold assessment, не
permission; exit 2 — hold. stdout — schema 2, disposition, selection/use, three
accounts, holds, observed refs, assessment digest и `actuation_grant:false`.
Неверный hash/контекст/схема/отсутствующее основание не исправляются автоматически.

Шаблон envelope — [REENTRY_BINDING_TEMPLATE](../../templates/REENTRY_BINDING_TEMPLATE.json).
Exact ref: `{ "locus": "relative/path", "sha256": "..." }` либо
`{ "host_event": 335, "sha256": "..." }`. Context содержит `host`, absolute
`workspace`, `session`, `lineage`, integer `through_seq`. Evidence port обязан
наблюдать этот context независимо от envelope. Direct file JSON не Human channel.

Минимальные schema-2 owner records, referenced envelope:

| Record | Поля сверх `schema:2` |
|---|---|
| Candidate | `kind:initiative`, `initiative`, `use`, `request_ref` direct Human |
| Coverage | `kind:coverage`, `context`, `complete:true`, `unsearched:[]` — qualified coverage judgment |
| Selection | `owner:G`, `kind:selection`, `initiative`, `use`, `context`, `direct_ref`, `exact_text` |
| G account | `owner:G`, тот же initiative/use/context, `current:true`, `selection_ref`, `direct:[{kind,ref,exact_text,question_ref}]`, `scope:{allowed:[],prohibited:[]}`, `relied_refs` exact и в порядке F bindings |
| Relied basis | `owner:F`, тот же initiative/use/context, `bindings:[{ref,receiving_use}]` |
| Facts | `owner:X/E`, тот же initiative/use/context, `complete:true`, `unsearched:[]`, `records:[{action_id,outcome,intent_ref,attempt_ref,observation_refs}]`, `disposition`, `next_action_ref` |
| Intent | `owner:X`, та же initiative, original use/context с cut не позже текущего, `action_id`, exact `attempt_ref` |
| Observation | `owner:E`, та же initiative и original use этого intent, original context с cut не позже текущего, `kind:effect_observation`, `action_id`, `attempt_ref`, `outcome`, непустые `observed_refs` на независимые наблюдения/bytes |
| Pending action | `owner:X`, тот же initiative/use/context, `kind:intended_action`, новый `action_id`, `status:not_attempted`, exact `governance_ref`/`basis_ref` |

Facts outcomes: `applied`, `not_performed`, `reconciled`; прочие требуют отдельного
reconciliation. Completed не имеет next action. Pending требует отдельно bound
not-attempted intended action и не переиспользует ID прежней попытки. Historical
owner records сохраняются; если нужна current-use projection, она ссылается на
исторические основания, не переписывая их. Не заполнять records invented grants.
Direct relation `kind` — `request` либо `answer`; для ответа обязателен exact
`question_ref`. `relied_refs` связывает G assessment с проверенными редакциями,
не означает Human approval каждого Method/source. Пустые factual records требуют
отдельный `no_effects_basis_ref`; сама пустота не доказывает отсутствия effects.
Исторические intent/observation не переписываются на current use/cut. В v1 их
host/workspace/session/lineage должны совпадать с current context; перенос между
hosts/forks без qualified lineage relation удерживается, не выводится из имени.

Проверка bytes/relations не аутентифицирует supplied owners и не решает смысл
произвольных Human слов. Эти premises устанавливаются caller вне модели. `discover_reentry`
читает только explicit project carrier loci; Markdown/source нельзя механически
превратить в governing history. Ширина supplied loci не доказывает completeness.

Helper не подключается к агенту автоматически и не перехватывает инструменты.
Caller сам подготавливает context/observations из независимо установленного
источника; model-authored JSON и название host такой источник не квалифицируют.
Вызов helper не выдаёт разрешения независимо от exit code.

Ограничение schema-2 v1: `kind:continuation` не принимает текущее сообщение
одновременно за request и selection; для этого входа selection должен ссылаться
на предшествующее exact direct сообщение Human. Это ограничение helper, не запрет человеку
явно выбрать инициативу текущим сообщением в обычной работе. Нельзя подставлять
фиктивный `new_question`, seq или Human ответ ради PASS; использовать отдельную
instruction-led проверку исходных оснований либо вернуть точный blocker.

## Существующий operation entry

В продукт входит `operation.py`: одна requested source-registration или
exact-artifact operation с явно заданным workspace и independently established
direct decision/Method bindings. One call, no queue, no decision generation,
no automatic retries. `--adapter` выбирает technical operation port, не DPF route.

`operation.py` требует serialized OperationBasis на stdin, decision path + exact
hash, method path и direct channel basis ref. Host/agent предварительно
устанавливает direct source и scope по G guidance; parameter не аутентифицирует
Human и не создаёт authority. JSON transport сохраняет producer-owned values
через `$type`/`$bytes`. Permission/Method и expected target проверяются перед
commit. Самосозданный decision JSON не является independent grant.

Owner records выбранного project находятся в `project/process/ewr/<owner>/`;
каждый namespace имеет одного writer. Они не обязательны для всякого analysis.
R получает bounded OwnerStore.snapshot queries.

Synthetic `invoke.py`, его B1/X04 tests и `tests/.work` относятся только к
development test окружению, расположены вне продукта. Их fixture instructions
в сохранённых exact CONTRACT.md не задают дополнительный продуктовый entry.
Старые state/<owner> fixtures не мигрируют автоматически в user history.

Чистый состав проверен local POSIX subprocess tests с synthetic direct channel.
Проверены bounded operation/reuse/denial cases; это не полная host qualification.
Live authentication, host-wide enforcement и unattended runner не заявлены. Outside authorized tool/filesystem
envelope — affected hold. Справка: `python3 -I -S -B app/bootstrap/operation.py --help`.
