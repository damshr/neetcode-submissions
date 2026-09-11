class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #map char count of each string to list of anagrams
        for s in strs:
            count = [0] * 26 #26 zeroes , 1 for each char

            for c in s:
                count[ord(c) - ord("a")] += 1 #subtract ascii values
            res[tuple(count)].append(s) #list cannot be used as dict key but tuple can
        return list(res.values())

        