class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {} #declare dict
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in store:
                return [store[difference],i]
            else:
                store[nums[i]] = i #store in dict
            


                


        