class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window technique
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet: #it is duplicate
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        