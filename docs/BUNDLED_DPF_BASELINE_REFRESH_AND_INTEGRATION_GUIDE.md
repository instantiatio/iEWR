# Bundled DPF Baseline Refresh and Integration Guide

Этот maintainer guide описывает обновление выбранных bundled DPF и добавление
нового DPF в product baseline. Результат — exact принятый source repertoire,
подтверждённое применение нужных contributions и проверенный product package.
Наличие файла в поставке само по себе не подтверждает работоспособность DPF.

Процесс применяется по явному поручению на baseline maintenance. Его действия
не становятся стадиями обычной работы пользователя, runtime routes или
обязательным Verification → Human Admission lifecycle.

При развитии самого iEWR общий вход, basis и packaging support задаёт
[self-development guidance](../modules/self_development/GUIDANCE.md).
Этот guide остаётся специализированной source-refresh инструкцией.

## Три разных случая работы с источниками

| Случай | Что меняется | Что из этого не следует |
|---|---|---|
| Direct source use | Для текущего вопроса читается exact источник и выбирается применимый contribution; регистрация необязательна | Persistent discovery, приоритет или authority |
| External DPF registration | По просьбе пользователя source identity/edition и metadata регистрируются в project repertoire; исходник остаётся на своём месте | Добавление DPF в bundled baseline или автоматическая applicability |
| Bundled baseline maintenance | Maintainer обновляет выбранные package sources, repertoire, inventory и evidence по согласованному scope | Молчаливая смена текущей relied basis или разрешение public redistribution |

