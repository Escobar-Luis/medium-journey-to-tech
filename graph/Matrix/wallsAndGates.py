from collections import deque
from typing import List

# These are the possible moves (Up, Right, Down, Left)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

INF = 2147483647

def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    queue = deque()
    n = len(dungeon_map)
    m = len(dungeon_map[0])
    # nested loop, O(n^2) to populate queue with a list of gates (exits) out of dungeon so we can fan out from each gate and update each tile with steps from the closest gate
    for i, row in enumerate(dungeon_map):
        for j, entry in enumerate(row):
            if entry == 0:
                queue.append((i, j))
    # Once queue is populated
    while queue:
        # We popoff a location and calulate all its adjacent or neighboring locations
        row, col = queue.popleft()
        for delta_row, delta_col in directions:
            total_row, total_col = row + delta_row, col + delta_col
            # Upper bound and lower bound of matrix to make sure we don't overstep an edge
            if total_row >= 0 and total_row < n and total_col >= 0 and total_col < m:
                # only add adjacent locations if their value is INF (meaning they are empty and have not been visited)
                if dungeon_map[total_row][total_col] == INF:
                    # similar to knightmoves, we mark the distances on the cells bt adding the value of current cell by one
                    dungeon_map[total_row][total_col] = dungeon_map[row][col] + 1
                    # add the adjacent to the queue to be processed
                    queue.append((total_row, total_col))
    return dungeon_map