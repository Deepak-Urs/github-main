from collections import deque, defaultdict

adjList = {}
def adjacencyListGraph():
    # edgesList
    # readList
    # init map
    # populate map

    n = 5
    edgesList = [
        [0,1], [1,4], [1,2], [2,3]
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

def bfs(source, graph, n):
    q = deque()
    visited = [0] * (n+1)

    q.append(source)
    visited[source] = 1

    while q:
        f = q.popleft()
        print(f)
        for nbr in graph[f]:
            if not visited[nbr]:
                visited[nbr] = 1
                q.append(nbr)

adjacencyListGraph()
bfs(0, adjList, 5)
