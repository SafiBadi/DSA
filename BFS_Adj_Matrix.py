class graph:
    def __init__(self, noofv):
        self.adjmatrix = [[-1]*noofv for x in range(noofv)]

        for i in range(noofv):
            self.adjmatrix[i][i] = 0
        
    def addedge(self, frm , to, weight):
        self.adjmatrix [frm] [to] = weight
        self.adjmatrix [to] [frm] = weight # For undirected graph

    def printmatrix(self):
        for i in self.adjmatrix:
            print(i)

    # BFS using recursion
    def BFS(self, queue: list, visited: set):
        if len(queue) != 0:
            i = queue.pop(0)
            print(i)
        else:
            return

        for j in range( len(self.adjmatrix[0]) ):
            if self.adjmatrix[i][j] != -1 and j not in visited:
                visited.add(j)
                queue.append(j)
        
        myGraph.BFS(queue, visited)
        
        



myGraph = graph(5)

myGraph.addedge(0,1,10)
myGraph.addedge(1,2,20)
myGraph.addedge(2,4,30)
myGraph.addedge(3,4,40)

myGraph.addedge(1,4,10)
myGraph.addedge(0,4,10)
myGraph.addedge(1,3,10)

myGraph.printmatrix()

myGraph.BFS([0], {0})

