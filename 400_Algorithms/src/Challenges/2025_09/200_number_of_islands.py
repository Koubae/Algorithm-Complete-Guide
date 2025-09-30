from typing import List

from collections import deque

WATER = "0"
ISLAND = "1"


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS --> search in a grid
        # DFS --> find path or aras in grid

        m = len(grid)
        n = len(grid[0])

        # x,y coord
        island_count: int = 0
        visited: set[tuple[int, int]] = set()

        def dfs_tranverse_island(coords):
            stack = deque([coords])

            while stack:
                coords = stack.pop()
                if coords in visited:
                    continue
                visited.add(coords)

                y, x = coords
                node = grid[y][x]
                if node == WATER:
                    continue

                adjacents = (
                    (y, x - 1),  # left same row
                    (y, x + 1),  # right same row

                    (y - 1, x),  # top
                    (y + 1, x),  # bottom

                    # a diagonal island IS NOT adjacent!
                    # (y - 1, x - 1), # top - left corner
                    # (y - 1, x + 1), # top - right corner

                    # (y + 1, x - 1), # bottom - left corner
                    # (y + 1, x + 1), # bottom - right corner
                )

                for adj in adjacents:
                    if adj in visited:
                        continue

                    y2, x2 = adj
                    if 0 > y2 or y2 > (m - 1) or 0 > x2 or x2 > (n - 1):
                        continue
                    stack.append(adj)

        for y in range(m):
            for x in range(n):
                coords = (y, x)
                if coords in visited:
                    continue

                node = grid[y][x]
                if node == WATER:
                    continue

                dfs_tranverse_island(coords)
                island_count += 1

        return island_count
