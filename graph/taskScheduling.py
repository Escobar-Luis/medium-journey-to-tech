from collections import deque
from typing import List

# This is a helper function to find out how many times a task(parent) is required(other nodes point to itf)
# In this scenario, b is being pointed by 2 other nodes
def count_parents(graph):
    # im creating a new hash using the keys in my task hash as keys again but setting their value to 0 as starting value for counter
    counts = { node: 0 for node in graph }
    # for key in graph 
    for parent in graph:
        # for the value in the key
        for node in graph[parent]: 
                # use that value to access my count hash and iterate its count by 1 
            counts[node] += 1
    return counts


def topo_sort(graph):
    res = []
    q = deque()
    # Get my counts using helper function
    counts = count_parents(graph)
    # for every key in counts
    for node in counts:
        if counts[node] == 0:
            q.append(node)
    while len(q) > 0:
        node = q.popleft()
        res.append(node)
        # for child to the parent (for the task that needs to be done after a task)
        for child in graph[node]:
            counts[child] -= 1
            if counts[child] == 0:
                q.append(child)
    return res if len(graph) == len(res) else None

def task_scheduling(tasks: List[str], requirements: List[List[str]]) -> List[str]:
    # Hash using each task as key and setting its initial value to an empty list
    graph = {t: [] for t in tasks}
    # im appending which tasks have to go before my task in my hash
    for a, b in requirements:
        graph[a].append(b)
    print(graph)
    return topo_sort(graph)

tasks = ["a", "b", "c", "d"]
requirements = [["a", "b"], ["c", "b"], ["b", "d"]]

task_scheduling(tasks,requirements)