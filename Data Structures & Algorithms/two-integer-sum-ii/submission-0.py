class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in store:
                return [store[difference] + 1,i + 1]
            else:
                store[numbers[i]] = i
                

        