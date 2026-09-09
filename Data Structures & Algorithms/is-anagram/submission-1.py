class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
# Counter(s) creates a dictionary-like object mapping characters to their counts
# Comparing the two Counter objects checks if both the keys and values match exactly