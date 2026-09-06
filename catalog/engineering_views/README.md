# Инженерные представления — reference для I

Это selection/content aid [I](../../modules/interaction/HUMAN_INTERACTION.md).
Domain owner отвечает за смысл предмета/модели; L — evidence/use assessment;
G — exact question/response grounds. Каталог не создаёт runtime subsystem,
Working Process, Task/Run, checklist, authority или state writer.

Применять, когда material engineering question, аудитория или решение требуют
сделать отношения понятными. [EV-01…EV-09](CATALOG.md) дают вопросы и content
cues. Сначала проверить exact subject/use и adequate current view. Если форма
помогает, представить её минимально достаточный смысл; не устраивать diagram
interview и не создавать файл/profile ради факта предложения.

Текст достаточен для небольшого линейного объяснения, таблица — для mappings,
ownership и сравнения, диаграмма — для существенных topology/interaction/state
relations. Нотация и renderer не выбирают Method. Перегруженную Mermaid схему
делить по вопросам/уровням или строить вертикально, сохраняя читаемость.

Для material use указать предмет и boundary/level, purpose/use/audience, exact
source/configuration, freshness, material delta, uncertainty и non-coverage.
Level of consideration нужен, только если применим к предмету. View — projection;
authoritative model требует отдельного direct source/ownership basis. Не создавать
parallel truth. Component evidence не доказывает system properties.

Перед требуемым Human решением фактически показать affected semantics, условия,
эффекты и альтернативы. Ссылка дополняет подачу. Text-complete fallback сохраняет
material смысл, если renderer недоступен; privacy ограничения одинаковы для
текста и графики. Если sufficient safe presentation недоступна, удерживать только
зависимый выбор. Нельзя автоматически генерировать review-checklist, требовать
unset human fields, literal headings или admission ladder. Понятного direct
ответа достаточно в границах G exact question/conditions/currentness.

Feedback связывать с exact view/configuration и понятным element reference.
Вопрос/изменение/условие возвращается content owner; после разрешённого изменения
показать affected delta. Unaffected elements переиспользуются. View не редактирует
source и не создаёт решение от показа UI.

У material persisted-data use EV-05 помогает разделить logical entities, meaning,
relations/cardinalities и invariants; нужные physical tables/keys/constraints/
indexes/migrations; analytics layers и mappings/gaps; source/change/limitations.
Эти concerns могут быть показаны таблицей/текстом. Обязательность evidence идёт
от actual use/Method/policy, а не от EV label или наличия database.

Project profile [template](templates/PROJECT_VIEW_PROFILE.yaml) — optional view,
только при полезном повторном use и явно выбранном persistent scope. Existing
SoR использовать напрямую. Новые schema 2 fields не конвертируют прежние schema 1
records; original source_work_context/status остаются historical facts.

External renderer/skill получает только разрешённые данные и bounded task.
Capability compatibility проверяется по X/F guidance; external publication не
возникает автоматически. Никакого обязательного числа видов или новых DPF routes.
