def adjacencyMatrixGraph():
    # edgesList
    # readList
    # init matrix
    # populate matrix

    n = 5
    edgesList = [
        [1, 2], [2, 3], [3, 4], [4, 2], [1, 3]
    ]
    adjMat = [[0] * n for _ in range(n)]

    for edge in edgesList:
        a, b = edge[0], edge[1]

        adjMat[a][b] = 1
        adjMat[b][a] = 1
    
    print(adjMat)

adjacencyMatrixGraph()

def adjacencyListGraph():
    # edgesList
    # readList
    # init map
    # populate map

    n = 5
    edgesList = [
        [1, 2], [2, 3], [3, 4], [4, 2], [1, 3]
    ]
    adjList = {}

    for edge in edgesList:
        a, b = edge[0], edge[1]

        if a not in adjList:
            adjList[a] = []
        
        if b not in adjList:
            adjList[b] = []
        
        adjList[a].append(b)
        adjList[b].append(a)
    
    print(adjList)

adjacencyListGraph()