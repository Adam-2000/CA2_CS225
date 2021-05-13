# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:53:29 2020

@author: 45242
"""

class MainData:
    class Block:
        def __init__(self,size):
            self.size = size
            self.tuples = [None] * size
            self.numtuples = 0
        def __getitem__(self,idx):
            return self.tuples[idx]
        def __setitem__(self,idx,t):
            self.tuples[idx] = t
        def getnumtuples(self):
            return self.numtuples
        def insert(self,t):
            for i in range(self.size):
                if self.tuples[i] == None:
                    self.tuples[i] = t
                    self.numtuples += 1
                    return i
            raise IndexError("The block is full.")
        def retrieve(self,idx):
            return self.tuples[idx]
    def __init__(self,blocksize):
        self.size = 100
        self.blocksize = blocksize
        self.blocks = [None] * 100
        for i in range(100):
            newblock = MainData.Block(blocksize)
            self.blocks[i] = newblock
    def getblocksize(self):
        return self.blocksize
    def __getitem__(self,idx):
        return self.blocks[idx]
    def __setitem__(self,idx,b):
        self.blocks[idx] = b
    def insert(self,record):
        for i in range(100):
            if self.blocks[i].getnumtuples() < self.blocksize:
                idx = self.blocks[i].insert(record)
                blocknumber = i
                return (blocknumber,idx)
    def retrieve(self,pointer):
        blocknumber = pointer[0]
        idx = pointer[1]
        return self.blocks[blocknumber][idx]
    def delete(self,pointer):
        blocknumber = pointer[0]
        idx = pointer[1]
        self.blocks[blocknumber][idx] = None
                
class BTreeNode:
    def __init__(self,order):
        self.size = 3 * order
        self.items = [None] * self.size
        self[0] = 0
    def pr_print(self,db,number):
        print("-------------")
        print("Btree node #",number)
        print(self)
        print("number of Keys:",self.getnumKeys(),"Parent node:", self.getParent())
        print("Child 0:", self.getChild(0))
        for i in range(1,self.getnumKeys()+1):
            print("Key",i,":",self.getKey(i))
            print("Tuple",i,":",db.retrieve(self.getData(i)))
            print("Child",i,":",self.getChild(i))
    def __setitem__(self,index,val):
        if index >= 0 and index < self.size:
            self.items[index] = val
            return
        raise IndexError("BTree node assignment index out of range")
    def __getitem__(self,index):
        if index >= 0 and index < self.size:
            return self.items[index]
        raise IndexError("Btree node index out of range")
    def getnumKeys(self):
        return self[0]
    def getParent(self):
        return self[1]
    def getChild(self,index):
        idx = 3 * index + 2
        if index >= 0 and index <= self[0]:
            return self[idx]
        raise IndexError("There is no child with this index")
    def getKey(self,index):
        idx = 3 * index
        if index >= 1 and index <= self.getnumKeys():
            return self[idx]
        raise IndexError("There is no key with this index")
    def getData(self,index):
        idx = 3 * index + 1
        if index >= 1 and index <= self[0]:
            return self[idx]
        raise IndexError("There is no key with this index")
    def setnumKeys(self,nokeys):
        self[0] = nokeys
    def setParent(self,parent):
        self[1] = parent
    def setChild(self,index,child):
        idx = 3 * index + 2
        if idx >= 2 and idx <= self.size:
            self[idx] = child
    def setKey(self,index,key):
        idx = 3 * index
        if idx >= 3 and idx <= self.size:
            self[idx] = key
    def setData(self,index,data):
        idx = 3 * index + 1
        if idx >= 4 and idx <= self.size:
            self[idx] = data
    def find(self,key):
        if self.getnumKeys() != 0:
            minidx, maxidx = 1, self.getnumKeys()
            return self.__find(key,minidx,maxidx)
        return (0,None)
    def __find(self,key,min,max):
        if min == max:
            if self.getKey(min) == key:
                return (min,None)
            if key < self.getKey(min):
                return (0,self.getChild(min-1))
            return (0,self.getChild(min))
        else:
            new = (min + max) // 2
            if self.getKey(new) == key:
                return (new,None)
            if key < self.getKey(new):
                return self.__find(key,min,new)
            else:
                return self.__find(key,new+1,max)
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
    def insertatIndex(self,idx,k,p,c):
        for i in range(self.getnumKeys(),idx-1,-1):
            self.setKey(i+1,self.getKey(i))
            self.setData(i+1,self.getData(i))
            self.setChild(i+1,self.getChild(i))
        self.setKey(idx,k)
        self.setData(idx,p)
        self.setChild(idx,c)
        self.setnumKeys(self.getnumKeys()+1)
    def insert(self,k,p,c):
        if 3 * (self.getnumKeys() + 1) < self.size:
            if self.getnumKeys() == 0:
                idx = 1
            else:
                min, max = 1, self.getnumKeys()
                idx = self.__locate(k,min,max)
            self.insertatIndex(idx,k,p,c)
            return None
        separator = self.split(k,p,c)
        parent = self.getParent()
        if parent != None:
            return parent.insert(separator[0],separator[1],separator[2])
        order = self.size // 3
        newroot = BTreeNode(order)
        newroot.setnumKeys(1)
        newroot.setChild(0,self)
        newroot.setKey(1,separator[0])
        newroot.setData(1,separator[1])
        newroot.setChild(1,separator[2])
        self.setParent(newroot)
        separator[2].setParent(newroot)
        return newroot
    def split(self,key,p,c):
        min, max = 1, self.getnumKeys()
        idx = self.__locate(key,min,max)
        halflength = (self.getnumKeys() + 1) // 2
        order = self.size // 3
        newnode = BTreeNode(order)
        newnode.setnumKeys(self.getnumKeys() - halflength)
        newnode.setParent(self.getParent())
        key_idx = 1
        for i in range(1,self.getnumKeys()+1):
            if self.getKey(i) < key:
                key_idx += 1
        if key_idx <= halflength:
            newkey = self.getKey(halflength)
            newdata = self.getData(halflength)
            newnode.setChild(0,self.getChild(halflength))
            for i in range(halflength,key_idx+1,-1):
                self.setKey(i,self.getKey(i-1))
                self.setData(i,self.getData(i-1))
                self.setChild(i,self.getChild(i-1))
            self.setKey(key_idx,key)
            self.setData(key_idx,p)
            self.setChild(key_idx,c)
            for i in range(1,newnode.getnumKeys()+1):
                j = i + halflength
                newnode.setKey(i,self.getKey(j))
                newnode.setData(i,self.getData(j))
                newnode.setChild(i,self.getChild(j))           
        else:
            if key_idx == halflength + 1:
                newkey = key
                newdata = p
                newnode.setChild(0,c)
                for i in range(1,newnode.getnumKeys()+1):
                    j = i + halflength
                    newnode.setKey(i,self.getKey(j))
                    newnode.setData(i,self.getData(j))
                    newnode.setChild(i,self.getChild(j))
            else:
                newkey = self.getKey(halflength+1)
                newdata = self.getData(halflength+1)
                newnode.setChild(0,self.getChild(halflength+1))
                for i in range(1,newnode.getnumKeys()):
                    j = i + halflength + 1
                    key_idx = 1
                    if self.getKey(j) < key:
                        newnode.setKey(i,self.getKey(j))
                        newnode.setData(i,self.getData(j))
                        newnode.setChild(i,self.getChild(j))
                        key_idx += 1
                    else:
                        newnode.setKey(i,self.getKey(j-1))
                        newnode.setData(i,self.getData(j-1))
                        newnode.setChild(i,self.getChild(j-1))
                if key_idx != newnode.getnumKeys():
                    newnode.setKey(newnode.getnumKeys(),self.getKey(j))
                    newnode.setData(newnode.getnumKeys(),self.getData(j))
                    newnode.setChild(newnode.getnumKeys(),self.getChild(j))
                newnode.setKey(key_idx,key)
                newnode.setData(key_idx,p)
                newnode.setChild(key_idx,c)
        self.setnumKeys(halflength)
        for i in range(newnode.getnumKeys()+1):
            chld = newnode.getChild(i)
            if chld != None:
                chld.setParent(newnode)
        return(newkey,newdata,newnode)
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
            node1.setKey(num1+1,Key[0])
            node1.setData(num1+1,Key[1])
            node1.setChild(num1+1,node2.getChild(0))
            for i in range(num1+2,med):
                node1.setKey(i,node2.getKey(i-num1-1))
                node1.setData(i,node2.getData(i-num1-1))
                node1.setChild(i,node2.getChild(i-num1-1))
                if node1.getChild(i) != None:
                    node1.getChild(i).setParent(node1)
            k = node2.getKey(node2.getnumKeys()-med+1)
            p = node2.getData(node2.getnumKeys()-med+1)
            node2.setChild(0,node2.getChild(node2.getnumKeys()-med+1))
            num2 = numitems - med
            for i in range(1,num2+1):
                node2.setKey(i,node2.getKey(i+node2.getnumKeys()-med+1))
                node2.setData(i,node2.getData(i+node2.getnumKeys()-med+1))
                node2.setChild(i,node2.getChild(i+node2.getnumKeys()-med+1))
            node2.setnumKeys(num2)
            return (k,p)
        k = node1.getKey(med)
        p = node1.getData(med)
        num2 = numitems - med
        for i in range(node2.getnumKeys(),0,-1):
            node2.setKey(i+num2-node2.getnumKeys(),node2.getKey(i))
            node2.setData(i+num2-node2.getnumKeys(),node2.getData(i))
            node2.setChild(i+num2-node2.getnumKeys(),node2.getChild(i))
        node2.setKey(num2-node2.getnumKeys(),Key[0])
        node2.setData(num2-node2.getnumKeys(),Key[1])
        node2.setChild(num2-node2.getnumKeys(),node2.getChild(0))
        for i in range(1,num2-node2.getnumKeys()):
            node2.setKey(i,node1.getKey(i+med))
            node2.setData(i,node1.getData(i+med))
            node2.setChild(i,node1.getChild(i+med))
            if node2.getChild(i) != None:
                node2.getChild(i).setParent(node2)
        node2.setChild(0,node1.getChild(med))
        if node2.getChild(0) != None:
            node2.getChild(0).setParent(node2)
        node1.setnumKeys(med-1)
        node2.setnumKeys(num2)
        return (k,p)
    def delete(self,index):
        for i in range(index,self.getnumKeys()):
            self.setKey(i,self.getKey(i+1))
            self.setData(i,self.getData(i+1))
            self.setChild(i,self.getChild(i+1))
        self.setnumKeys(self.getnumKeys()-1)
        parent = self.getParent()
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
        order = self.size // 3
        if self.getnumKeys() < order // 2:
            if leftSibling != None and leftSibling.getnumKeys() > order // 2:
                separator = (parent.getKey(sepleft),parent.getData(sepleft))
                newKey = BTreeNode.__merge(leftSibling,separator,self)
                parent.setKey(sepleft,newKey[0])
                parent.setData(sepleft,newKey[1])
                return None
            if rightSibling != None and rightSibling.getnumKeys() > order // 2:
                separator = (parent.getKey(sepright),parent.getData(sepright))
                newKey = BTreeNode.__merge(self,separator,rightSibling)
                parent.setKey(sepright,newKey[0])
                parent.setData(sepright,newKey[1])
                return None
            if leftSibling != None:
                separator = (parent.getKey(sepleft),parent.getData(sepleft))
                newnumKeys = leftSibling.getnumKeys()+self.getnumKeys()+1
                oldnumKeys = leftSibling.getnumKeys()
                leftSibling.setnumKeys(newnumKeys)
                for i in range(1,self.getnumKeys()+1):
                    leftSibling.setKey(i+oldnumKeys+1,self.getKey(i))
                    leftSibling.setData(i+oldnumKeys+1,self.getData(i))
                    leftSibling.setChild(i+oldnumKeys+1,self.getChild(i))
                    if leftSibling.getChild(i+oldnumKeys+1) != None:
                        leftSibling.getChild(i+oldnumKeys+1).setParent(leftSibling)
                leftSibling.setKey(oldnumKeys+1,separator[0])
                leftSibling.setData(oldnumKeys+1,separator[1])
                leftSibling.setChild(oldnumKeys+1,self.getChild(0))
                if leftSibling.getChild(oldnumKeys+1) != None:
                        leftSibling.getChild(oldnumKeys+1).setParent(leftSibling)
                if parent.getnumKeys() > 1:
                    return parent.delete(sepleft)
                leftSibling.setParent(None)
                return leftSibling
            separator = (parent.getKey(sepright),parent.getData(sepright))
            newnumKeys = rightSibling.getnumKeys()+self.getnumKeys()+1
            oldnumKeys = self.getnumKeys()
            self.setnumKeys(newnumKeys)
            for i in range(1,rightSibling.getnumKeys()+1):
                self.setKey(i+oldnumKeys+1,rightSibling.getKey(i))
                self.setData(i+oldnumKeys+1,rightSibling.getData(i))
                self.setChild(i+oldnumKeys+1,rightSibling.getChild(i))
                if self.getChild(i+oldnumKeys+1) != None:
                    self.getChild(i+oldnumKeys+1).setParent(self)
            self.setKey(oldnumKeys+1,separator[0])
            self.setData(oldnumKeys+1,separator[1])
            self.setChild(oldnumKeys+1,rightSibling.getChild(0))
            if self.getChild(oldnumKeys+1) != None:
                self.getChild(oldnumKeys+1).setParent(self)
            if parent.getnumKeys() > 1:
                return parent.delete(sepright)
            self.setParent(None)
            return self
        return None
            
class BTree:
    def __init__(self,db,order):
        self.main = db
        self.root = BTreeNode(order)
    def prprint(self):
        BTree.__ppt(self.root,self.main,"0")
    def __ppt(node,db,num):
        if node != None:
            node.pr_print(db,num)
            for i in range(node.getnumKeys()+1):
                numext = num+"."+str(i)
                BTree.__ppt(node.getChild(i),db,numext)
    def find(self,key):
        return BTree.__find(self.root,self.main,key)
    def __find(node,db,key):
        location = node.find(key)
        idx = location[0]
        if idx != 0:
            pointer = node.getData(idx)
            record = db.retrieve(pointer)
            return record
        child = location[1]
        if child != None:
            return BTree.__find(child,db,key)
        raise IndexError("There is no tuple with this key.")
    def __check(node,key):
        location = node.find(key)
        idx = location[0]
        if idx != 0:
            raise ValueError("There exists already a tuple with this key.")
        else:
            child = location[1]
            if child != None:
                return BTree.__check(child,key)
            return node
    def insert(self,key,t):
        leaf = BTree.__check(self.root,key)
        pointer = self.main.insert(t)
        res = leaf.insert(key,pointer,None)
        if res != None:
            self.root = res
    def __finddelete(node,db,key):
        location = node.find(key)
        idx = location[0]
        if idx != 0:
            pointer = node.getData(idx)
            record = db.delete(pointer)
            return (node,idx)
        child = location[1]
        if child != None:
            return BTree.__finddelete(child,db,key)
        raise IndexError("There is no tuple with this key.")
    def __swapMax(node,ancestor,index):
        lastidx = node.getnumKeys()
        lastChild = node.getChild(lastidx)
        if lastChild != None:
            return BTree.swapMax(lastChild,ancestor,index)
        kmax = node.getKey(lastidx)
        pmax = node.getData(lastidx)
        ancestor.setKey(index,kmax)
        ancestor.setData(index,pmax)
        return (node,lastidx)
    def delete(self,key):
        location = BTree.__finddelete(self.root,self.main,key)
        if location[0].getChild(location[1]) != None:
            leftchild = location[0].getChild(location[1]-1)
            location = BTree.__swapMax(leftchild,location[0],location[1])
        res = location[0].delete(location[1])
        if res != None:
            self.root = res
        
DB = MainData(10)
btree = BTree(DB,5)
btree.insert(8,(8,"Harry"))
btree.insert(14,(14,"George"))    
btree.insert(2,(2,"Sandra"))
btree.insert(15,(15,"Qing"))
btree.insert(3,(3,"Ying"))
btree.insert(1,(1,"Liz"))
btree.insert(16,(16,"Sarah"))
btree.insert(6,(6,"Fred"))
btree.insert(5,(5,"Qing"))
btree.insert(27,(27,"Bernie"))
btree.insert(37,(37,"Yuan"))
btree.insert(18,(18,"Juan"))
btree.insert(25,(25,"Iris"))
btree.insert(7,(7,"Chen"))
btree.insert(13,(13,"Chen"))
btree.insert(20,(20,"Lisa"))
btree.insert(22,(22,"Victor"))
btree.insert(23,(23,"Ralf"))
btree.insert(24,(24,"Eva"))
btree.insert(21,(21,"Emma"))
btree.prprint()

btree.delete(6)
btree.delete(7)
btree.delete(23)
btree.delete(8)
btree.delete(16)
btree.prprint()
        

