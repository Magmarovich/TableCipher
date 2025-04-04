#!/usr/bin/env python
# -*- coding: utf-8 -*-

from table_cipher import TableCipher

def print_example(title, text, key="SECRET"):
    print("\n" + "=" * 50)
    print(f"Пример: {title}")
    print("=" * 50)
    
    cipher = TableCipher(key)
    
    encrypted = cipher.encrypt(text)
    
    decrypted = cipher.decrypt(encrypted)
    
    print(f"Исходный текст: {text}")
    print(f"Ключ: {key}")
    print(f"Зашифрованный текст: {encrypted}")
    print(f"Расшифрованный текст: {decrypted}")
    
    original_clean = ''.join(c for c in text.upper() if c.isalpha())
    if original_clean == decrypted:
        print("✓ Шифрование и дешифрование успешны")
    else:
        print("✗ Ошибка в шифровании или дешифровании")
        print(f"Ожидалось: {original_clean}")
        print(f"Получено:  {decrypted}")

def main():
    print("Демонстрационные примеры табличного шифра")
    
    print_example(
        "Простой текст",
        "HELLO WORLD"
    )
    
    print_example(
        "Текст с другим ключом",
        "PYTHON PROGRAMMING",
        "CUSTOM"
    )
    
    print_example(
        "Текст со специальными символами",
        "Hello! @#$%^&*() World! 123"
    )
    
    print_example(
        "Длинный текст",
        "THIS IS A LONGER TEXT THAT DEMONSTRATES HOW THE CIPHER WORKS WITH LONGER MESSAGES"
    )
    
    print_example(
        "Текст с повторяющимися символами",
        "AAAAA BBBBB CCCCC"
    )

if __name__ == "__main__":
    main() 