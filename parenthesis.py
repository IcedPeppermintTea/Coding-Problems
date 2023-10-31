"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        valid_brack = [('{', '}'), ('(', ')'), ('[', ']')]
        stack = []
        for i in s:
            # check if the stack is not empty, and
            if (len(stack) > 0 and stack[-1], i) in valid_brack:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0 # if stack is empty, return true