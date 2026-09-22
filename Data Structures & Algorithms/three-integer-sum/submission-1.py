class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort() #helps to skip duplicates
        res = []


        for i, a in enumerate(nums):
            if a > 0:
                break #remaining numbers positive
            if i > 0 and a == nums[i - 1]: #to skip duplicates
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0 :
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    #Don't add the same triplet multiple times.
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1 
        return res

