#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import sys
import os

def main():
    """
    Запуск автоматических юнит-тестов с подробным выводом результатов.
    """
    print("=" * 50)
    print("Запуск автоматических юнит-тестов")
    print("=" * 50)
    
    # Получаем путь к директории с тестами
    tests_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests")
    
    # Запускаем тесты с подробным выводом
    args = [
        "-v",  # Подробный вывод
        "--cov=table_cipher",  # Измерение покрытия кода
        "--cov-report=term",  # Вывод отчета о покрытии в терминал
        tests_dir
    ]
    
    # Запускаем pytest с аргументами
    result = pytest.main(args)
    
    # Выводим результат
    if result == 0:
        print("\nВсе тесты успешно пройдены!")
    else:
        print("\nНекоторые тесты не пройдены. Проверьте вывод выше для деталей.")
    
    return result

if __name__ == "__main__":
    sys.exit(main()) 