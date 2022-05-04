from collections import deque
from typing import List

# similar to delta coordinates from matrix tranversing, so we can loop through each direction in the list to get neighbor coordinates
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# This is the combo we must arrange our init_pos too.
target = ((1, 2, 3), (4, 5, 0))

def num_steps(init_pos: List[List[int]]) -> int:
    # use tuple because it is immutable
    init_pos = tuple(tuple(line) for line in init_pos)
    # Handle lucky base case
    if init_pos == target:
        return 0
    # use map to keep track of moves
    moves_map = {init_pos: 0}
    # Fifo, we enque the queue with the init_pos
    moves_queue = deque([init_pos])
    # while loop to exhaust all possible moves to get position == target
    while moves_queue:
        # remove the first state of our current puzzle from queue 
        top = moves_queue.popleft()
        #think of these as the pointers to get values & tranverse through each line
        row, col = 0, 0
        # for index of every row in this scenario
        for i, line in enumerate(top):
            # use j to iterate through every character or column of every row
            for j, entry in enumerate(line):
                # if the character is ==0, then we set the row to i and column to j because that is the empty space
                if entry == 0:
                    row, col = i, j
        # once we iterated through a row, we are going to find our neighbors to that empty space so we know which characters we can move
        for delta_row, delta_col in directions:
            # add our row and col to our delta
            new_row, new_col = row + delta_row, col + delta_col
            # as long as this new row is in bounds
            if new_row >= 0 and new_row < 2 and new_col >= 0 and new_col < 3:
                # my new_state or init-pos is initialized to a copy of our top but as a list since we can mutate it
                new_state = list(list(line) for line in top)
                # since 0 represents empty space, we set the piece we are moving to the empty space and the empty space to the piece we moved
                new_state[new_row][new_col], new_state[row][col] = new_state[row][col], new_state[new_row][new_col]
                # we mutated our state so we contruct new tuple
                new_tuples = tuple(tuple(line) for line in new_state)
                # check if this move has been done before
                if new_tuples not in moves_map:
                    # add it to our moves by adding one to the previous moves count tracker which is the value for every key/move in our hash
                    moves_map[new_tuples] = moves_map[top] + 1
                    # add this new state of positioned elements into our queue so we can test out all next moves from it
                    moves_queue.append(new_tuples)
                    # check if new_state is the target we want to so we return its value which is the count of steps it took to achieve it
                    if new_tuples == target:
                        return moves_map[new_tuples]
    # if nothing returns,then return -1
    return -1
num_steps([[4, 1, 3], [2, 0, 5]])