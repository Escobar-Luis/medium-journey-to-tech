from collections import deque
from typing import List

def count_number_of_islands(grid: List[List[int]]) -> int:
    # calculate boundaries of matrix
    # this essentially is me constructing the grid to access using index notation diffeent areas of the grid to give me the value of the object
    num_rows = len(grid)
    num_cols = len(grid[0])
# this is an iterative function taking the result as the iterable
    def get_neighbors(coord):
        res = []
        row, col = coord
        # clockwize notation to tranverse without any adjacents, only veritcal and horizontal
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r, c))
        # Im returning all the neighbors to the current node back to my bfs caller function
        return res
# so the root doesnt matter if it is intialized as r,c you can set it as w.e and destructure it as so
    def bfs(start):
        queue = deque([start])
        r, c = start
        # this is the same as doing visited[r][c]=True but 0.
        grid[r][c] = 0
        while len(queue) > 0:
            # in an interview, i can just pop it to the right and make the function dfs
            node = queue.popleft()
            # I iterate through the array of neighbors for the current node
            for neighbor in get_neighbors(node):
                r, c = neighbor
                # If my neighbor is 0, ignore, then im using the values of the neighbors to judge it its 1
                if grid[r][c] == 0:
                    continue
                # If it's 1, append it to queue and set its value to 0 to mark it as visited
                queue.append(neighbor)
                grid[r][c] = 0
# this count keeps track of the isalnds found 
    count = 0
    # bfs starting from each unvisited land cell, nd we call this iteratvely on every cell
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0:
                continue
            bfs((r, c))
            count += 1 # bfs would find 1 connected island, increment count
    return count