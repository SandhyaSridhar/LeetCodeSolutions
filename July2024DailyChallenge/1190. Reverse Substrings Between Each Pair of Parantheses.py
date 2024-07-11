class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ')':
                rev= ""
                while stack and stack[-1] != '(':
                    rev += stack.pop()
                if stack:
                    stack.pop()
                for c in rev:
                    stack.append(c)
            else:
                stack.append(i)

        return ''.join(stack)
