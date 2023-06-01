graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
visited = set()  # List for visited nodes.
def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour)


dfs(visited, graph, '5')

'''
graph = {
    '5': ['3', '7'],   # Node '5' has neighbors '3' and '7'
    '3': ['2', '4'],   # Node '3' has neighbors '2' and '4'
    '7': ['8'],        # Node '7' has neighbor '8'
    '2': [],           # Node '2' has no neighbors
    '4': ['8'],        # Node '4' has neighbor '8'
    '8': []            # Node '8' has no neighbors
}

visited = set()  # Set to keep track of visited nodes

def dfs(visited, graph, root):
    if root not in visited:  # If the current node is not visited
        print(root)         # Print the current node
        visited.add(root)   # Add the current node to the visited set
        for neighbour in graph[root]:  # Iterate over each neighbor of the current node
            dfs(visited, graph, neighbour)  # Recursively call dfs with the neighbor as the new root

dfs(visited, graph, '5')  # Start DFS from node '5'

'''
