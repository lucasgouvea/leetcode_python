from typing import Tuple


class Solution387:
    def first_uniq_char(self, s: str) -> int:
        letter_count: dict[str, int] = {}
        
        for i in range(len(s)):
            letter = s[i]
            count = letter_count.get(letter)
            if count == None:
                letter_count[letter] = 1
            else:
                letter_count[letter] = count + 1
                
        for i in range(len(s)):
            letter = s[i]
            count = letter_count.get(letter)
            if count == 1:
                return i

        return -1