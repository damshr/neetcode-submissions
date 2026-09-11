class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        count = {} #counts how many times each no. appears
        freq = [[] for i in range (len(nums) + 1)] #freq array length must be equal to the original array length as max freq = len(input array)
        # also frequency can be equal to the length of the array.
        for n in nums:
            #count occurrence
            count[n] = 1 + count.get(n,0)
        for n,c in count.items(): #got thr each value counted
            freq[c].append(n) #n occurs c no. of times, put in freq bucket
        res = []
        for i in range (len(freq) - 1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



        