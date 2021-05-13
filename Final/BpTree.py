# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:47:04 2020

@author: 45242
"""
from heap import heapsort
class Block():
    def __init__(self, size, keyrange):
        self.size = size
        self.keyrange = keyrange
        self.tuples = [None] * size
        self.numtuples = 0
        self.numGaps = 0
    class __Placeholder:
        def __init__(self):
            pass
        def __eq__(self,other):
            return False
    def __getitem__(self,idx):
        return self.tuples[idx]
    def __setitem__(self,idx,t):
        self.tuples[idx] = t
    def getnumtuples(self):
        return self.numtuples
    def setnumtuples(self, n):
        self.numtuples = n
    def getKey(self, idx):
        item = self.tuples[idx]
        if item == None or type(item) == Block.__Placeholder:
            return None
        if type(self.keyrange) == int:
            return item[:self.keyrange]
        else:
            key = []
            for i in self.keyrange:
                key.append(item[i])
            return key
    def retrieve(self,idx):
        return self.tuples[idx]
    def __repr__(self):
        return str(self.tuples)
    
class MainBlock(Block):
    def find(self, key):
        if self.numtuples == 0:
            #print("Empty main Block:", key)
            return -1
        maxidx = self.numGaps + self.numtuples - 1
        for i in range(maxidx+1):
            if self.getKey(i) == key:
                return i
        return -1
    class __Placeholder:
        def __init__(self):
            pass
        def __eq__(self,other):
            return False
    def getKey(self, idx):
        item = self.tuples[idx]
        if item == None or type(item) == MainBlock.__Placeholder:
            return None
        if type(self.keyrange) == int:
            return item[:self.keyrange]
        else:
            key = []
            for i in self.keyrange:
                key.append(item[i])
            return key

    def delete(self, key):
        idx = self.find(key)
        if idx == -1:
            return False
        self[idx] = MainBlock.__Placeholder()
        self.numGaps += 1
        self.numtuples -= 1
        return True
        
class OverflowBlock(Block):
    def find(self, key):
        for i in range(self.size):
            if self.getKey(i) == key:
                return i
        #print("Key not found in overflow block:", key)
        return -1
    def append(self, item):
        for i in range(self.size):
            if self[i] == None:
                self[i] = item
                break
        self.numtuples += 1
    def delete(self, key):
        idx = self.find(key)
        if idx == -1:
            return False
        self[idx] = None
        self.numtuples -= 1
        return True
    
class LeafNode():
    def __init__(self, parent, size, keyrange, left = None, right = None):
        self.size = size
        self.keyrange = keyrange
        self.parent = parent
        self.left = left
        self.right = right
        self.main = MainBlock(size, keyrange)
        self.overflow = OverflowBlock(size, keyrange)
        self.numTuples = 0
    def pr_print(self,number = "Undefined"):
        print("________________________________")
        print("Leaf Node #",number)
        print(self)
        print("Parent node:", self.getParent())
        print("left,right:", self.left, self.right)
        print("MainBlockNum:", self.main.numtuples)
        print("MainBlock:")
        print(self.main)
        print("OverBlockNum:", self.overflow.numtuples)
        print("Overflow Block:")
        print(self.overflow)
        print("--------------------------------")
    def getnumTuples(self):
        return self.numTuples
    def setnumTuples(self, n):
        self.numTuples = n
        self.main.setnumtuples(n)
    def getParent(self):
        return self.parent
    def setParent(self,parent):
        self.parent = parent
    def getKey(self,index):
        return self.main.getKey(index)
    def getData(self,index):
        return self.main[index]
    def __getitem__(self,idx):
        return self.main[idx]
    def __setitem__(self,idx,t):
        self.main.tuples[idx] = t
    def find(self, key):
        res = self.main.find(key)
        if res == -1:
            res = self.overflow.find(key)
            if res == -1:
                #print("Key Not Found in LeafNode:", key)
                return (self, -1)
            res = self.overflow[res]
        else:
            res = self.main[res]
        return (self, res)
    def reorganize(self):
        newMainBlock = MainBlock(self.size, self.keyrange)
        newOverflowBlock = OverflowBlock(self.size, self.keyrange)
        newlist = []
        for i in range(self.main.numtuples + self.main.numGaps):
            item = self.main.tuples[i]
            if self.main.getKey(i) != None:
                newlist.append((self.main.getKey(i), item))
        for i in range(self.overflow.size):
            item = self.overflow.tuples[i]
            if item != None:
                newlist.append((self.overflow.getKey(i), item))
        newlist = heapsort(newlist)
        newlen = len(newlist)
        for i in range(newlen):
            newMainBlock[i] = newlist[i][1]
        newMainBlock.numtuples = newlen
        self.main = newMainBlock
        #print("self.main",self.main)
        self.overflow = newOverflowBlock 
    def split(self):
        self.reorganize()
        length = self.numTuples
        mid = self.size // 2
        newkey = self.getKey(mid)
        newroot = None
        if self.parent == None:
            newroot = Non_LNode(self.size + 1)
            self.parent = newroot
        newnode = LeafNode(self.parent, self.size, self.keyrange, self, self.right)
        if self.right != None:
            self.right.left = newnode
        self.right = newnode
        for i in range(mid, self.main.numtuples):
            newnode.main[i - mid] = self.main[i]
            self.main[i] = None
        newnode.numTuples = length - mid
        newnode.main.numtuples = length - mid
        self.numTuples = mid
        self.main.numtuples = mid
        if newroot != None:
            self.parent.setKey(1, newkey) 
            self.parent.setnumKeys(1)
            self.parent.setChild(0, self)
            self.parent.setChild(1, newnode)
            return 0
        return (newkey, newnode)
    
    def insert(self, item):
        self.overflow.append(item)
        self.numTuples += 1
        if self.numTuples == self.size:
            res = self.split()
            if res == 0:
                return self.parent
            return self.parent.insert(res[0], res[1])
        if self.overflow.numtuples >= self.size // 2:
                self.reorganize()
        return None
    
    def __merge(node1,node2):
        numitems = node1.getnumTuples() + node2.getnumTuples()
        med = numitems // 2 
        if node1.getnumTuples() < node2.getnumTuples():
            num1 = node1.getnumTuples()
            node1.setnumTuples(med)
            for i in range(num1, med):
                node1[i] = node2[i-num1]
            k = node2.getKey(med - num1)
            num2 = numitems - med
            for i in range(0,num2):
                node2[i] = node2[i + med - num1]
            node2.setnumTuples(num2)
            return k
        k = node1.getKey(med)
        num2 = numitems - med
        for i in range(node2.getnumTuples() - 1, -1, -1):
            node2[i+num2-node2.getnumTuples()] = node2.getKey(i)
        for i in range(0, num2-node2.getnumTuples()):
            node2[i] =  node1[i+med]
        node1.setnumTuples(med)
        node2.setnumTuples(num2)
        return k
    def delete(self, key):
        if not self.main.delete(key): 
            if not self.overflow.delete(key):
                raise KeyError("Key Not Found for deletion in leaf:", key)
                return None
        self.numTuples -= 1
        if self.numTuples < self.size // 2:
            self.reorganize()
            parent = self.getParent()
            if parent == None:
                if self.getnumTuples() == 0:
                    print("B+-tree is empty")
                return None
            else:
                left = parent.leftsibling(self)
                right = parent.rightsibling(self)
            if left != None:
                leftSibling = left[0]
                sepleft = left[1]
            else:
                leftSibling = None
            if right != None:
                rightSibling = right[0]
                sepright = right[1]
            else:
                rightSibling = None
            if self.parent != None and self.getnumTuples() < self.size // 2:
                if leftSibling != None and leftSibling.getnumTuples() > self.size // 2:
                    leftSibling.reorganize()
                    newKey = LeafNode.__merge(leftSibling,self)
                    parent.setKey(sepleft,newKey)
                    return None
                if rightSibling != None and rightSibling.getnumTuples() > self.size // 2:
                    rightSibling.reorganize()
                    newKey = LeafNode.__merge(self,rightSibling)
                    parent.setKey(sepright,newKey)
                    return None
                if leftSibling != None:
                    newnumTuples = leftSibling.getnumTuples()+self.getnumTuples()
                    leftSibling.reorganize()
                    for i in range(0,self.getnumTuples()):
                        leftSibling[i+leftSibling.getnumTuples()] = self[i]
                    leftSibling.setnumTuples(newnumTuples)
                    if self.right != None:
                        self.right.left = leftSibling
                    leftSibling.right = self.right
                    return parent.delete(sepleft)
                newnumTuples = rightSibling.getnumTuples()+self.getnumTuples()
                rightSibling.reorganize()
                for i in range(0,rightSibling.getnumTuples()):
                    self[i+self.getnumTuples()] = rightSibling[i]
                self.setnumTuples(newnumTuples)
                if rightSibling.right != None:
                    rightSibling.right.left = self
                self.right = rightSibling.right
                return parent.delete(sepright)
            return None
        elif self.main.numGaps >= self.size // 2:
            self.reorganize()
        return None

        

        
        
        
class Non_LNode():
    def __init__(self, size, parent = None):
        self.size = size
        self.items = [None] * size
        self.numKeys = 0
        self.items[0] = parent
    def pr_print(self, number):
        print("-------------")
        print("NonLeaf Node #",number)
        print(self)
        print("number of Keys:",self.getnumKeys(),"Parent node:", self.getParent())
        print("Child 0:", self.getChild(0))
        for i in range(1,self.getnumKeys()+1):
            print("Key",i,":",self.getKey(i))
            print("Child",i,":",self.getChild(i))
    def __setitem__(self, index, val):
        if index >= 0 and index < self.size:
            self.items[index] = val
            return
        raise IndexError("NonLeafNode assignment index out of range")
    def __getitem__(self,index):
        if index >= 0 and index < self.size:
            return self.items[index]
        raise IndexError("NonLeafNode index out of range")
    def getnumKeys(self):
        return self.numKeys
    def getParent(self):
        return self[0]
    def getChild(self,index):
        idx = 2 * index + 1
        if index >= 0 and index <= self.numKeys:
            return self[idx]
        raise IndexError("There is no child with this index")
    def getKey(self,index):
        idx = 2 * index
        if index >= 1 and index <= self.getnumKeys():
            return self[idx]
        raise IndexError("There is no key with this index")
    def setnumKeys(self, nokeys):
        self.numKeys = nokeys
    def setParent(self,parent):
        self[0] = parent
    def setChild(self,index,child):
        idx = 2 * index + 1
        if idx >= 1 and idx <= self.size:
            self[idx] = child
    def setKey(self,index,key):
        idx = 2 * index
        if idx >= 2 and idx < self.size:
            self[idx] = key
    def find(self, key):
        idx = 0
        for i in range(1, self.numKeys + 1):
            if self.getKey(i) > key:
                break
            idx += 1
        return self.getChild(idx).find(key)
    def __locate(self,key,min,max):
        med = (min + max) // 2
        if key < self.getKey(med):
            if min == med:
                return min
            return self.__locate(key,min,med)
        if key > self.getKey(med):
            if max == med:
                return max + 1
            return self.__locate(key,med+1,max)
        raise IndexError("The key already exists.")
    def insertatIndex(self,idx,k,c):
        for i in range(self.getnumKeys(),idx-1,-1):
            self.setKey(i+1,self.getKey(i))
            self.setChild(i+1,self.getChild(i))
        self.setKey(idx,k)
        self.setChild(idx,c)
        self.setnumKeys(self.getnumKeys()+1)
    def insert(self, k, c):
        if 2 * (self.getnumKeys() + 1) < self.size:
            if self.getnumKeys() == 0:
                idx = 1
            else:
                min, max = 1, self.getnumKeys()
                idx = self.__locate(k,min,max)
            self.insertatIndex(idx,k,c)
            return None
        separator = self.split(k,c)
        parent = self.getParent()
        if parent != None:
            return parent.insert(separator[0],separator[1])
        newroot = Non_LNode(self.size)
        newroot.setnumKeys(1)
        newroot.setChild(0, self)
        newroot.setKey(1,separator[0])
        newroot.setChild(1,separator[1])
        self.setParent(newroot)
        separator[1].setParent(newroot)
        return newroot
    def split(self,key,c):
        halflength = (self.getnumKeys() + 1) // 2
        newnode = Non_LNode(self.size)
        newnode.setnumKeys(self.getnumKeys() - halflength)
        newnode.setParent(self.getParent())
        key_idx = 1
        for i in range(1,self.getnumKeys()+1):
            if self.getKey(i) < key:
                key_idx += 1
        if key_idx <= halflength:
            newkey = self.getKey(halflength)
            newnode.setChild(0,self.getChild(halflength))
            for i in range(halflength,key_idx,-1):   
                self.setKey(i,self.getKey(i-1))
                self.setChild(i,self.getChild(i-1))
            self.setKey(key_idx,key)
            self.setChild(key_idx,c)
            for i in range(1,newnode.getnumKeys()+1):
                j = i + halflength
                newnode.setKey(i,self.getKey(j))
                newnode.setChild(i,self.getChild(j))           
        elif key_idx == halflength + 1:
                newkey = key
                newnode.setChild(0,c)
                for i in range(1,newnode.getnumKeys()+1):
                    j = i + halflength
                    newnode.setKey(i,self.getKey(j))
                    newnode.setChild(i,self.getChild(j))
        else:
            newkey = self.getKey(halflength+1)
            newnode.setChild(0,self.getChild(halflength+1))
            for i in range(1, key_idx - halflength - 1):
                j = i + halflength + 1
                newnode.setKey(i,self.getKey(j))
                newnode.setChild(i,self.getChild(j))
            newnode.setKey(key_idx - halflength - 1,key)
            newnode.setChild(key_idx - halflength - 1,c)
            for i in range(key_idx - halflength, newnode.getnumKeys() + 1):
                j = i + halflength
                newnode.setKey(i,self.getKey(j))
                newnode.setChild(i,self.getChild(j))
            
        self.setnumKeys(halflength)
        for i in range(newnode.getnumKeys()+1):
            chld = newnode.getChild(i)
            if chld != None:
                chld.setParent(newnode)
        return(newkey,newnode)
    def leftsibling(self,node):
        if self.getChild(0) == node:
            return None
        for i in range(1,self.getnumKeys()+1):
            if self.getChild(i) == node:
                separator = i
                return (self.getChild(i-1),separator)
    def rightsibling(self,node):
        for i in range(self.getnumKeys()):
            if self.getChild(i) == node:
                separator = i+1
                return (self.getChild(i+1),separator)
        return None
    def __merge(node1,Key,node2):
        numitems = node1.getnumKeys() + node2.getnumKeys() + 1
        med = numitems // 2 + 1
        if node1.getnumKeys() < node2.getnumKeys():
            num1 = node1.getnumKeys()
            node1.setnumKeys(med-1)
            node1.setKey(num1+1,Key)
            node1.setChild(num1+1,node2.getChild(0))
            for i in range(num1+2,med):
                node1.setKey(i,node2.getKey(i-num1-1))
                node1.setChild(i,node2.getChild(i-num1-1))
                if node1.getChild(i) != None:
                    node1.getChild(i).setParent(node1)
            k = node2.getKey(med - num1 - 1)
            node2.setChild(0,node2.getChild(med - num1 - 1))
            num2 = numitems - med
            for i in range(1,num2+1):
                node2.setKey(i,node2.getKey(i+node2.getnumKeys()-num2))
                node2.setChild(i,node2.getChild(i+node2.getnumKeys()-num2))
            node2.setnumKeys(num2)
            return k
        k = node1.getKey(med)
        num2 = numitems - med
        for i in range(node2.getnumKeys(),0,-1):
            node2.setKey(i+num2-node2.getnumKeys(),node2.getKey(i))
            node2.setChild(i+num2-node2.getnumKeys(),node2.getChild(i))
        node2.setKey(num2-node2.getnumKeys(),Key)
        node2.setChild(num2-node2.getnumKeys(),node2.getChild(0))
        for i in range(1,num2-node2.getnumKeys()):
            node2.setKey(i,node1.getKey(i+med))
            node2.setChild(i,node1.getChild(i+med))
            if node2.getChild(i) != None:
                node2.getChild(i).setParent(node2)
        node2.setChild(0,node1.getChild(med))
        if node2.getChild(0) != None:
                node2.getChild(0).setParent(node2)
        node1.setnumKeys(med-1)
        node2.setnumKeys(num2)
        return k
    def delete(self,index):
        for i in range(index,self.getnumKeys()):
            self.setKey(i,self.getKey(i+1))
            self.setChild(i,self.getChild(i+1))
        self.setnumKeys(self.getnumKeys()-1)
        parent = self.getParent()
        if parent == None:
            if self.getnumKeys() == 0:
                self.getChild(0).setParent(None)
                return self.getChild(0)
            return None
        else:
            left = parent.leftsibling(self)
            right = parent.rightsibling(self)
        if left != None:
            leftSibling = left[0]
            sepleft = left[1]
        else:
            leftSibling = None
        if right != None:
            rightSibling = right[0]
            sepright = right[1]
        else:
            rightSibling = None
        order = self.size // 2
        
        if self.getnumKeys() < order // 2 - 1:
            if leftSibling != None and leftSibling.getnumKeys() > order // 2:
                separator = parent.getKey(sepleft)
                newKey = Non_LNode.__merge(leftSibling,separator,self)
                parent.setKey(sepleft,newKey)
                return None
            if rightSibling != None and rightSibling.getnumKeys() > order // 2:
                separator = parent.getKey(sepright)
                newKey = Non_LNode.__merge(self,separator,rightSibling)
                parent.setKey(sepright,newKey)
                return None
            if leftSibling != None:
                separator = parent.getKey(sepleft)
                newnumKeys = leftSibling.getnumKeys()+self.getnumKeys()+1
                oldnumKeys = leftSibling.getnumKeys()
                leftSibling.setnumKeys(newnumKeys)
                for i in range(1,self.getnumKeys()+1):
                    leftSibling.setKey(i+oldnumKeys+1,self.getKey(i))
                    leftSibling.setChild(i+oldnumKeys+1,self.getChild(i))
                    if leftSibling.getChild(i+oldnumKeys+1) != None:
                        leftSibling.getChild(i+oldnumKeys+1).setParent(leftSibling)
                leftSibling.setKey(oldnumKeys+1,separator)
                leftSibling.setChild(oldnumKeys+1,self.getChild(0))
                if leftSibling.getChild(oldnumKeys+1) != None:
                        leftSibling.getChild(oldnumKeys+1).setParent(leftSibling)
                return parent.delete(sepleft)
            separator = parent.getKey(sepright)
            newnumKeys = rightSibling.getnumKeys()+self.getnumKeys()+1
            oldnumKeys = self.getnumKeys()
            self.setnumKeys(newnumKeys)
            for i in range(1,rightSibling.getnumKeys()+1):
                self.setKey(i+oldnumKeys+1,rightSibling.getKey(i))
                self.setChild(i+oldnumKeys+1,rightSibling.getChild(i))
                if self.getChild(i+oldnumKeys+1) != None:
                    self.getChild(i+oldnumKeys+1).setParent(self)
            self.setKey(oldnumKeys+1,separator)
            self.setChild(oldnumKeys+1,rightSibling.getChild(0))
            if self.getChild(oldnumKeys+1) != None:
                self.getChild(oldnumKeys+1).setParent(self)
            return parent.delete(sepright)
        return None

class BpTree():
    def __init__(self, order = 8, keyrange = 1):
        self.blocksize = order * 2
        self.keyrange = keyrange
        self.root = LeafNode(None, self.blocksize - 1, keyrange)
    def prprint(self):
        BpTree.__ppt(self.root,"0")
    def __ppt(node,num):
        if node != None:
            node.pr_print(num)
            if type(node) == Non_LNode:
                for i in range(node.getnumKeys()+1):
                    numext = num+"."+str(i)
                    BpTree.__ppt(node.getChild(i),numext)
    def getFirst(self):
        cursor = self.root
        while cursor.size == self.blocksize:
            cursor = cursor.getChild(0)
        return cursor
    def find(self,key):
        res = BpTree.__find(self.root, key)
        if res[1] == -1:
            print("Key Not Found in Tree:", key)
            return False
        return res[1]
    def __find(node, key):
        return node.find(key)
    def __check(node,key):
        res = node.find(key)
        if res[1] != -1:
            raise ValueError("There exists already a tuple with this key.")
        return res[0]
    def insert(self, item):
        if type(self.keyrange) == int:
            key = item[:self.keyrange]
        else:
            key = []
            for i in self.keyrange:
                key.append(item[i])
        leaf = BpTree.__check(self.root, key)
        #print("\ncheck done")
        res = leaf.insert(item)
        if res != None:
            self.root = res
            
    def delete(self, key):
        res = self.root.find(key)
        if res[1] == -1:
            print("Key Not Found For Deletion:", key)
        res = res[0].delete(key)
        if res != None:
            self.root = res
    def retrieve(self, pointer):
        node = pointer[0]
        idx = pointer[1]
        return node[idx]
    def __iterSortBlock(node):
        if node != None:
            node.reorganize()
            yield node
            for e in BpTree.__iterSortBlock(node.right):
                yield e
        return
    def IterSortBlock(self):
        return BpTree.__iterSortBlock(self.getFirst())
    def __iterallkey(node):
        if node == None:
            return
        node.reorganize()
        for i in range(node.main.numtuples):
            yield node.main.getKey(i)
        for e in BpTree.__iterallkey(node.right):
            yield e
    def iterallkey(self):
        return BpTree.__iterallkey(self.getFirst())
    def __iteralldata(node):
        if node == None:
            return
        node.reorganize()
        for i in range(node.main.numtuples):
            yield node[i]
        for e in BpTree.__iterallkey(node.right):
            yield e
    def iterallData(self):
        return BpTree.__iteralldata(self.getFirst())


if __name__ == '__main__':
    print("Tests for B+-tree:\n")
    print("BpTree of order 1:\n")
    bt = BpTree(4, 1)
    print("input data1:\n")
    test1 = []
    j = 0
    for i in range(40):
        j = (j + 1) %4
        test1.append([i,j])
    print(test1)
    for e in test1:
        bt.insert(e)
    bt.prprint()
    print("#######################################################################")
    for i in range(0,40):
        bt.delete([i])
    bt.prprint()
    print("#######################################################################")

    from movies import movies as test2
    #print(test2)
    bt = BpTree(8, 2)
    for i in range(len(test2)):
        bt.insert(test2[i])
    lb = []
    for e in bt.iterallData():
        lb.append(e)
    print("new input:\n")
    print(lb)
    print("new data:\n")
    bt.prprint()
    for i in range(len(test2)//2 - 1):
        bt.delete(test2[2*i][:2])
    print("#####################################################")
    print("after deletion:\n")
          
    bt.prprint()
    print("\nfinding Chaplin:\n")
    a = bt.find(['Chaplin', 1992])
    print(a)


        





        







                