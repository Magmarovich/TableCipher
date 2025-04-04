#!/usr/bin/env python
# -*- coding: utf-8 -*-

from table_cipher import TableCipher

def main():
    print("=" * 50)
    print("Интерактивный режим табличного шифра")
    print("=" * 50)
    
    key = input("Введите ключ шифрования (или нажмите Enter для использования ключа по умолчанию 'SECRET'): ")
    if not key:
        key = "SECRET"
    
    cipher = TableCipher(key)
    print(f"Используется ключ: {key}")
    
    while True:
        print("\nВыберите действие:")
        print("1. Зашифровать текст")
        print("2. Расшифровать текст")
        print("3. Изменить ключ")
        print("0. Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            text = input("Введите текст для шифрования: ")
            encrypted = cipher.encrypt(text)
            print(f"Зашифрованный текст: {encrypted}")
        
        elif choice == "2":
            text = input("Введите текст для расшифровки: ")
            decrypted = cipher.decrypt(text)
            print(f"Расшифрованный текст: {decrypted}")
        
        elif choice == "3":
            key = input("Введите новый ключ шифрования: ")
            if key:
                cipher = TableCipher(key)
                print(f"Ключ изменен на: {key}")
            else:
                print("Ключ не может быть пустым")
        
        elif choice == "0":
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, выберите 0, 1, 2 или 3")

if __name__ == "__main__":
    main() 