import pytest
from table_cipher import TableCipher

def test_cipher_initialization():
    cipher = TableCipher()
    assert cipher.key == "SECRET"
    
    cipher = TableCipher("CUSTOM")
    assert cipher.key == "CUSTOM"

def test_text_preparation():
    cipher = TableCipher()
    text = "Hello, World! 123"
    prepared = cipher._prepare_text(text)
    assert prepared == "HELLOWORLD"

def test_key_order():
    cipher = TableCipher("SECRET")
    order = cipher._get_key_order()
    expected = [2, 1, 4, 3, 0, 5]
    assert order == expected

def test_encryption():
    cipher = TableCipher("SECRET")
    text = "HELLO WORLD"
    encrypted = cipher.encrypt(text)
    assert len(encrypted) == len(text.replace(" ", ""))
    assert encrypted.isalpha()

def test_decryption():
    cipher = TableCipher("SECRET")
    original = "HELLO WORLD"
    encrypted = cipher.encrypt(original)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == "HELLOWORLD"

def test_full_cycle():
    cipher = TableCipher("CUSTOM")
    test_cases = [
        "HELLO WORLD",
        "PYTHON PROGRAMMING",
        "CRYPTOGRAPHY",
        "A" * 10,
        "Z" * 5
    ]
    
    for text in test_cases:
        encrypted = cipher.encrypt(text)
        decrypted = cipher.decrypt(encrypted)
        cleaned_text = ''.join(c for c in text.upper() if c.isalpha())
        assert decrypted == cleaned_text

def test_special_characters():
    cipher = TableCipher()
    text = "Hello! @#$%^&*() World! 123"
    encrypted = cipher.encrypt(text)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == "HELLOWORLD" 