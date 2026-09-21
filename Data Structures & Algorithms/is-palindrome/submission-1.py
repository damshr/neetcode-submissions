class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1


        while l < r:
            # move till points to alpha numeric char
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True


    # checks if the Unicode code point of character c falls between the particular code point
    def alphaNum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

        