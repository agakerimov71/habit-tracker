"""Хранение привычек в JSON-файле."""
import json
import os


def load(path):
    # если файла еще нет, начинаем с пустого словаря
    if not os.path.exists(path):
        return {}
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def save(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
