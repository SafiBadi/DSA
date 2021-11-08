class graph:
    def __init__(self, noofv):
        self.adjmatrix = [[-1]*noofv for x in range(noofv)]
        
    def addedge(self, frm , to, weight):
        self.adjmatrix [frm] [to] = weight
        self.adjmatrix [to] [frm] = weight # For undirected graph

    def printmatrix(self):
        for i in self.adjmatrix:
            print(i)

myGraph = graph(5)

myGraph.addedge(0,1,10)
myGraph.addedge(1,2,20)
myGraph.addedge(2,4,30)
myGraph.addedge(3,4,40)

myGraph.printmatrix()

