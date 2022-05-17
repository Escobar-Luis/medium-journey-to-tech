from collections import deque
from typing import List

def sequence_reconstruction(original: List[int], seqs: List[List[int]]) -> bool:
    def count_parents(graph):
        counts = { node: 0 for node in graph }
        #How may times this node is a child to a parent
        for parent in graph:
            for node in graph[parent]:
                counts[node] += 1
        return counts


    def topo_sort(graph):
        seq = []
        q = deque()
        counts = count_parents(graph)
        for node in counts:
            if counts[node] == 0:
                q.append(node)
        while len(q) > 0:
            # If there are 2 itmes in queue, meaning 2 nodes had a count of 0 then the sequence cannot be unique
            if len(q) > 1: # if there's > 1 item, then the recontruction is not unique
                return False
            node = q.popleft()
            seq.append(node)
            # decrement the counts all of this nodes children
            for child in graph[node]:
                counts[child] -= 1
                if counts[child] == 0:
                    q.append(child)
        # if sequence is equal to original than true, otherwise false
        return seq == original

    # Create the graph from the sequences
    # The orginal sequence is a permutation of the integers from 1 to n
    n = len(original)
    # 1+n to stop at actual length of n since the stop parameter is not included
    graph = { node: set() for node in range(1, 1 + n) } # nodes from 1 to n
    # for each sequence
    for seq in seqs:
        # for each number in the sequence (accessing them by index)
        for i in range(len(seq) - 1): # create an edge for each adjancent pairs
            # take the current number to access in graph and add the destination which would be the number that comes after
            source, destination = seq[i], seq[i + 1]
            graph[source].add(destination)
    return topo_sort(graph)

sequence_reconstruction([1,2,3],[[1,2], [1,3], [2,3]])