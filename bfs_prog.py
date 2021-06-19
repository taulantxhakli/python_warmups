# BFS Program, CS 300
# @author Taulant Xhakli
# @version 1.0

graph = {
  'Sparkill' : ['New York','Detroit'],
  'New York' : ['Boston', 'Washington'],
  'Detroit' : ['Miami'],
  'Boston' : [],
  'Washington' : ['Miami'],
  'Miami' : []
}

visited = []
queue = []

def BFS(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver
BFS(visited, graph, 'Sparkill')
