"""
Calculator https://www.geogebra.org/m/ExvvrBbR
https://rosettacode.org/wiki/Josephus_problem

Each time a survivor is eliminated,
they skip the next k - 1 people and go directly to the person after the kth person.

To get their new position the formala is:

(old_number - k ) mod n     = new number
(josephus(n, k) - k) mod n  = josephus(n - 1, k)

Binary Josephus Problem:

k = 2

old_number      = 2 * new number
josephus(n, 2)  = 2 * josephus(n / 2, 2)


J(n,k) = (J(n − 1, k) + k ) mod n  | J(1,k)=0
"""

DEBUG = False

class Solution:
    def josephus(self, n: int, k: int) -> int:
        """
        Return the position (1-indexed) of the survivor in Josephus problem.

        n: number of people in the circle
        k: step rate (every k-th person is eliminated)
        """
        return self.solution_1(n, k)

    def solution_1(self, n: int, k: int) -> int:
        rebels = [i + 1 for i in range(n)]

        i = 0
        while len(rebels) > 1:

            left = len(rebels)
            if i > left - 1:
                i = 0

            for j in range(k - 1):
                i += 1
                if i > left - 1:
                    i = 0

            killed = rebels.pop(i)
            if DEBUG:
                print(f"Killed at position {i} survivor {killed} | Left:{rebels}")

        return rebels[0]

    def j_control(self, n, k):
        """use this function as "control" to compare with my solutions
        @credit: https://rosettacode.org/wiki/Josephus_problem#Python
        """
        p, i, seq = list(range(n)), 0, []
        while p:
            i = (i + k - 1) % len(p)
            seq.append(p.pop(i))

        survivor = seq[-1] + 1
        if DEBUG:
            return 'Prisoner killing order: %s.\nSurvivor: %i' % (', '.join(str(i + 1) for i in seq[:-1]), survivor)
        else:
            return survivor


def check(n, k, expected):
    s = Solution()
    got = s.josephus(n, k)
    control = s.j_control(n, k)


    assert got == expected, f"josephus({n}, {k}) → expected {expected}, got {got}"
    assert got == control, f"Control Failure josephus({n}, {k}) → expected {control}, got {got}"

if __name__ == "__main__":
    print(Solution().josephus(13, 3))  # 13 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(Solution().josephus(20, 2))  # 9 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    print(Solution().josephus(6, 7))  # 5 [1, 2, 3, 4, 5, 6]
    print(Solution().j_control(6, 7))  # 5 [1, 2, 3, 4, 5, 6]

    print(Solution().josephus(30, 5))   # 3
    print(Solution().j_control(30, 5))  # 3

    print(Solution().josephus(50, 7))   # 1
    print(Solution().j_control(50, 7))  # 1

    # [1, 2, 3, 4, 5, 6] -> 1
    # [2, 3, 4, 5, 6] -> 3
    # [2, 4, 5] -> 6
    # [4, 5] -> 2
    # [4, 5] -> 2
    # [5] -> 4

    # Specific cases
    check(13, 3, 13)
    check(20, 2, 9)
    check(41, 2, 19)

    # Basic tests (1-indexed survivor)
    check(1, 1, 1)  # Only person 1 survives
    check(5, 2, 3)  # Survivor = 3
    check(7, 3, 4)
    check(10, 1, 10)  # Last person survives

    # Edge cases
    check(2, 2, 1)
    check(6, 7, 5)

    # Larger n
    check(13, 3, 13)
    check(20, 2, 9)
    check(41, 2, 19)
    check(30, 5, 3)
    check(50, 7, 1)
    check(100, 10, 26)
    check(200, 13, 63)
    print("All tests passed!")
