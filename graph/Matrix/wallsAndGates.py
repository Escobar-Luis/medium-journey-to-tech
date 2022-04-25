from collections import deque
from typing import List

# These are the possible moves (Right, Down, Left, Up)
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

dungeon_map = [
  [INF, -1, 0, INF],
  [INF, INF, INF, -1],
  [INF, -1, INF, -1],
  [0, -1, INF, INF],
]

def map_gate_distance(dungeon_map: List[List[int]]) -> List[List[int]]:
    queue = deque()
    nums_rows = len(dungeon_map)
    nums_cols = len(dungeon_map[0])
    # nested loop, O(n^2) to populate queue with a list of gates (exits) out of dungeon so we can fan out from each gate and update each tile with steps from the closest gate
    for i, row in enumerate(dungeon_map):
        for j, entry in enumerate(row):
            if entry == 0:
                queue.append((i, j))
        # we have a queue containg the row and column of every gate in our matrix
    while queue:
        row,col = queue.popleft()
        for delta_row,delta_col in directions:
            adj_row,adj_col= row + delta_row, col + delta_col
            # If the neighboring square is not an obstacle (-1) and is inbounds
            if adj_row >=0 and adj_row<nums_rows and adj_col>=0 and adj_col<nums_cols:
                # Only add to queue if we found an empty sapce
                if dungeon_map[adj_row][adj_col] == INF:
                    # we set the neighbor to our previous step count and add 1 to it (our first iteration is from gate wo we would be starting from 0)
                    dungeon_map[adj_row][adj_col] = dungeon_map[row][col] + 1
                    # add the neighbor coordinate to queue to find its neighbors and see what the next move is, if any
                    queue.append((adj_row, adj_col))
                
map_gate_distance(dungeon_map)