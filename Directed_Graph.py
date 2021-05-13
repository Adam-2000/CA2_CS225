# -*- coding: utf-8 -*-
"""
Created on Sat May 23 18:38:11 2020

@author: 45242
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:07:35 2020

@author: 45242
"""
#from pylist import PyList
import networkx as nx
import matplotlib.pyplot as plt
# (i) Modified DiGraph class from Graph Class
class DiGraph:
    def __init__(self,edges=[]):
        self.vertexList = VertexList(edges)
        for e in edges:
            self.addEdge(e)

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
    def deleteEdge(self,edge):
        self.__deleteEdge(edge)
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

    #DFS traverse using recursion
    def allDFS(self):
        numVertices = self.vertexList.getlength()
        initlist = [None]* numVertices
        self.tree = initlist
        for i in range(numVertices):
            newgraph = DiGraph([])
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
                self.dfs(s,idx)
    def dfs(self,vertex,index):
        for e in self.outgoingEdges(vertex):
            idx = self.vertexList.index(e[1])
            if self.mark[idx] == None:
                self.tree[index].insertEdge(e)
                self.__traverseTreeEdge(e)
                self.mark[idx] = e[1]
                self.dfs(e[1],index)
        self.backtrack(vertex)
    def __traverseTreeEdge(self,e):
        idx = self.vertexList.index(e[1])
        self.dfsNum[idx] = self.dfsPos
        self.dfsPos += 1
    def backtrack(self,vertex):
        idx = self.vertexList.index(vertex)
        self.finishTime[idx] = self.finishingTime
        self.finishingTime += 1
            
    def plot_digraph(self):
        edges = [e for e in self]
        vertices = [v for v in self.vertexList]
        G = nx.DiGraph()
        G.add_nodes_from(vertices)
        G.add_edges_from(edges)
        print("Print all vertices：{}".format(G.nodes()))
        print("Print all edges：{}".format(G.edges()))
        print("Print the number of edges：{}".format(G.number_of_edges()))
        nx.draw_networkx(G)
        plt.show()
        
    """
    Ex1_2
    We use Kosaraju algorithm, first DFSall to have a forest,
    iterate the tree in the forest
    if the root is not marked, then a new component is create, for those children who appeared in the tree and the inverse_tree,
    mark them and add them to the component
    if the root is marked, then add more edges to the corresponding components
    """    
    def inverted_graph(self):
        g = DiGraph()
        for e in self:
            g.insertEdge((e[1], e[0]))
        return g
    
    def cc_digraph(self):
        invgraph = self.inverted_graph()
        numVertex = self.vertexList.getlength()
        res = []
        count = 0
        self.marks = [-1] * numVertex
        self.allDFS()
        invgraph.allDFS()
        vertexList = [v for v in self.vertexList]
        for i in range(numVertex):
            subtree = self.tree[i]
            vertex = vertexList[i]
            if self.marks[i] == -1:
                self.marks[i] = count
                ansgraph = DiGraph()
                ansgraph.insertVertex(vertex)
                invidx = invgraph.vertexList.index(vertex)
                invsubtree = invgraph.tree[invidx]
                edges = [e for e in subtree]
                #subtree.plot_digraph()
                #invsubtree.plot_digraph()
                for v in invsubtree.vertexList:
                    for e in edges:
                        if v == e[1]:
                            ansgraph.insertEdge(e)
                            self.marks[self.vertexList.index(v)] = count
                            break
                count += 1
                #ansgraph.plot_digraph()
                res.append(ansgraph)
            else:
                subgraph = res[self.marks[i]]
                for e in self.outgoingEdges(vertex):
                    if e[1] in subgraph.vertexList:
                        if e not in subgraph:
                            subgraph.addEdge(e)
                
        return res        
                
                

# Definition of VertexList Class, a linked list
class VertexList:
    class  __Vertex:
        def __init__(self,item,next=None,previous=None):
            self.item=item # the vertex content
            self.next=next
            self.previous=previous
            self.edges=None # vertices related to this vertex
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
    # locate the vertex location using its vertex value
    def locate(self,vertex): 
        cursor = self.dummy
        for i in range(self.numVertices):
            cursor = cursor.getNext()
            item = cursor.getItem()
            if vertex == item:
                return cursor
    # add new vertex if possible for the new edge
    def addVertex(self,edge):
        node1 = edge[0]
        node2 = edge[1]
        if not (node1 in self):
            self.append(node1)
        if not (node2 in self):
            self.append(node2)
    # remove a vertex
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
    
# Definition of EdgeList Class, also a linked list
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
print("test for Ex1_2")
edges = [(1,2),(1,3),(1,4),(2,1),(2,5),(2,6),(3,2),(3,1),(3,6),(4,1),(4,7),(6,5),(7,8),(8,1),(8,4)]
g = DiGraph(edges)
g.plot_digraph()

lb = g.cc_digraph()
for subgraph in lb:
    subgraph.plot_digraph()
"""

    
    

