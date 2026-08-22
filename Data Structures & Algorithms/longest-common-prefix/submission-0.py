class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for word in strs:
            while not word.startswith(res):
                res = res[:-1]

                if res == "":
                    break

        return res