# Компонент оформления Markdown

`vendor/marked.cjs` — неизменные bytes `lib/marked.umd.js` из Marked **17.0.5** (https://marked.js.org/), MIT. Полный текст лицензии сохранён в [vendor/MARKED_LICENSE.md](vendor/MARKED_LICENSE.md). Источник этой локальной копии — установленный пакет npm `marked@17.0.5`; сетевое получение и установка не выполнялись.

Компонент вызывается только во время сборки Markdown → HTML через Node.js 20+. Готовый Decision View и его HTML-материалы не загружают Marked, Node.js или удалённые библиотеки. Для построения ER и основного HTML достаточно Python 3.10+; ER renderer написан в этом проекте и не использует Marked.
