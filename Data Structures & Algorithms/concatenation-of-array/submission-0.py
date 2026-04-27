class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums * 2:
            ans.append(num) 

        return ans 