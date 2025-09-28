from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.chat_gpt(nums, target)

    def chat_gpt(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}
        for i, x in enumerate(nums):
            j = seen.get(target - x)
            if j is not None:
                return [i, j]

            if x not in seen:  # keep earlist to handle duplicates
                seen[x] = i

    def solution_2_using_2_points_and_cache(self, nums: List[int], target: int) -> List[int]:
        """
        - time Complexity O(log^2 N) -- logarithmic
        - Space Complexity O(N^2) -- quadratic?

        """

        l = len(nums)
        left = 0
        right = l - 1
        seen = dict()  # for caching value -> index mapping
        while left <= right:
            left_value = nums[left]
            if left == right:
                right_value = -999
            else:
                right_value = nums[right]

            if (left_value + right_value) == target:  # if we lucky we find the answer already
                return [left, right]

            left_diff = target - left_value
            right_diff = target - right_value

            if left_diff in seen:
                j = seen[left_diff]
                return [left, j]
            if right_diff in seen:
                j = seen[right_diff]
                return [right, j]

            seen[left_value] = left
            seen[right_value] = right

            left += 1
            right -= 1

    def naive_solution(self, nums: List[int], target: int) -> List[int]:
        """
        - Time Complexity(N^2) (Quadratic)
        - Space Complexity O(N)
        """
        for i in range(len(nums)):
            value = nums[i]
            diff = target - value

            try:
                j = nums.index(diff, i + 1)
                return [i, j]
            except ValueError:
                pass
