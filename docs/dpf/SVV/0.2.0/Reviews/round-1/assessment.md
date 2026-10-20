# SVV 0.2.0 — round 1

Ordinary floor 4 пока не достигнут: `repairBeforeUse` у шести E.21 результатов и `repairBeforeDPFUse` у пакета. Все 114 координат с соседними значениями, 12 DA, 13 PFM, D12, F.19 и полная PFIP traversal сохранены в assessment.json. Средний балл не вычислялся.

Предметные действия шести методов восстановлены. Первое применение правильно отвергло [1,2,3] при ожидаемых [3,1,2]; выполнение исходной функции не проводилось. Сквозной desk replay сохранил различия oracle/случая/границы наблюдения/сбоя/нужды/вывода без обязательной поставки другого DPF.

1. **SVV-F2 — потерян рабочий возврат к источникам.** SVV.md:499 ведёт в PROVENANCE.md, но бывшая ссылка на SOURCES.md там только экранированная историческая цитата (строка 40). Активных ссылок в PROVENANCE нет. Сама карта с capture hashes/атрибуцией сохранена в `stage/docs/dpf/shared/software-2026-10-19/SOURCES.md`. Дайте из PROVENANCE корректную живую ссылку `../../shared/software-2026-10-19/SOURCES.md`; сохраняйте исторический статус, без обязательного чтения других DPF. До ремонта traceability каждой E.21 строки =3; D5/D9/D10=3. PFIP обнаружил именно source-return loss, не потерю software-step.
2. **SVV-F1 — нет одной декларации selectable keys/forms.** PROPERTY и UNKNOWN опубликованы как H3 ordinary entries, однако product declaration отсутствует. Достаточна одна компактная запись PROPERTY=ordinary-entry, UNKNOWN=ordinary-entry, cards=none. Текущие короткие входы достаточны содержательно; mantra не требуется. PFM1a fail; D2/D5=3.

RESTORE побайтно восстановил весь predecessor 0.1.1 с SHA256 `467788373c9aa1f8c19c0432e60067d48726e1f17e3edcfae303617dbf8d89f4`; все unchanged/changed spans проверены раздельно. Из 23 accepted-input rows одна source-history relocation остаётся частичной из-за F2. Current source hash совпал с REQUEST до и после чтения.

Основа F.19 смешанная: whole-publication expert walkthrough и один сохранённый actual AI response в initial.md. Прежние source/fixture records использованы по совпадающим claims, без переноса grades. Новых user/production/crash испытаний нет; live websites не сверялись. Изоляция чтения — компенсированная порядком и отчётом, не enforced filesystem isolation. Тексты рамок не менялись.
