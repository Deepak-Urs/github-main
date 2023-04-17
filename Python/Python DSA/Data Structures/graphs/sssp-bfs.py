class Graph:
    def __init__(self, gdict):
        if not gdict:
            gdict = {}
        self.gdict = gdict
    
    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            print('\n start of loop--')
            path = queue.pop(0)
            print('path seen', path)
            node = path[-1]
            print('node seen', node)

            if node == end:
                print('node == end seen')
                return path
            for adjacent in self.gdict.get(node, []):
                print('Adj.connectovity seen', self.gdict[node])
                print('adjacent seen', adjacent)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
                print('new_path seen', new_path)
                print('queue seen', queue)
                print('----')
            print('EOF')

customDict = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"]
}

g = Graph(customDict)
print(g.bfs("a", "e"))