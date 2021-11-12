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

myGraph = Graph(5)

myGraph.addEdge(0,3)
myGraph.addEdge(1,3)
myGraph.addEdge(2,3)
myGraph.addEdge(4,3)
myGraph.addEdge(1,4)
myGraph.addEdge(2,4) 

myGraph.printGraph()


