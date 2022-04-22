from collections import deque
from typing import List
def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    # This is the function to tranverse the graph since there is no parent-child relationship in graphs
    def get_neighbors(node: int):
        return graph[node]
    
    def bfs(root: int, target: int):
        # This set it going to keep track of visited nodes, remember to intialize it with root node
        visited = set([root])
        queue = deque([root])
        res =0
        while len(queue) > 0:
            #Dictate how many nodes are in this 'level'
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node == target:
                    return res
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            # at the end of every pass in each level, iterate result to keep track of depth
            res +=1
        def bfs_ans(root: int, target: int):
            queue = deque([root])
            visited = set([root])
            level = 0
            while len(queue) > 0:
                n = len(queue)
                for n in range(n):
                    node = queue.popleft()
                    if node == target:
                        return level
                    for neighbor in get_neighbors(node):
                        if neighbor in visited:
                            continue
                        queue.append(neighbor)
                        visited.add(neighbor)
                level += 1

    return bfs(a, b)