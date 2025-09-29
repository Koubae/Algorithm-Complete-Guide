from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        time: O(n) Linear
        space: O(n)
        """
        n = len(s)
        if n <= 1:
            return n

        if set(s) == 1:  # if string is just one char
            return 1

        window = deque()
        seen = set()
        best = 0
        for ch in s:
            while ch in seen:  # O(1) membership via set
                rem = window.popleft()
                seen.remove(rem)

            window.append(ch)
            seen.add(ch)
            best = max(best, len(window))
        return best

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
        time: O(n^2) Quadratic
        space: O(n)
        """
        n = len(s)
        if n <= 1:
            return n

        if set(s) == 1:  # if string is just one char
            return 1

        longest = 1
        substring = deque([s[0]])
        for char in s[1:]:
            is_duplicate = char in substring
            if is_duplicate:
                # remove till we find duplicate
                for _ in range(len(substring)):
                    rem = substring.popleft()
                    if rem == char:
                        break
            substring.append(char)
            n2 = len(substring)
            if n2 > longest:
                longest = n2

        return longest

    def lengthOfLongestSubstring1(self, s: str) -> int:
        """
        time: O(n^2) Quadratic
        space: O(log n log)
        """
        n = len(s)
        if n <= 1:
            return n

        if set(s) == 1:  # if string is just one char
            return 1

        longest = 1
        substring = list(s[0])
        for char in s[1:]:
            is_duplicate = char in substring
            if is_duplicate:
                # remove till we find duplicate
                for _ in range(len(substring)):
                    rem = substring.pop(0)
                    if rem == char:
                        break
            substring.append(char)
            n2 = len(substring)
            if n2 > longest:
                longest = n2

        return longest
