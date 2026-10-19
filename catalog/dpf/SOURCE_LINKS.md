# Переходы по ссылкам исходных DPF

Тексты DPF сохранены без переписывания. Часть авторских относительных ссылок использует структуру исходной библиотеки, а не каталоги этой поставки. Для включённых публикаций используйте таблицу ниже и [указатель методов](METHODS.md), затем проверяйте original body нужной редакции. Совпадение имени не устанавливает переносимость утверждения или соответствие старого PatternID новому.

| Имя в исходной ссылке | Доступный источник или граница |
| --- | --- |
| `BPD.md` | Не входит в комплект. Нужный вклад требует доступного согласованного источника; ссылка не разрешает его получение. |
| `CORPORATE-GOVERNANCE-PRINCIPLES-FRAMEWORK.md` | Не входит в комплект. Нужный вклад требует доступного согласованного источника; ссылка не разрешает его получение. |
| `DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md` | [PSDA](../../frameworks/dpf/problem-structuring-decision-support/2026-10-12-rev-7d0a7800/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md) — закреплённая редакция базы |
| `ENGINEERING-ASSET-MANAGEMENT-PRINCIPLES-FRAMEWORK.md` | Не входит в комплект. Нужный вклад требует доступного согласованного источника; ссылка не разрешает его получение. |
| `ENGINEERING-DPF-SUITE-REFERENCE.md` | Не входит в комплект. Нужный вклад требует доступного согласованного источника; ссылка не разрешает его получение. |
| `EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md` | [EXD](../../frameworks/dpf/explanation-design/2026-10-17-rev-d9c3dd65/EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md) — закреплённая редакция базы |
| `FPF-Spec.md` | Не входит в комплект. Нужный вклад требует доступного согласованного источника; ссылка не разрешает его получение. |
| `HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md` | Не входит в комплект. Нужный вклад требует доступного согласованного источника; ссылка не разрешает его получение. |
| `KNOWLEDGE-CORPUS-ACCESS-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | [KCAE](../../frameworks/dpf/knowledge-corpus-access-engineering/snapshot-2026-10-14-rev-7d0a7800/KNOWLEDGE-CORPUS-ACCESS-ENGINEERING-PRINCIPLES-FRAMEWORK.md) — закреплённая редакция базы |
| `MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | Не входит в комплект. Нужный вклад требует доступного согласованного источника; ссылка не разрешает его получение. |
| `MANAGEMENT-ACCOUNTING-PRINCIPLES-FRAMEWORK.md` | Не входит в комплект. Нужный вклад требует доступного согласованного источника; ссылка не разрешает его получение. |
| `MATHEMATICAL-MODELING-PRACTICE-DPF.md` | Не входит в комплект. Нужный вклад требует доступного согласованного источника; ссылка не разрешает его получение. |
| `METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | [ME](../../frameworks/dpf/method-engineering/2026-09-20-rev-9e1c4834/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md) — закреплённая редакция базы |
| `OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md` | [OPS](../../frameworks/dpf/operations-management/2026-10-15-rev-b40c9df9/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) — закреплённая редакция базы |
| `ORGANIZATION-ADMINISTRATION-PRINCIPLES-FRAMEWORK.md` | [ADM](../../frameworks/dpf/organization-administration/2026-09-20-rev-7d0a7800/ORGANIZATION-ADMINISTRATION-PRINCIPLES-FRAMEWORK.md) — закреплённая редакция базы |
| `ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | [OCE](../../frameworks/dpf/organization-change-engineering/2026-10-15-rev-b40c9df9/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md) — закреплённая редакция базы |
| `RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md` | [RMP](../../frameworks/dpf/research-method-practice/2026-10-15-rev-b40c9df9/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md) — закреплённая редакция базы |
| `SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | [SIE](../../frameworks/dpf/semantic-integration-engineering/2026-10-15-rev-b40c9df9/SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK.md) — закреплённая редакция базы |
| `STRATEGY-PRINCIPLES-FRAMEWORK.md` | [STR](../../frameworks/dpf/strategy/2026-10-14-rev-7d0a7800/STRATEGY-PRINCIPLES-FRAMEWORK.md) — закреплённая редакция базы |
| `SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | [SYSE](../../frameworks/dpf/systems-engineering/2026-10-15-rev-b40c9df9/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md) — закреплённая редакция базы |

Это навигация, не автоматический resolver и не утверждение совместимости ссылочных fragments. Полная проверка 6.0.3 обнаружила 277 унаследованных относительных переходов, чьи буквальные пути не существуют в структуре поставки. Это ссылки неизменённых источников; новые документы и все 266 входа указателя проверены отдельно. Точный список включён в BUILD_CHECKS. Источники с путями Library/Suite ищут по имени файла в таблице и указателе, затем проверяют нужный раздел и редакцию.

Дополнительные соответствия:

| Имя исходной ссылки | Переход или граница |
| --- | --- |
| `ORGANIZATION-ADMINISTRATION-PRINCIPLES-FRAMEWORK.md` | [ADM](METHODS.md#adm) — текущее полное тело через указатель |
| `ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md` | [OCE](METHODS.md#oce) — текущее полное тело через указатель |
| `WEP.md` внутри VID | В VID явно закреплён WEP 0.1.4; этот старый файл не включён. [Текущий WEP 0.1.6](METHODS.md#wep) не считается молчаливой заменой. Получите достаточный результат из задания либо проверьте затронутое соединение перед новым use. |

Полный FPF, BPD и прочие отсутствующие публикации из ссылок не добавлены. Отсутствующий обязательный вклад удерживает зависимое применение; наличие навигационного соответствия само по себе не квалифицирует его смысл.

Если необходимое определение или метод недоступны, сохраняется точный gap зависимого use. При достаточном теле выбранного метода отсутствие необязательной справки не блокирует независимый полезный результат. Правила поиска и подключения — [AGENTS](../../AGENTS.md).
