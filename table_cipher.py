import math
from typing import List, Tuple

class TableCipher:
    def __init__(self, key: str = "SECRET"):
        self.key = key.upper()
        
    def _prepare_text(self, text: str) -> str:
        text = ''.join(c for c in text.upper() if c.isalpha())
        return text
    
    def _get_key_order(self) -> List[int]:
        key_pairs = [(char, i) for i, char in enumerate(self.key)]
        key_pairs.sort()
        return [pos for _, pos in key_pairs]
    
    def encrypt(self, text: str) -> str:
        text = self._prepare_text(text)
        
        key_length = len(self.key)
        text_length = len(text)
        rows = math.ceil(text_length / key_length)
        
        table = [['' for _ in range(key_length)] for _ in range(rows)]
        
        pos = 0
        for i in range(rows):
            for j in range(key_length):
                if pos < text_length:
                    table[i][j] = text[pos]
                    pos += 1
        
        key_order = self._get_key_order()
        
        result = []
        for col_idx in key_order:
            for row in range(rows):
                if table[row][col_idx]:
                    result.append(table[row][col_idx])
        
        return ''.join(result)
    
    def decrypt(self, encrypted_text: str) -> str:
        text = self._prepare_text(encrypted_text)
        
        key_length = len(self.key)
        text_length = len(text)
        rows = math.ceil(text_length / key_length)
        
        table = [['' for _ in range(key_length)] for _ in range(rows)]
        
        key_order = self._get_key_order()
        
        chars_in_last_row = text_length % key_length
        if chars_in_last_row == 0:
            chars_in_last_row = key_length
        
        pos = 0
        for col_idx in key_order:
            chars_in_col = rows if col_idx < chars_in_last_row else rows - 1
            for row in range(chars_in_col):
                if pos < text_length:
                    table[row][col_idx] = text[pos]
                    pos += 1
        
        result = []
        for row in range(rows):
            for col in range(key_length):
                if table[row][col]:
                    result.append(table[row][col])
        
        return ''.join(result) 