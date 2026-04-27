import math

class Solution:
    def isKValid(self, piles: List[int], h: int, k: int):
        total_sum = 0
        for pile in piles:
            total_sum += math.ceil(pile / k)
        if total_sum <= h:
            return True
        else:
            return False 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            # we need to check if k is valid
            if self.isKValid(piles, h, mid) == True:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result