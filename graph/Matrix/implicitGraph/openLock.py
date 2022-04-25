# Return number of steps to get from 0000 to lock combination

from collections import deque
from typing import List

# create next_digit and previous digit using next digit
#we add ending hash to next-digit since we are going against simple pattern in for loop
next_digit = {**{str(i): str(i + 1) for i in range(9)}, "9": "0"}
# .items() converts digits hash into a tuple that we iterate through
prev_digit = {e: n for n, e in next_digit.items()}

def num_steps(combo: str, trapped_combos: List[str]) -> int:
    # Base case since it would require no steps
    if combo == "0000":
        return 0
    # put trapped combo in set
    trapped_combo_set = set(trapped_combos)
    # bfs map to
    bfs_map = {
        "0000": 0
    }
    # Intialize queue with starting combo
    bfs_queue = deque({"0000"})
    # while queue
    while bfs_queue:
        # pop out starting combo
        top = bfs_queue.popleft()
        for i in range(4):
            # new combo would be 
            first=top[0:i]
            second=next_digit[top[i]]
            third=top[i + 1:]
            # we construct a string using first index of string (0:i)
            # Add next digit by using first character in string as key in our next digit hash to use its value and add everything after current index we on (during first iteration its 0)
            new_combo = top[0:i] + next_digit[top[i]] + top[i + 1:]
            # if this new combo has never been seen then we add it to our queue, add it to our hash as key and set value as original combo key value and add 1 to it to keep track of steps
            if new_combo not in trapped_combo_set and new_combo not in bfs_map:
                bfs_queue.append(new_combo)
                bfs_map[new_combo] = bfs_map[top] + 1
                if new_combo == combo:
                    return bfs_map[new_combo]
            new_combo = top[0:i] + prev_digit[top[i]] + top[i + 1:]
            if new_combo not in trapped_combo_set and new_combo not in bfs_map:
                bfs_queue.append(new_combo)
                bfs_map[new_combo] = bfs_map[top] + 1
                if new_combo == combo:
                    return bfs_map[new_combo]
    return -1
combo = "0202"
trapped_combos = ["0201","0101","0102","1212","2002"]
# num_steps(combo,trapped_combos)
# next_digit2 = {{str(i): str(i + 1) for i in range(9)}, '9':'0'}
prev_digits = {print({e:n}) for n, e in next_digit.items()}
print(prev_digit)
# print(prev_digits)