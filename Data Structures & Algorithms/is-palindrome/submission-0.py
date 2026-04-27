class Solution:
    def isPalindrome(self, s: str) -> bool:
        nowhite_s = s.replace(" ", "")
        lower_s = s.lower()
        clean_s = ""

        for c in lower_s:
            if c.isalnum():
                clean_s += c

        left = 0
        right = len(clean_s) - 1

        while left <= right:
            if clean_s[left] != clean_s[right]:
                return False
            
            left += 1
            right -= 1

        return True
