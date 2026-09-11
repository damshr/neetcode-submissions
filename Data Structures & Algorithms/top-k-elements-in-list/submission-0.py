class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = 1 + freq.get(i,0)

        sorted_items = sorted(freq.items(), key = lambda item : item[1], reverse = True)
        top_k = sorted_items[:k]

        top_two_keys = []
        
        for key, freq in top_k:
            top_two_keys.append(key)

        return list(top_two_keys) 

