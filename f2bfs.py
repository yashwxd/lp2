def bfs(graph, root):
  visited = set()
  queue = [root]

  while queue:
    vertex = queue.pop(0)
    if vertex not in visited:
      print(vertex, end=' ')
      visited.add(vertex)
      queue.extend(graph[vertex])
# Driver Code
graph = {
  '5': ['3', '7'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': []
}
bfs(graph, '5')  # function calling

"""
def bfs(graph, root):
    visited = set()  # Set to keep track of visited nodes
    queue = [root]  # Initialize the queue with the root node

    while queue:  # Continue the loop as long as the queue is not empty
        vertex = queue.pop(0)  # Remove the element from the front of the queue
        if vertex not in visited:  # Check if the vertex has not been visited before
            print(vertex, end=' ')  # Print the vertex (visited node)
            visited.add(vertex)  # Add the vertex to the visited set

            # Add the unvisited neighbors of the current vertex to the queue
            queue.extend(graph[vertex])


# Driver Code
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
bfs(graph, '5')  # Call the bfs function with the graph and the starting node '5'

"""
