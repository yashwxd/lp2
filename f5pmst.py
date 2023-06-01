from heapq import heappush, heappop

def prim(graph):
    visited = set()
    heap = [(0, list(graph.keys())[0])]
    while heap:
        (cost, node) = heappop(heap)
        if node not in visited:
            visited.add(node)
            for (next_node, c) in graph[node].items():
                if next_node not in visited:
                    heappush(heap, (c, next_node))
    return visited

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4},
    'C': {'A': 3, 'B': 4},
}

mst = prim(graph)
print("Minimum Spanning Tree:", mst)

"""

from heapq import heappush, heappop

def prim(graph):
    visited = set()  # Set to keep track of visited nodes
    heap = [(0, list(graph.keys())[0])]  # Heap to store nodes with their corresponding costs
    while heap:
        (cost, node) = heappop(heap)  # Pop the node with the minimum cost from the heap
        if node not in visited:  # If the node has not been visited yet
            visited.add(node)  # Mark the node as visited
            for (next_node, c) in graph[node].items():  # Iterate over the neighbors of the current node
                if next_node not in visited:  # If the neighbor has not been visited
                    heappush(heap, (c, next_node))  # Add the neighbor to the heap with its cost
    return visited  # Return the set of visited nodes, representing the minimum spanning tree

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4},
    'C': {'A': 3, 'B': 4},
}

mst = prim(graph)
print("Minimum Spanning Tree:", mst)

"""
