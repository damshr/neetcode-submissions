class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = 1
        while left <= right:
            k = (left + right) // 2
            totalHours = 0

            for p in piles:
                totalHours += math.ceil(p/k)

            if totalHours <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res

