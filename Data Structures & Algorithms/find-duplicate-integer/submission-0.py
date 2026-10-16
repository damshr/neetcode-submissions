class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat the array as a linked list
        slow = nums[0]
        fast = nums[0]
        
        # Phase 1: Find a meeting point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2 : Find the duplicate
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
