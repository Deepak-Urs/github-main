adjList = {}
def adjacencyListGraph():
    # edgesList
    # readList
    # init map
    # populate map

    n = 5
    edgesList = [
        [0,1], [0,4], [1,2], [2,3]
    ]

    for edge in edgesList:
        a, b = edge[0], edge[1]

        if a not in adjList:
            adjList[a] = []
        
        if b not in adjList:
            adjList[b] = []
        
        adjList[a].append(b)
        adjList[b].append(a)
    
    print('adjList-', adjList)

def dfs(node, graph, visited):
    print(node)
    visited[node] = 1

    for nbr in graph[node]:
        if not visited[nbr]:
            dfs(nbr, graph, visited)
    
    

#adjacencyListGraph()
graph = {
    0: [1],
    1: [0],
    4: [2],
    2: [3, 4],
    3: [2]
}
n = 5  # Number of nodes in the graph
visited = [0] * (n + 1)
source = 0
dfs(source, adjList, visited)