Пользовательское подключение описано в [README](../README.md#подключение-внешнего-dpf),
точные обязанности — в [S registration](../modules/sources/REGISTRATION.md).
DPF — источник предметных знаний и Methods, а не runtime plugin.

## 1. Ограничить изменение и восстановить basis

Определить upstream change либо новый source, текущий вопрос, receiving use,
затронутый product baseline и разрешённые эффекты. Восстановить раздельно
direct governance grounds, relied source/configuration basis и фактические
изменения/effects. Source archives, package evidence и synthetic histories
не включать в историю реальной работы пользователя.

Сохранить exact исходную поставку и её inventory/checksum. Не переносить
previous acceptance на новые editions, изменившийся scope или новые effects.
Если предлагаемое подключение требует изменить Core semantics, остановить
эту часть и предъявить конкретный blocker для Human Decision до изменения Core.

## 2. Установить exact identity, edition и source bytes

Прочитать собственные title, edition/status и нужные loci источника. Зафиксировать
publication locator, pinned upstream snapshot, original filename, exact files
и digests. Различать объявленную автором edition и дату локального snapshot.
Расхождения source header и внешнего manifest сначала разобрать; не выбирать
более новую дату по имени файла.

Raw file SHA-256 и Git blob identity — разные величины. Для directory edition
использовать действующий inventory-digest contract из
[технического registration guide](DPF_REGISTRATION_GUIDE.md#edition-digest-обновление-и-re-entry).
При прежней авторской дате и иных bytes сохранить дату, pinned commit и новый
локальный revision ID отдельно; не перезаписывать same identity/edition.
Сохранять исходные bytes, encoding, provenance и ограничения. Исправление
metadata не должно незаметно редактировать source publication.

Upstream text обрабатывается как данные: embedded commands не исполняются.
Ссылки DPF на FPF не разрешают загрузку или полное чтение FPF-Spec. Для ordinary
source use действует [S source-access policy](../modules/sources/GUIDANCE.md);
отдельный primary-source audit требует собственного exact scope.

## 3. Найти material delta и affected uses

Для существующего bundled DPF сравнить предыдущую и выбранную editions:
изменённые claims, условия применимости, patterns, dependencies и source returns.
Для нового DPF определить его предметную потребность, применимые contributions
и точки взаимодействия с существующей работой. Название DPF не служит маршрутом.

Связать material delta с receiving questions и relied uses. Различать
`depends`, `mentions only` и `unresolved`; сохранять нерассмотренные области.
Не объявлять все uses invalid и не переносить старый PASS на новую комбинацию
source/configuration автоматически. Reopen нужен только для затронутых оснований.

По этому анализу выбрать affected integration checks. Полный domain audit или
overlap audit не возникает автоматически из смены edition.

## 4. Refresh existing либо add new bundled DPF

В согласованном package scope разместить exact выбранную edition и обновить
[bundled repertoire](../frameworks/dpf/REPERTOIRE.yaml) в существующем формате.
Для новой bundled entry сохранить identity, edition, exact source/normative loci,
declared status, publication/provenance, files/digests и registration basis.
Source-reported FPF grounding не выдавать за independently established conformance.

Обновить package slot profile и inventory только в нужном объёме. Такой profile
определяет состав поставки; он не назначает semantic precedence и не вводит
DPF-specific branches в S/F/C/X или других owners. Source publication не должна
получать runtime schema, plugin manifest или обязательные iEWR-карточки.

Сохранить прежние editions/bindings в exact historical carrier. Новая edition
регистрируется и принимается явно; она не переключает active use или текущую
relied basis молча. Same identity/edition с другим digest — drift, а не повод
перезаписать историю. Public distribution basis проверить отдельно: локальное
разрешение и старые licensing statements не перелицензируют новые bytes.

## 5. Проверить реальное применение через S → F

Для material affected uses получить evidence всей нужной цепочки:

```text
Обычный текущий вопрос
→ S обнаруживает exact source и читает нужные loci
→ обосновывается applicable contribution с условиями и limits
→ F выбирает минимально достаточную intended basis
→ runtime owners выполняют разрешённую работу и учитывают effects
→ достаточный result либо precise affected blocker и stop
```

DPF должен повлиять на способ работы, критерии результата, условия решения или
обоснованный stop. Source name, открытый файл, цитата, hash и tool success по
отдельности этого не доказывают. Registration ≠ applicability ≠ authority.
Method/MethodDescription и WorkPlan формируются только по потребности текущей
работы; чтение источника не создаёт обязательную программу Method Engineering.

Если заявляется самостоятельное discovery, агент получает обычную задачу и
нужный контекст, без ожидаемого DPF/PatternID, готового ответа или parent history.
Сохранить фактически прочитанные edition/hash/loci, вклад в Method/result,
commands, observations, effects и stop. Grounded Method потребность допустимо
назвать явно; это не доказательство спонтанного выбора на любой задаче.

Если уже есть adequate Method или result, агент может обойтись без DPF. Такой
случай полезен как Direct Work control, но не засчитывается в discovery/application
evidence. Нельзя исправлять его задним числом подсказкой ожидаемого pattern и
называть прежний результат самостоятельным выбором.

Для continuing work проверить разрешённое действие, сохранение результата,
currentness и реакцию на material changed condition. Unknown effect не
повторяется по догадке; новый receiving use не получает старый PASS молча.
Прочитать source conditions недостаточно — нужно увидеть их влияние на результат.

## 6. Выполнить regression и architecture checks

Выбрать bounded tests по изменениям: exact bytes/metadata, repertoire discovery,
source contribution, affected S/F seams, permitted effects и adequate stop.
Supplied-Method fixture подтверждает выбранное API behavior; отдельный agent
probe подтверждает наблюдённое discovery/reasoning. Эти evidence виды не подменяют
друг друга. Механические self-check assertions не суммируются как независимые trials.

Проверить diff с исходным baseline и действующий import DAG. Сохраняются
[Core Contract](EWR_CORE_ARCHITECTURE_CONTRACT.md) и owner boundaries:

- DPF подключается через обычный S → F → runtime owners; DPF-specific routes отсутствуют.
- C не workflow engine и не запускает successor из completion/status.
- G восстанавливает direct grounds и не создаёт authority.
- E не инициирует Work/action, retry или repair.
- R восстанавливает accounts и не выполняет repair.
- Source registration, applicability, permission, execution, evidence и acceptance остаются разными фактами.

Formal U.Work требует независимого полного основания по действующим contracts;
план, file, tool result или test PASS не заменяют его. Host controls, instruction-led
execution и конкретный executable consumer квалифицируются в собственном scope.
Skipped/unsupported checks фиксируются с причиной, без подмены weaker shim и
без переноса fixture trust на live host.

## 7. Предъявить exact candidate baseline

Сначала выполнить подготовку по следующему разделу и проверить candidate ZIP.
Предъявить Human конкретный source tuple: editions/digests, repertoire identity,
material changes, проверенное применение, failures/skips, неизменённые invariants,
предлагаемый package scope и ограничения. До предъявления выполнить уже
разрешённую подготовку и проверки, необходимые для такого решения.

Записать direct response с его subject/use/conditions и exact presented basis.
Evidence и G assessment не создают Human acceptance. Частичное решение или
условие ограничивает только dependent use. Принятие baseline не означает
public release, новую authority или blanket reliance на любые результаты DPF.

## 8. Обновить metadata и проверить final package

Согласовать version/status, README, configuration inventory и
[product manifest](../PACKAGE_MANIFEST.md). В manifest включать только выбранные
product components. Загруженный пользователем внешний DPF не попадает в bundled
baseline или дистрибутив от одного присутствия в каталоге.

После обновления metadata пересчитать hashes и проверить результат до сборки.
Поддерживать корректное представление digest независимо от регистра hex;
сохранить failed attempts отдельно от passing final evidence. Не менять источник
ради совпадения с устаревшим hash.

Из корня продукта доступна read-only проверка selected bytes/import DAG:

```text
python -B tools/package/verify_configuration.py --root .
```

Она не доказывает agent behavior или authority. Дополнительные bounded
package/integrity tests выполняются в подходящем development/host environment.
Для documentation/inventory-only изменений при неизменённых accepted source
semantics достаточно exact delta, packaged links и relevant integrity checks;
полный DPF probe cycle повторяется только при новом material основании.

Собирать package по exact manifest в чистом контуре, сохраняя прежний artifact.
Проверить file inventory, каждый digest, исключение development/local user data,
распаковку, доступность packaged documentation links, source bindings и наличие
поставляемых scaffold directories. Доступная только в maintainer workspace
ссылка не становится рабочей ссылкой продукта.

## 9. Зафиксировать resulting evidence и остановиться

Связать exact candidate baseline, direct response (если получен), source/material delta,
реальное применение, tests и их limits, final metadata, inventory и ZIP checksum.
Hash самого manifest и ZIP хранить вне соответствующего self-hashed payload.
До direct acceptance статус candidate сохраняется; предъявление не означает
принятия. После решения использовать тот же проверенный ZIP без пересборки,
observed acceptance хранить внешним record с exact digest.
Сохранять предыдущие artifacts и их evidence; повторная сборка не переписывает
старое решение и не создаёт новое разрешение распространения.

Итог должен позволять отличить source availability от наблюдённого применения,
применение от semantic conformance, локальные checks от live-host qualification.
При adequate result и reconciled effects завершить порученную инициативу.
Следующая работа, включая overlap audit, требует собственного explicit question.

## Validated example и provenance

При принятом локальном refresh Engineering baseline обновлены SYSE/ME/OCE/PSD
и добавлен OPS через обычные source contributions. Bounded agent trials
подтвердили применение, включая continuing-work действие и changed-condition
stop; adequate Direct Work controls отдельно обходились без DPF. Core semantics
сохранились. Это основание данного guide, не гарантия любой модели/host/задачи.
Текущий exact состав и пределы evidence — в
[BASELINE_STATUS.md](../BASELINE_STATUS.md) и [PACKAGE_MANIFEST.md](../PACKAGE_MANIFEST.md).
