class Graph:
    def __init__(self, noOfVertex):
        self.v = noOfVertex
        self.graph = [[] for i in range(self.v) ]

    def addEdge(self, frm, to):
        self.graph[frm].append(to)

        #For undirected
        self.graph[to].append(frm)

    def printGraph(self):
        for i in self.graph:
            print(i)

    # bfs using loop
    # starting node n
    def bfsOfGraph(self,n):
        bfs = list()
        
        visited = [False for i in range(self.v)]
        q = list()
        
        visited[n] = True
        q.append(n)
        
        while len(q) > 0:
            temp = q.pop(0)
            bfs.append(temp)
            
            for i in self.graph[temp]:
                if visited[i] is False:
                    q.append(i)
                    visited[i] = True
        
        return (bfs)

myGraph = Graph(5)

myGraph.addEdge(0,3)
myGraph.addEdge(1,3)
myGraph.addEdge(2,3)
myGraph.addEdge(4,3)
myGraph.addEdge(1,4)
myGraph.addEdge(2,4) 

myGraph.printGraph()

print(myGraph.bfsOfGraph(0))


