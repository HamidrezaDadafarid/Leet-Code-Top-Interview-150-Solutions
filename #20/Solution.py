class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_parenthesis = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in matching_parenthesis.values():
                stack.append(c)
            elif c in matching_parenthesis:
                if stack and stack[-1] == matching_parenthesis[c]:
                    stack.pop()
                else:
                    return False
            else:
                return False  # This handles any invalid characters

        return len(stack) == 0
