class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ans = []

        for op in operations:
            if op.lstrip('-').isdigit():
                stack.append(int(op))
            elif op == "+":
                stack.append(int(stack[-1] + stack[-2]))
            elif op == "D":
                stack.append(int(stack[-1] * 2))
            elif op == "C":
                stack.pop()

        return sum(stack)