class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char in "([{ ":
                stack.append(char)
            if char in ")]}":
                if not stack:
                    return False
                if stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False

        return not stack