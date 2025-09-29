from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Really bad performance"""
        n = len(intervals)
        if n == 1:
            return intervals

        results = []

        i = 0
        while i <= (n - 1):
            interval = intervals[i]

            merged = None
            to_remove = []
            for j, other in enumerate(results):
                left = interval
                right = other
                if left[0] > right[0]:  # move interval with lower bound to the left always
                    left, right = right, left

                if left[1] >= right[0]:
                    merged = [min(left[0], right[0]), max(left[1], right[1])]
                    interval = merged
                    to_remove.append(j)

            if not merged:
                results.append(interval)
            else:
                print(f"To remove {to_remove} | results={results}")
                results_temp = []
                for j, r in enumerate(results):
                    if j in to_remove:
                        continue
                    results_temp.append(r)
                results = results_temp
                results.append(merged)

            i += 1

        return results
