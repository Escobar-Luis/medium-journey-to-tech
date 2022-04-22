from collections import deque
from typing import List

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    # number of rows is the # of arrays within the array of arrays lol
    # number of colums is the # of numbers in an array because they are all equall in this scenario
    num_rows, num_cols = len(image), len(image[0])
    
    def get_neighbors(coord, color):
        # Coordinate is the node
        row, col = coord
        # neighbors starting from north, rotating clockwise(ontop,right,bottom,left) from current node
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        # Get all inbound neighbors(at max 4)
        for i in range(len(delta_row)):
            # get neighbor row by adding the row coordinate with delta row
            neighbor_row = row + delta_row[i]
            # get neighbor col by adding the col coordinate with delta col
            neighbor_col = col + delta_col[i]
            # Make sure calculated neigbor row and column is inbound by neighbor being 0 or greater and less than the num of rows & columns
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                # If inbound, is the color (i.e integer value) of square different from the replacement by equating it to root node original integer?
                if image[neighbor_row][neighbor_col] == color:
                    # If so yield it, not return it so it doesn't exit execution
                    yield neighbor_row, neighbor_col

    def bfs(root):
        queue = deque([root])
        # set all cols and rows to false in visited
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        # break up the root into row and col
        r, c = root
        # Get color integer
        color = image[r][c]
        # We start of by replacing the colorof the root
        image[r][c] = replacement # replace root color
        # set visited to true for that specific coordinate
        visited[r][c] = True
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node, color):
                # remember to keep breaking up the node to row and col
                r, c = neighbor
                # If visited the neighbor, continue to the others
                if visited[r][c]:
                    continue
                # If never visited, than replace the color, append neighbor to queue to check its neighbors later and set visited to true
                image[r][c] = replacement # replace color
                queue.append(neighbor)
                visited[r][c] = True
    # since we are given row and column, we destructure it by using parenthesis
    bfs((r, c))
    # We are returning the modified image, not a new one which is why it is returned outside in main function
    return image