class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_order = ''.join(char.lower() for char in s if char.isalnum())
        str_reverse = ''.join(reversed(str_order))

        if str_order == str_reverse:
            return True
        else:
            return False
        