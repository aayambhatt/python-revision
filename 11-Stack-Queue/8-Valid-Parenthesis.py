class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for bracket in s:
            if bracket in mapping.values():  # Opening brackets
                stack.append(bracket)
            elif bracket in mapping:  # Closing brackets
                if not stack or stack.pop() != mapping[bracket]:
                    return False
            else:
                # In case of any non-bracket characters (optional)
                return False

        return len(stack) == 0
