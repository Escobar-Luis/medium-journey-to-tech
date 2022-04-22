from collections import deque
from typing import List

def count_number_of_islands(grid: List[List[int]]) -> int:
    # calculate boundaries of matrix
    num_rows = len(grid)
    num_cols = len(grid[0])

    def get_neighbors(coord):
        res = []
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r, c))
        # Im returning all the neighbors to the current node back to my bfs caller function
        return res

    def bfs(start):
        queue = deque([start])
        r, c = start
        grid[r][c] = 0
        while len(queue) > 0:
            node = queue.popleft()
            # I iterate through the array of neighbors for the current node
            for neighbor in get_neighbors(node):
                r, c = neighbor
                # If my neighbor is 0, ignore
                if grid[r][c] == 0:
                    continue
                # If it's 1, append it to queue and set its value to 0 to mark it as visited
                queue.append(neighbor)
                grid[r][c] = 0

    count = 0
    # bfs starting from each unvisited land cell
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0:
                continue
            bfs((r, c))
            count += 1 # bfs would find 1 connected island, increment count
    return count