class Solution:
    PARENTHESES_MAP = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    def isValid(self, s: str) -> bool:
        return self.solution_1(s)

    def solution_1(self, s: str) -> bool:
        stack = []
        if len(s) <= 1:  # cannot be true right?
            return False

        for p in s:
            is_opening = p in self.PARENTHESES_MAP
            if is_opening:
                stack.append(p)
                continue

                # we are working with a closing one
            if not stack:
                return False

            next_opened = stack.pop()
            expected_closed = self.PARENTHESES_MAP.get(next_opened, None) == p
            if not expected_closed:
                return False

        # if we got something left means some parenthesis isn't closed
        if stack:
            return False
        return True
