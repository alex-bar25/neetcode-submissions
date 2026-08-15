class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_1 = {}
        counter_2 = {}

        for char in s:
            if char in counter_1:
                counter_1[char] += 1
            else:
                counter_1[char] = 1

        for char in t:
            if char in counter_2:
                counter_2[char] += 1
            else:
                counter_2[char] = 1

        return counter_1 == counter_2
            