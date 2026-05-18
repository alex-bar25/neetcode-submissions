class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}
        for i, char in enumerate(order):
            rank[char] = i

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            matched_all = True

            for j in range(min(len(w1), len(w2))):
                if rank[w1[j]] > rank[w2[j]]:
                    return False
                elif rank[w1[j]] < rank[w2[j]]:
                    matched_all = False
                    break
                
            if matched_all and len(w1) > len(w2):
                return False

        return True