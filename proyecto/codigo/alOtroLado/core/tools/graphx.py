from collections import deque 
class node():
    def __init__(self,value, weight):
        self.value=value
        self.weight=weight
        self.next=None

class Graph:
    def __init__(self):
        self.graph={}            

    def addEdges(self,source,dest, weight): 
        vert=node(dest, weight)
        if source in self.graph:
            self.graph[source]=self.graph[source].append(vert)
            vert.next=self.graph[source]
        else:
            self.graph[source]=[vert]
        vertice.next=self.graph[source]
        self.graph[source]= vertice
