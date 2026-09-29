class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        freq_s1, freq_s2 = [0] * 26, [0] * 26  #store freq of each alphabet
        matches = 0 # maintain total no. of eqal chars

        for i in range(n1):
            freq_s1[ord(s1[i]) - ord('a')] += 1 #freq of all chars of s1 string
            freq_s2[ord(s2[i]) - ord('a')] += 1 #freq of all chars of s2 string

        if freq_s1 == freq_s2:
            return True

    
        for i in range(n1, n2):
         # add new char to freq array
            freq_s2[ord(s2[i]) - ord('a')] += 1
            freq_s2[ord(s2[i - n1]) - ord('a')] -= 1 #remove left char
            if freq_s1 == freq_s2:
                return True
        return False

# i - n1 points to the leftmost character of the current window, the one that needs to be removed when the new character s2[i] enters.

        




        