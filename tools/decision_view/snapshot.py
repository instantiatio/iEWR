"""Cooperative bounded local snapshot primitives; no semantic or authority claims."""
from datetime import datetime
import os
from pathlib import Path
import re
import stat

LIMIT = 1024 * 1024


def fields(value, names, where):
    if not isinstance(value, dict) or set(value) != set(names.split()):
        raise ValueError(f"{where}: ожидаются поля {names}")


def text(value, where, nullable=False):
    if nullable and value is None:
        return
    if not isinstance(value, str) or not value.strip() or len(value) > 12000:
        raise ValueError(f"{where}: нужен непустой текст до 12000 символов")
    if any(ord(c) < 32 and c not in '\n\r\t' for c in value):
        raise ValueError(f"{where}: управляющий символ")


def sequence(value, where, maximum=100):
    if not isinstance(value, list) or len(value) > maximum:
        raise ValueError(f"{where}: нужен список, максимум {maximum}")


def timestamp(value, where, nullable=True):
    if nullable and value is None:
        return
    text(value, where)
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if parsed.utcoffset() is None:
            raise ValueError()
    except ValueError:
        raise ValueError(f"{where}: нужна ISO-дата со временем и часовым поясом") from None


def local_path(path, root):
    path = Path(os.path.abspath(path))
    try:
        relative = path.relative_to(root)
    except ValueError:
        raise ValueError("Путь вне выбранного root") from None
    current = root
    for part in relative.parts:
        if (any(ord(c) < 32 or c in ':*?"<>|' for c in part)
                or part.endswith(('.', ' '))
                or re.fullmatch(r'(?i)(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\..*)?', part)):
            raise ValueError('Непереносимое имя файла или поток данных')
        current /= part
        if current.exists() or current.is_symlink():
            info = current.lstat()
            if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
                raise ValueError("Ссылки и reparse points не поддерживаются")
    return path


def read_local(path, maximum=LIMIT):
    before = path.stat()
    if not stat.S_ISREG(before.st_mode) or before.st_size > maximum:
        raise ValueError("Нужен обычный файл допустимого размера")
    with path.open('rb') as source:
        raw = source.read(maximum + 1)
    after = path.stat()
    if len(raw) > maximum or (before.st_ino, before.st_size, before.st_mtime_ns) != (
            after.st_ino, after.st_size, after.st_mtime_ns):
        raise ValueError("Файл изменился во время чтения")
    return raw


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Повтор поля JSON: {key}")
        result[key] = value
    return result

