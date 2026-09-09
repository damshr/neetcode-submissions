class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def build_freq_table(s):
            freq = {}
            for i in range(len(s)):
                freq[s[i]] = 1 + freq.get(s[i],0) 
            # "Give me the value for this key. If the key doesn't exist, give me 0."
            return freq
        s_freq, t_freq = build_freq_table(s), build_freq_table(t) 
        #calls function twice

        for char in s_freq:
            if char not in t_freq or s_freq[char] != t_freq[char]:
                return False
        return True

        