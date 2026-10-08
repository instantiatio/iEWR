# iEWR 5.7.0 Beta — основа и пределы

Дата: 2026-10-08. Human прямо поручил исправить замечания обеих проверок, проверить/испытать результат, выпустить 5.7.0, опубликовать как Latest и обновить main/главную GitHub. Повторное согласование этого же объёма не вводится; это основание данного выпуска, не разрешение пользователям на будущую публикацию.

Принятая исходная основа — iEWR 5.6.4 Beta, commit b83c3a19059dc109107f1471c97b7f7e9845f838, ZIP SHA-256 6e6fc0a58275a9a58d0667761993a2f46f45e3266f8fb893f072ab3787435b43, 141 файл. До правок новая рабочая копия и выбранные файлы исходного workspace совпали с ZIP. Сохранён отдельный instruction candidate-r1, SHA-256 897baae51fcf15f4bb1604c87ba8ac9fc21369878b282c98cf826527c2eb8092; выпуск включает его согласованные правки и исправления найденных замечаний.

Изменены инструкции, связанные G/X/P/bootstrap механизмы и Markdown reader Decision View. Добавлен только пустой project/dpf/.gitkeep: итоговый состав 142 файла. Удаление исторических файлов не выполнено — необходимое отсутствие reader/dependency/recovery use не доказано. Core Contract 1.0 RC, bundled source bytes, атрибуция, 14 DPF и 242 метода сохранены. Авторская Instantiatio SDLC 0.2.2 и привязка 0.2.2-package-5.6.2 не переименованы.

Изготовление пакета и публикация — разные наблюдения. CONFIGURATION.json описывает подготовленный exact архив: release_authorized, publication_authorized=true, public_release=false на момент сборки. Фактическая публикация подтверждается [GitHub Release 5.7.0](https://github.com/instantiatio/iEWR/releases/tag/5.7.0-beta) и отдельным publication receipt, без пересборки проверенного ZIP. distribution_ready означает сохранённые основания включения exact sources, а не промышленную квалификацию.

Наблюдения, проверки и ограничения — [VERIFICATION.md](VERIFICATION.md). Synthetic direct grounds не доказывают live-channel authentication; instruction-led обязанности не являются host-wide enforcement. Номер 5.7.0 отмечает существенную совместимую редакцию поведения и инструкций при сохранении Core/owners/authority; новая архитектурная major boundary не вводится.
