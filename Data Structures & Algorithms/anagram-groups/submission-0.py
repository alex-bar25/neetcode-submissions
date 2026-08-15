class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = {}
        ans = []

        for word in strs:
            key = "".join(sorted(word))

            if key not in counter:
                counter[key] = []

            counter[key].append(word)

        for vals in counter.values():
            ans.append(vals)

        return ans

        

            
        