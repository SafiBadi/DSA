class Node:
    def __init__(self, dest):
        self.dest = dest
        self.next = None

class Graph:
    def __init__(self, noOfVertex):
        self.v = noOfVertex
        self.graph = [None] * self.v

    def addEdge(self, frm, to):
        n = Node(to)
        n.next = self.graph[frm]
        self.graph[frm] = n

        #For undirected
        n = Node(frm)
        n.next = self.graph[to]
        self.graph[to] = n

    def printGraph(self):
        for i in range(self.v):

            temp = self.graph[i]
            while temp:
                print(temp.dest, " ",end='')
                temp = temp.next
            print("")

myGraph = Graph(5)

myGraph.addEdge(0,3)
myGraph.addEdge(1,3)
myGraph.addEdge(2,3)
myGraph.addEdge(4,3)
myGraph.addEdge(1,4)
myGraph.addEdge(2,4)

myGraph.printGraph()


