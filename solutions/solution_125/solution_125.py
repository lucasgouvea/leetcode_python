import re

class Solution125:
    char_pattern = r'[a-zA-Z0-9]'

    def is_palindrome(self, s: str) -> bool:

        parsed_str = self.__get_parsed_str(s)

        left: int = 0
        right: int = len(parsed_str) - 1
        
        while left < right:
            if parsed_str[left] != parsed_str[right]:
                return False
            left += 1
            right -= 1

        return True

    def __get_parsed_str(self, s: str) -> str:
        parsed_str: str = ""

        for char in s:
            if self.__is_char(char) == True:
                parsed_str += char.lower()
        
        return parsed_str

    def __is_char(self, s: str) -> bool:
        if re.match(self.char_pattern, s):
            return True
        return False