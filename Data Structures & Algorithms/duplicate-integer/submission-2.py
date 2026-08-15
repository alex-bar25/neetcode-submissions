class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        for num in counter.keys():
            if counter[num] >= 2:
                return True

        return False