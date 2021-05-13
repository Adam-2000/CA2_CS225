# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:12:52 2020

@author: 45242
"""


class BTreeNode:
    def __init__(self,order,db = None):
        self.size = 3 * order
        self.items = [None] * self.size
        self.db = db
        self[0] = 0
    def pr_print(self,db,number = 'undefined'):
        print("-------------")
        print("Btree node #",number)
        print(self)
        print("number of Keys:",self.getnumKeys(),"Parent node:", self.getParent())
        print("Child 0:", self.getChild(0))
        for i in range(1,self.getnumKeys()+1):
            print("Key",i,":",self.getKey(i))
            print("Tuple",i,":")
            lp = []
            for p in self.getData(i):
                lp.append(db.retrieve(p))
            print(lp)
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
            if type(data) == list:
                self[idx] = data
            else:
                self[idx] = [data]
    def addData(self,index,data):
        idx = 3 * index + 1
        if idx >= 4 and idx <= self.size:
            if self[idx] == None:
                self[idx] = []
            self[idx].append(data)
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
        return [med]
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
        if self.getnumKeys() == 0:
            idx = 1
        else:
            min, max = 1, self.getnumKeys()
            idx = self.__locate(k,min,max)
            if type(idx) == list:
                idx = idx[0]
                self.addData(idx, p)
                return None
                
        if 3 * (self.getnumKeys() + 1) < self.size:
            self.insertatIndex(idx,k,p,c)
            return None
        separator = self.split(k,p,c)
        parent = self.getParent()
        if parent != None:
            return parent.insert(separator[0],separator[1],separator[2])
        order = self.size // 3
        newroot = BTreeNode(order, self.db)
        newroot.setnumKeys(1)
        newroot.setChild(0,self)
        newroot.setKey(1,separator[0])
        newroot.setData(1,separator[1])
        newroot.setChild(1,separator[2])
        self.setParent(newroot)
        separator[2].setParent(newroot)
        return newroot
    def split(self,key,p,c):
        #min, max = 1, self.getnumKeys()
        #idx = self.__locate(key,min,max)
        halflength = (self.getnumKeys() + 1) // 2
        order = self.size // 3
        newnode = BTreeNode(order, self.db)
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
            for i in range(halflength,key_idx,-1):   
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
        elif key_idx == halflength + 1:
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
            for i in range(1, key_idx - halflength - 1):
                j = i + halflength + 1
                newnode.setKey(i,self.getKey(j))
                newnode.setData(i,self.getData(j))
                newnode.setChild(i,self.getChild(j))
            newnode.setKey(key_idx - halflength - 1,key)
            newnode.setData(key_idx - halflength - 1,p)
            newnode.setChild(key_idx - halflength - 1,c)
            for i in range(key_idx - halflength, newnode.getnumKeys() + 1):
                j = i + halflength
                newnode.setKey(i,self.getKey(j))
                newnode.setData(i,self.getData(j))
                newnode.setChild(i,self.getChild(j))
            
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
                """big problem here"""
                return parent.delete(sepleft)
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
            return parent.delete(sepright)
        return None
            
class BTree:
    def __init__(self, db, order, seckeyidx):
        self.main = db
        self.root = BTreeNode(order, db)
        self.seckeyidx = seckeyidx
        self.insert2tree(db)
    def prprint(self):
        BTree.__ppt(self.root,self.main,"0")
    def __ppt(node,db,num):
        if node != None:
            node.pr_print(db,num)
            for i in range(node.getnumKeys()+1):
                numext = num+"."+str(i)
                BTree.__ppt(node.getChild(i),db,numext)
    def __iterkeys(node):

        if node != None:
            for e in BTree.__iterkeys(node.getChild(0)):
                    yield e
            for i in range(1, node.getnumKeys() + 1):
                yield node.getKey(i)
                for e in BTree.__iterkeys(node.getChild(i)):
                    yield e

    def iterkeys(self):
        return BTree.__iterkeys(self.root)
    def find(self,key):
        return BTree.__find(self.root,self.main,key)
    def __find(node,db,key):
        location = node.find(key)
        idx = location[0]
        if idx != 0:
            pointers = node.getData(idx)
            lr = []
            for p in pointers:
                record = db.retrieve(p)
                lr.append(record)
            return lr
        child = location[1]
        if child != None:
            return BTree.__find(child,db,key)
        print("There is no tuple with this key.", key)
        return None
    def insert2tree(self, content):
        #j = 0
        #m = 0
        for block in content.IterSortBlock():
            #block.pr_print(str(j))
            #j += 1
            for i in range(block.getnumTuples()):
                if type(self.seckeyidx) == int:
                    key = block[i][self.seckeyidx]
                else:
                    key = []
                    for k in self.seckeyidx:
                        key.append(block[i][k])
                pointer = (block, i)
                loc = BTree.__check(self.root, key)
                #print("key, loc: ", key, loc)
                if loc[1] != 0:
                    loc[0].addData(loc[1], pointer)
                else:
                    res = loc[0].insert(key, pointer, None)
                    if res != None:
                        self.root = res
                """
                print(m,"----------------------------------------------------------------------------")
                m += 1
                self.prprint()
                """
    def __check(node,key):
        location = node.find(key)
        idx = location[0]
        if idx != 0:
            return(node, idx)
        else:
            child = location[1]
            if child != None:
                return BTree.__check(child,key)
            return (node, 0)
    """
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
            db.delete(pointer)
            return (node,idx)
        child = location[1]
        if child != None:
            return BTree.__finddelete(child,db,key)
        raise IndexError("There is no tuple with this key.")
    def __swapMax(node,ancestor,index):
        lastidx = node.getnumKeys()
        lastChild = node.getChild(lastidx)
        if lastChild != None:
            return BTree.__swapMax(lastChild,ancestor,index)
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
    """
#from Relations import MainData 
#md = MainData(8)
#btree = BTree(md.MOVIES, 5, [1])
#btree.prprint()
"""
#md.MOVIES.prprint()  
print("########################################")

la = []
for e in btree.iterkeys():
    la.append(e)
print(la)
      
print(btree.find([1997]))
"""



        






