class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        seen = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != seen[ch]:
                    return False

        return len(stack) == 0
