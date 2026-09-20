class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1 #start new sequence
                while (num + length) in numSet:
                    length = length + 1 #increase length of the sequence
                longest = max(length,longest)
        return longest
            