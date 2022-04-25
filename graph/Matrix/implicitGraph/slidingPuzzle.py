from collections import deque
from typing import List

# we are creating the direction in which we can move
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# This is the combo to unlock 
target = ((1, 2, 3), (4, 5, 0))

def num_steps(init_pos: List[List[int]]) -> int:
    # convert array of strings into a tuple because it is not intended to be changed
    init_pos = tuple(tuple(line) for line in init_pos)
    if init_pos == target:
        return 0
    # keep track of amount of moves made
    moves_map = {init_pos: 0}
    # initialize queue with initial position
    moves_queue = deque([init_pos])
    while moves_queue:
        top = moves_queue.popleft()
        row, col = 0, 0
        # iterate through first tuple (top of puzzle)
        for i, line in enumerate(top):
            # iterate through that tops entry values
            for j, entry in enumerate(line):
                # if it contains 0, then set row and col to that coordinate using i and j indexes.
                if entry == 0:
                    row, col = i, j
        for delta_row, delta_col in directions:
            # finding neighbor rows
            new_row, new_col = row + delta_row, col + delta_col
            # If new row and column is inbounds by setting lower and upper bounds
            if new_row >= 0 and new_row < 2 and new_col >= 0 and new_col < 3:
                new_state = list(list(line) for line in top)
                new_state[new_row][new_col], new_state[row][col] = new_state[row][col], new_state[new_row][new_col]
                new_tuples = tuple(tuple(line) for line in new_state)
                if new_tuples not in moves_map:
                    moves_map[new_tuples] = moves_map[top] + 1
                    moves_queue.append(new_tuples)
                    if new_tuples == target:
                        return moves_map[new_tuples]
    return -1
init_pos = [[4, 1, 3], [2, 0, 5]]
num_steps(init_pos)