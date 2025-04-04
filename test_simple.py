from table_cipher import TableCipher
import math

def print_table(table):
    for row in table:
        print(row)

def test_simple():
    cipher = TableCipher("SECRET")
    
    text = "HELLO"
    print(f"\nИсходный текст: {text}")
    
    key_order = cipher._get_key_order()
    print(f"Порядок столбцов: {key_order}")
    print(f"Ключ: {[(i, c) for i, c in enumerate(cipher.key)]}")
    
    key_length = len(cipher.key)
    text_length = len(text)
    rows = math.ceil(text_length / key_length)
    
    table = []
    for i in range(rows):
        row = []
        for j in range(key_length):
            pos = i * key_length + j
            if pos < text_length:
                row.append(text[pos])
            else:
                row.append('')
        table.append(row)
    
    print("\nИсходная таблица:")
    print_table(table)
    
    encrypted = cipher.encrypt(text)
    print(f"\nЗашифрованный текст: {encrypted}")
    
    decrypt_table = [['' for _ in range(key_length)] for _ in range(rows)]
    pos = 0
    for col_idx in key_order:
        for row in range(rows):
            if pos < len(encrypted):
                decrypt_table[row][col_idx] = encrypted[pos]
                pos += 1
    
    print("\nТаблица для дешифрования:")
    print_table(decrypt_table)
    
    decrypted = cipher.decrypt(encrypted)
    print(f"\nРасшифрованный текст: {decrypted}")
    
    assert text == decrypted, f"Ошибка! Ожидалось {text}, получено {decrypted}"
    print("Тест пройден успешно!")

def test_long_text():
    cipher = TableCipher("CUSTOM")
    
    text = "CRYPTOGRAPHY"
    print(f"\nИсходный текст: {text}")
    print(f"Длина текста: {len(text)}")
    
    key_order = cipher._get_key_order()
    print(f"Порядок столбцов: {key_order}")
    print(f"Ключ: {[(i, c) for i, c in enumerate(cipher.key)]}")
    
    key_length = len(cipher.key)
    text_length = len(text)
    rows = math.ceil(text_length / key_length)
    
    table = [['' for _ in range(key_length)] for _ in range(rows)]
    pos = 0
    for i in range(rows):
        for j in range(key_length):
            if pos < text_length:
                table[i][j] = text[pos]
                pos += 1
    
    print("\nИсходная таблица:")
    print_table(table)
    
    encrypted = cipher.encrypt(text)
    print(f"\nЗашифрованный текст: {encrypted}")
    print(f"Длина зашифрованного текста: {len(encrypted)}")
    
    decrypt_table = [['' for _ in range(key_length)] for _ in range(rows)]
    chars_per_col = [rows if i < text_length % key_length else rows - 1 for i in range(key_length)]
    print(f"\nСимволов в столбцах: {chars_per_col}")
    
    pos = 0
    for i, col in enumerate(key_order):
        for row in range(chars_per_col[col]):
            decrypt_table[row][col] = encrypted[pos]
            pos += 1
    
    print("\nТаблица для дешифрования:")
    print_table(decrypt_table)
    
    decrypted = cipher.decrypt(encrypted)
    print(f"\nРасшифрованный текст: {decrypted}")
    print(f"Длина расшифрованного текста: {len(decrypted)}")
    print(f"Ожидаемый текст: {text}")
    
    assert text == decrypted, f"Ошибка! Ожидалось {text}, получено {decrypted}"
    print("Тест пройден успешно!")

if __name__ == "__main__":
    test_simple()
    test_long_text() 