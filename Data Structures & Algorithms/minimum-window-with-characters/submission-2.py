class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        mapS = {}
        mapT = {}

        # Count characters in t
        for ch in t:
            mapT[ch] = 1 + mapT.get(ch, 0)

        have = 0 #how many chars currently have reqd freq
        need = len(mapT) #counts distinct chars
        result = ""
        left = 0
        min_len = float("inf")   # FIX

        # Sliding window
        for right in range(len(s)):
            ch = s[right]
            mapS[ch] = mapS.get(ch, 0) + 1
            
            if ch in mapT and mapS[ch] == mapT[ch]:
                have += 1

            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                left_char = s[left]
                mapS[left_char] -= 1

                if left_char in mapT and mapS[left_char] < mapT[left_char]:
                    have -= 1

                left += 1

        return result

    



