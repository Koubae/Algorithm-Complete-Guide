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

                # we are worknig with a closing one
            if not stack:
                return False

            next_opened = stack.pop()
            expected_closed = self.PARENTHESES_MAP.get(next_opened, None) == p
            if not expected_closed:
                return False

        # if we got something left means some parethesis aren't closed
        if stack:
            return False
        return True

    def solution_x(self, s: str) -> bool:
        def recursion(closing: str, s):
            print(f"closing {closing}, s={s}")
            l = len(s)
            if l == 0:
                return False

            next_para = s[0]
            closes = next_para == closing
            if l == 1:
                return closes

            index = 1
            if closes:
                next_para = s[1]
                # index = 2
            # else:
            # # if closes:
            # #     next_para = s[0]
            # #     index = 1
            # if not closing:
            # closing = self.PARENTHESES_MAP.get(next_para, None)
            # if closing is None:
            #     return False

            closing = self.PARENTHESES_MAP.get(next_para, None)
            if closing is None:
                return False

            print(f"closing={closing} next_para={next_para}, closing={closing}, index={index} closes={closes}")
            # closing_expected = self.PARENTHESES_MAP.get(next_para, None)
            # print(f"closing_expected={closing_expected} next_para={next_para}, index={index} closes={closes}")
            # if closing_expected is None:
            #     return False
            return recursion(closing, s[index:])

            # if next_para == closing:
            #     if l == 1:
            #         return True

            #     next_para = s[1]
            #     closing_expected = self.PARENTHESES_MAP.get(next_para, None)
            #     if closing_expected is None:
            #         return False
            #     print(f"Next para {next_para}, s[2 {s[2:]}")
            #     return recursion(closing_expected, s[2:])

            # if l == 1:
            #     return False

            # closing_expected = self.PARENTHESES_MAP.get(next_para, None)
            # if closing_expected is None:
            #     return False
            # return recursion(closing_expected, s[1:])

        first_para = s[0]
        # solves 1st case where opening brackets are from the start
        closing_expected = self.PARENTHESES_MAP.get(first_para, None)
        if closing_expected is None:
            return False

        result = recursion(closing_expected, s[1:])
        return result
