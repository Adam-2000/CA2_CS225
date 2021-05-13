class AssociativeArray:
    def __init__(self,contents=[]):
        self.items = [None] * 20
        self.numItems = 0
        for e in contents:
            self.add(e)
            
    def add(self,item):
        if AssociativeArray.__add(item,self.items):
            self.numItems += 1
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = AssociativeArray.__rehash(self.items, [None]*2*len(self.items))
                
    def __contains__(self,item):
        index = hash(item[0]) % len(self.items)
        while self.items[index] != None:
            if self.items[index][0][0] == item[0]:
                for e in self.items[index]:
                    if e == item:
                        return True
                return False
            index = (index + 1) % len(self.items)
        return False
    
    def delete(self,item):
        if AssociativeArray.__remove(item,self.items):
            self.numItems -= 1
            load = max(self.numItems,20) / len(self.items)
            if load <= 0.25:
                self.items = AssociativeArray.__rehash(self.items, [None]*(len(self.items) // 2))
    def getvalues(self, key):
        index = hash(key) % len(self.items)
        while self.items[index] != None:
            if self.items[index][0][0] == key:
                return self.items[index]
            index = (index + 1) % len(self.items)
        return None
    def iterbuckets(self):
        buckets = []
        for bucket in self.items:
            if bucket != AssociativeArray.__Placeholder and bucket != None:
                buckets.append(bucket)
        return bucket
    def iterkeys(self):
        keys = []
        for bucket in self.items:
            if bucket != AssociativeArray.__Placeholder and bucket != None:
                keys.append(bucket[0][0])
        return keys

    # ===== Hidden Class =====
    class __Placeholder:
        def __init__(self):
            pass
        
        def __eq__(self,other):
            return False
    
    # ===== Auxiliary Functions =====
    # They all have '__' as prefixes to indicate that they are private methods to the class
    def __add(item,items):
        index = hash(item[0]) % len(items)
        location = -1
        while items[index] != None:
            if items[index][0][0] == item[0]:
                for e in items[index]:
                    if e == item:
                        return False
                items[index].append(item)
                return False
            if location < 0 and type(items[index]) == AssociativeArray.__Placeholder:
                location = index
            index = (index + 1) % len(items)
        if location < 0:
            location = index
        items[location] = [item]
        return True
        
    def __rehash(olditems,newitems):
        for e in olditems:
            if e != None and type(e) != AssociativeArray.__Placeholder:
                for el in e :
                    AssociativeArray.__add(el, newitems)
        return newitems
                
    def __remove(item,items):
        index = hash(item[0]) % len(items)
        while items[index] != None:
            if items[index][0][0] == item[0]:
                flag = 0
                for i in range(len(items[index])):
                    if items[index][i] == item:
                        nextIndex = (index + 1) % len(items)
                        flag = 1
                        break
                if not flag:
                    raise KeyError("Item not in HashSet")
                if len(items[index]) == 1:
                    if items[nextIndex] == None:
                        items[index] = None
                    else:
                        items[index] = AssociativeArray.__Placeholder()
                    return True
                else:
                    items[index].pop(i)
                    return False
            index = (index + 1) % len(items)
        raise KeyError("Item not in HashSet")
    
    def __eq__(self, other):
        for e in self.items:
            if e != None and type(e) != AssociativeArray.__Placeholder:
                for el in e:
                    if not other.__contains__(el):
                        return False
        return True
    def __repr__(self):
        return str(self.items)
    def __getallval(self, key):
        if key == None or type(key) == tuple:
            return []
        values = [v[1] for v in self.getvalues(key)]
        newvalues = []
        for val in values:
            if val not in self.keyset:
                print("value not in", val)
                self.keyset.append(val)
                childvals = self.__getallval(val)
                for c in childvals:
                    if c not in values:
                        newvalues.append(c)
        for c in newvalues:
            self.add((key, c))
        newvalues.extend(values)
        return newvalues
        
    def getalldirectedpairs(self):
        print(self)
        self.keyset = []
        first = self.iterkeys()[0]
        self.__getallval(first)
        res = []
        print("\n\n\n",self)
        print("keys", self.keyset)
        for key in self.keyset:
            edges = self.getvalues(key)
            print(edges)
            res.extend(edges)
        return res
        
                        
    

"""
Input = [(1, 2), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5), (5, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (5, 2), (4, 2)]
R = AssociativeArray(Input)
print(R)
B = R.getalldirectedpairs()
print(B)
"""