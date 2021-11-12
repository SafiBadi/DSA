class graph:
    def __init__(self, noofv):
        self.adjmatrix = [[-1]*noofv for x in range(noofv)]

        for i in range(noofv):
            self.adjmatrix[i][i] = 0
        
    def addedge(self, frm , to, weight):
        self.adjmatrix [frm-1] [to-1] = weight
        #self.adjmatrix [to-1] [frm-1] = weight # For undirected graph

    def printmatrix(self):
        for i in self.adjmatrix:
            print(i)

class Solution:
    def dijkstraAlgo(self, graph, startingVertex):

        dijkstra = [1e10 for i in range(len(graph[0]))]
        distance = [-1 for i in range(len(graph[0]))]

        for i in range(len(graph[startingVertex])):
            if graph[startingVertex-1][i] != -1:
                dijkstra[i] = graph[startingVertex-1][i]
        print(dijkstra)
        print(distance)

        minimum = min(dijkstra)
        minindex = dijkstra.index(minimum)
        distance[minindex] = minimum 

        for i in range(len(dijkstra)-1):
            print("h1")
            print("minimum",minimum)
            print(dijkstra)
            print(distance)

            for j in range(len(graph[minindex])):
                if graph[minindex][j] != -1 and distance[j] == -1:
                    if (dijkstra[minindex] + graph[minindex][j]) < dijkstra[j]:
                        dijkstra[j] = dijkstra[minindex] + graph[minindex][j]

                        print(dijkstra)
                        print(distance)

            dijkstra[minindex] = 1e10  

            minimum = min(dijkstra)
            minindex = dijkstra.index(minimum)

            if minimum != 1e10:
                distance[minindex] =  minimum
                
            

        return distance


myGraph = graph(6)

myGraph.addedge(1,4,10)
myGraph.addedge(4,1,10)
myGraph.addedge(1,2,50)
myGraph.addedge(4,5,15)
myGraph.addedge(2,4,15)
myGraph.addedge(5,2,20)
myGraph.addedge(1,3,45)
myGraph.addedge(6,5,3)
myGraph.addedge(2,3,10)
myGraph.addedge(5,3,35)
myGraph.addedge(3,5,30)


myGraph.printmatrix()

ans = Solution()

print("\n", ans.dijkstraAlgo(myGraph.adjmatrix, 1))

