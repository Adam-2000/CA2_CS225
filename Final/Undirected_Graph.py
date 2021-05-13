# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:51:32 2020

@author: 45242
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:09:49 2020

@author: 45242
"""

from pylist import PyList
from fifo_stack import Fifo
import networkx as nx
import matplotlib.pyplot as plt
# Original Definition of Graph Class
class Graph:
    def __init__(self,edges=[]):
        self.vertexList = VertexList(edges)
        for e in edges:
            self.addEdge(e)
            self.addEdge((e[1],e[0]))
    def addEdge(self,edge):
        vertex = self.vertexList.locate(edge[0])
        edgelist = vertex.edges
        if edgelist != None:
            edgelist.add(edge[1])
        else:
            edgelist = EdgeList(edge[1])
        vertex.setEdges(edgelist)
    def __iter__(self):
        vertices = self.vertexList
        for v in vertices:
            x = vertices.locate(v)
            y = x.edges
            if y != None:
                for z in y:
                    yield (v,z)
    def insertVertex(self,item):
        if not (item in self.vertexList):
            self.vertexList.append(item)
    def deleteVertex(self,item):
        return self.vertexList.remove(item)
    def insertEdge(self,edge):
        self.vertexList.addVertex(edge)
        self.addEdge(edge)
        self.addEdge((edge[1],edge[0]))
    def deleteEdge(self,edge):
        self.__deleteEdge(edge)
        self.__deleteEdge((edge[1],edge[0]))
    def __deleteEdge(self,edge):
        if not (edge[0] in self.vertexList):
            print("There is no edge", edge)
            return False
        vertexlocation = self.vertexList.locate(edge[0])
        edgelist = vertexlocation.getEdges()
        if edgelist == None:
            print("There is no edge", edge)
            return False
        res = edgelist.remove(edge[1])
        if res == False:
            print("There is no edge", edge)
        return res
    def outgoingEdges(self,item):
        vertex = self.vertexList.locate(item)
        if vertex == None:
            print("There is no vertex", item)
            return []
        edgelist = vertex.getEdges()
        if edgelist == None:
            return []
        res = []
        for v in edgelist:
            res.append((item,v))
        return res
            # yield (item,v) # If we replace the above two lines with this line, then this methods works as an iterator.
    def bfs(self,vertex):
        if not (vertex in self.vertexList):
            print("There is no vertex", vertex)
            return None
        length = self.vertexList.getlength()
        distance = [None] * length
        parent = [None] * length
        index = self.vertexList.index(vertex)
        distance[index] = 0
        parent[index] = vertex
        currentlayer = Fifo(length)
        currentlayer.pushback(vertex)
        nextlayer = Fifo(length)
        for l in range(length):
            for u in currentlayer:
                #print(u)
                loc = self.vertexList.locate(u)
                edgelist = loc.getEdges()
                if edgelist != None:
                    for v in edgelist:
                        idx = self.vertexList.index(v)
                        if parent[idx] == None:
                            nextlayer.pushback(v)
                            distance[idx] = l + 1
                            parent[idx] = u
            currentlayer = nextlayer
            nextlayer = Fifo(length)
        return (distance,parent)  

    #Alternative DFS traverse using recursion
    def allDFS(self):
        numVertices = self.vertexList.getlength()
        initlist = [None]* numVertices
        self.tree = PyList(initlist,numVertices)
        for i in range(numVertices):
            newgraph = Graph([])
            self.tree[i] = newgraph
        for s in self.vertexList:
            self.mark = [None] * numVertices
            self.dfsPos = 1
            self.dfsNum = [1] * numVertices
            self.finishingTime = 1
            self.finishTime = [1] * numVertices
            idx = self.vertexList.index(s)
            if self.mark[idx] == None:
                self.mark[idx] = s
                self.dfsNum[idx] = self.dfsPos
                self.dfsPos += 1
                self.tree[idx].insertVertex(s)
                self.dfs(s,s,idx)
    def dfs(self,vertex1,vertex2,index):
        for e in self.outgoingEdges(vertex2):
            idx = self.vertexList.index(e[1])
            if self.mark[idx] != None:
                self.__traverseNontreeEdge(e)
            else:
                self.tree[index].insertEdge(e)
                self.__traverseTreeEdge(e)
                self.mark[idx] = e[1]
                self.dfs(vertex2,e[1],index)
        self.backtrack(vertex1,vertex2)
    def __traverseTreeEdge(self,e):
        idx = self.vertexList.index(e[1])
        self.dfsNum[idx] = self.dfsPos
        self.dfsPos += 1
    def __traverseNontreeEdge(self,e):
        self.dfsPos = self.dfsPos
    def backtrack(self,vertex1,vertex2):
        idx = self.vertexList.index(vertex2)
        self.finishTime[idx] = self.finishingTime
        self.finishingTime += 1
        
    def plot_graph(self):
        edges = [e for e in self]
        G = nx.Graph()
        G.add_edges_from(edges)
        print("Print all vertices：{}".format(G.nodes()))
        print("Print all edges：{}".format(G.edges()))
        print("Print the number of edges：{}".format(G.number_of_edges()))
        nx.draw_networkx(G)
        plt.show()
    """
    Ex1_1
    We merge all trees after allDFS. merge means if two trees have same elements, then add edges together
    """
    def cc_undirected(self):
        self.allDFS()
        res = []
        numVertex = self.vertexList.getlength()
        self.marks = [-1] * numVertex
        vertexList = [v for v in self.vertexList]
        for i in range(numVertex):
            root = self.marks[i]
            if root != -1:
                subgraph = self.tree[root] 
                for e in self.outgoingEdges(vertexList[i]):
                    if e not in subgraph:
                        subgraph.addEdge(e)
                        subgraph.addEdge((e[1], e[0]))
            else:
                subtree = self.tree[i]
                for v in subtree.vertexList:
                    idx = self.vertexList.index(v)
                    self.marks[idx] = i
                res.append(subtree)
        return res
        
    
# Definition of VertexList Class
class VertexList:
    class  __Vertex:
        def __init__(self,item,next=None,previous=None):
            self.item=item
            self.next=next
            self.previous=previous
            self.edges=None
        def getItem(self):
            return self.item
        def getNext(self):
            return self.next
        def getPrevious(self):
            return self.previous
        def getEdges(self):
            return self.edges
        def setItem(self,item):
            self.item = item
        def setNext(self,next):
            self.next = next
        def setPrevious(self,previous):
            self.previous = previous
        def setEdges(self,edge):
            self.edges = edge
    
    def __init__(self,edges=[]):
        self.dummy = VertexList.__Vertex(None,None,None)
        self.numVertices = 0
        self.dummy.setNext(self.dummy)
        self.dummy.setPrevious(self.dummy)
        for e in edges:
            self.addVertex(e)
    def __iter__(self):
        cursor = self.dummy
        for i in range(self.numVertices):
            cursor = cursor.getNext()
            yield cursor.getItem()
    def append(self,item):
        lastVertex = self.dummy.getPrevious()
        newVertex = VertexList.__Vertex(item,self.dummy,lastVertex)
        lastVertex.setNext(newVertex)
        self.dummy.setPrevious(newVertex)
        self.numVertices += 1
    def __contains__(self,item):
        cursor = self.dummy
        for i in range(self.numVertices):
            cursor = cursor.getNext()
            vertex = cursor.getItem()
            if vertex == item:
                return True
        return False
    
    def __getitem__(self, index):
        cursor = self.dummy
        for i in range(index + 1):
            cursor = cursor.next
        return cursor.item
    
    def locate(self,vertex):
        cursor = self.dummy
        for i in range(self.numVertices):
            cursor = cursor.getNext()
            item = cursor.getItem()
            if vertex == item:
                return cursor
    def addVertex(self,edge):
        node1 = edge[0]
        node2 = edge[1]
        if not (node1 in self):
            self.append(node1)
        if not (node2 in self):
            self.append(node2)
    def remove(self,item):
        cursor = self.dummy
        location = None
        for i in range(self.numVertices):
            cursor = cursor.getNext()
            vertex = cursor.getItem()
            edgelist = cursor.edges
            if edgelist != None:
                if item in edgelist:
                    print(item, "cannot be deleted, as it appears in an edge.")
                    return False
            if vertex == item:
                location = cursor
        if location == None:
            print(item, "is not a vertex.")
            return False
        nextVertex = location.getNext()
        prevVertex = location.getPrevious()
        prevVertex.setNext(nextVertex)
        nextVertex.setPrevious(prevVertex)
        self.numVertices -= 1
        return True
    def index(self,item):
        cursor = self.dummy
        for i in range(self.numVertices):
            cursor = cursor.getNext()
            if cursor.getItem() == item:
                return i
        return -1
    def getlength(self):
        return self.numVertices


# Definition of EdgeList Class
class EdgeList:
    class __Edge:
        def __init__(self,item,next=None,previous=None):
            self.item=item
            self.next=next
            self.previous=previous
        def getItem(self):
            return self.item
        def getNext(self):
            return self.next
        def getPrevious(self):
            return self.previous
        def setItem(self,item):
            self.item = item
        def setNext(self,next):
            self.next = next
        def setPrevious(self,previous):
            self.previous = previous
    
    def __init__(self,edge):
        self.first = EdgeList.__Edge(edge,None,None)
        self.first.setNext(self.first)
        self.first.setPrevious(self.first)
        self.numEdges = 1
    def add(self,edge):
        lastEdge = self.first.getPrevious()
        newEdge = EdgeList.__Edge(edge,self.first,lastEdge)
        lastEdge.setNext(newEdge)
        self.first.setPrevious(newEdge)
        self.numEdges += 1
    def __iter__(self):
        cursor = self.first
        for i in range(self.numEdges):
            yield cursor.getItem()
            cursor = cursor.getNext()
    def __contains__(self,item):
        cursor = self.first
        for i in range(self.numEdges):
            vertex = cursor.getItem()
            if vertex == item:
                return True
            cursor = cursor.getNext()
        return False
    def remove(self,item):
        cursor = self.first
        for i in range(self.numEdges):
            vertex = cursor.getItem()
            if vertex == item:
                nextVertex = cursor.getNext()
                prevVertex = cursor.getPrevious()
                prevVertex.setNext(nextVertex)
                nextVertex.setPrevious(prevVertex)
                self.numEdges -= 1
                if (cursor == self.first):
                    self.first = nextVertex
                return True
            cursor = cursor.getNext()
        return False


"""
print("Visualization for Ex1_1\n, connected components:")
edges = [(1,2),(2,4),(3,5),(2,5),(1,5),(3,4),(3,1),(6,2),(6,3),(7,8),(8,9),(9,10),(10,8),(12,13)]
g = Graph(edges)

g.plot_graph()
vl = g.vertexList
lv = [v for v in vl]
#la = g.cc_undirected()
#for subgraph in la:
#    subgraph.plot_graph()

"""

    
    
    
    
    
    
    
    