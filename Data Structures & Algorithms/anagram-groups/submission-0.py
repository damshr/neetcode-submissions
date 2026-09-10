class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #If a key doesn't exist, automatically create an empty list for that key.

        for str in strs:
            key = ''.join(sorted(str))
            res[key].append(str)
        return list(res.values())




        