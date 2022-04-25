from collections import deque

def get_knight_shortest_path(x: int, y: int) -> int:
    def get_neighbors(coord):
        # we are going to return a list so we can iterate through our bfs
        res = []
        row, col = coord
        # since the knight has at least 8 moves, then we use the delta to manipulate the movements and see the shortest or shallow distance
        delta_row = [-2, -2, -1, 1, 2, 2, 1, -1]
        delta_col = [-1, 1, 2, 2, 1, -1, -2, -2]
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            #  we dont have to check if the coordinates are in bounds because the chess board is infinite
            res.append((r, c))
        return res

    def bfs(start):
        # initialize the set
        visited = set()
        # intialize count for the knight moves 
        steps = 0
        queue = deque([start])
        while len(queue) > 0:
            #  find length of possible nodes or moves for current step
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                # If the specific coordinates of node = x & y.
                if node[0] == y and node[1] == x:
                    return steps
                for neighbor in get_neighbors(node):
                    r, c = neighbor
                    if neighbor in visited:
                        continue
                    
                    queue.append(neighbor)
                    visited.add(neighbor)
            steps += 1

    return bfs((0, 0))