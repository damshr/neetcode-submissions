class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #create a set

        for num in nums:
            if num in seen:
                return True #no. is in set return true
            seen.add(num)#no.not in set add to the set
        return False #if no duplicate return false
        
        