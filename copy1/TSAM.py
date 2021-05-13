# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:31:22 2020

@author: 45242
"""
from Relations import MainData    
from BTree import BTree    
class TSAM:
    def __init__(self, database = MainData()):
        """delete the line"""
        database = MainData()###
        self.main = database
        self.RelationSet = database.getallRel()
        self.RelNameSet = database.getRelNames()
        self.LitNameSet = []
        self.ValSet =[]
        self.ENV = []
        self.RES = []
        self.KeySet = []
        self.signs = ['(', ')', '.', '^', '|', '@', '/','#']
        self.litrelnames = ['movie', 'person']
        self.arithmetic_operators = ['+','-','*']
        self.comparision_operators = ['==','<','>','<=','>=','!=']
        self.aggregation_operators = ['COUNT','MAX','SUM','MIN', 'AVERAGE', 'NESTED']
        self.list_operators = ['CONTAINS', 'IN']
        self.Boolean_operators_2 = ['and','or']
        self.Boolean_operators_1 = ['not']
        
        for relation in self.RelationSet:
            for name in relation.attributes:
                if name not in self.LitNameSet:
                    self.LitNameSet.append(name)
    def getRelation(self, name):
        return self.main.getRelation(name)
                
    """
    In our implementation, all single input should only be split with signs consists of ' ', '.', '(', ')', and '^'.
    The 1st step:
        After reading a query as a string, we split it by the signs into a list, so that we can further anaylize the calculation order
    """ 
    def eval(self, query_words):
        result = None
        query_list = query_words.split(' ')
        i = 0
        while i < len(query_list):
            if len(query_list[i]) > 1:
                for j in range(len(query_list[i])):
                    if query_list[i][j] in self.signs:
                        substr = query_list[i]
                        if j == 0:
                            query_list[i] = substr[0]
                            query_list.insert(i+1, substr[1:])
                        elif j == len(query_list[i]) - 1:
                            query_list[i] = substr[:-1]
                            query_list.insert(i+1, substr[-1])
                        else:
                            query_list[i] = substr[:j]
                            query_list.insert(i+1, substr[j])
                            query_list.insert(i+2, substr[j+1:])
                        break
            i += 1
        #print(query_list)   #You can see the form of splitted query 
        self.__eval_whole(query_list)
        #print(self.RES)     #You can see the RES stack
        result =  self.__thinlist(self.RES.pop())[1:]
        #result = self.distinct(result)
        return result
    """
    In our implementation, all operators have the same priority.
    So the order of calculation is only based on the order of input and the '(', ')'.
    We use the two function __eval_whole and __eval_single to recursively read and operate the input
    we first call __eval_whole, which calls __eval_single to evaluate and pop the first command in the query and operate
    If the __eval_single read a '(', then we find the position of the corresponding ')', and use the query in '(...)' to call another __eval_whole
    so recursively, we can evalute all combinations of single queries by '(' and ')'
    e.g. query = 1 + 2 * (3 + 4 * (5 + 6))/((7 + 8) + 9 * sum([1,2,3]))
    You can delete the '#' in front of "print(query)" in both functions below to see what happens
    """
    def __eval_whole(self, query):
        #print("----------------whole:", query)
        while query != []:
            self.__eval_single(query)
    """
    In our code:
    push(a, l) is implemented by l.append(a)
    pop(l) is implemented by l.pop()
    top(l) is implemented by l[-1]
    And these are all the operations used for RES and ENV stacks
    
    """
    def __eval_single(self, query):
        #print("----------------whole:", query)
        #print("single begin RES",self.RES) #You can check the RES and ENV yourself
        #print("single begin ENV",self.ENV)
        command = query.pop(0)
        #If the __eval_single read a '(', then we find the position of the corresponding ')', and use the query in '(...)' to call another __eval_whole
        if command == '(':
            count = 1
            for i in range(len(query)):
                if query[i] == '(':
                    count += 1
                elif query[i] == ')':
                    count -= 1
                if count == 0:
                    break
            self.__eval_whole(query[:i])
            for i in range(min(i+1, len(query))):
                query.pop(0)
            
        #when operating WHERE, we need to iterate all the elements in TOP(RES) and push them to ENV, and finally pop(ENV) and pop(RES)
        #in the PDF, the process is done one by one, but we finish them in one run because our function are flexible to deal with list of different depth
        elif command == 'WHERE':
            la = self.RES[-1]
            self.ENV.append(self.nested(la))
            self.__eval_single(query)
            #we obtain a list in the form[True, False, True, False] and use it to select from (1,4,7,10) in TOP(RES)
            self.RES.append(self.where(self.RES.pop(), self.RES.pop()))
            self.ENV.pop()
            
        elif command == '^':    #Our notation of the Cartesian product
            self.__eval_single(query)
            self.RES.append(self.cart(command, self.RES.pop(), self.RES.pop()))
            
        elif command == '|':    #Our notation of equl_join
            self.__eval_single(query)  
            self.RES.append(self.equljoin(self.RES.pop(), self.RES.pop()))
        elif command == '/':
            keyrelName = query.pop(0)
            mainname = self.RES.pop()[0]
            self.RES.append(self.seperate(mainname, keyrelName))
        elif command == '@':
            RelName = query.pop(0)
            keynames = self.RES.pop()
            self.RES.append(self.deref(keynames, RelName))
        elif command == '#':
            la = self.RES.pop()
            #print(query)
            self.__eval_single(query)
            res1 = self.RES.pop()
            #print(res1)
            bt = res1[0]
            self.RES.append(self.expand(la, bt))
        elif command == '.':    #projection
            litname = query.pop(0)
            self.RES.append(self.proj(litname, self.RES.pop()))
        elif command == 'NeverChildren':
            res = self.RES.pop()
            self.RES.append(self.Non_Children(res))
        #The two are different for upper is for Q.A, and lower is for where ((A...)*(B....))
        #So the inputs are on different stacks
        elif command in self.LitNameSet: #projection after WHERE, e.g. cinema in "Performance WHERE (cinema == Flora)"
            self.RES.append(self.proj(command, self.ENV[-1]))
            
        elif command in self.RelNameSet: # The Q e.g. Performance, Theatre...
            self.RES.append(self.Lname(command))
        elif command in self.litrelnames:
            self.RES.append(self.proj(command, self.ENV[-1]))
        
        elif command in self.comparision_operators:
            self.__eval_single(query)
            self.RES.append(self.compare(command, self.RES.pop(), self.RES.pop()))
        
        elif command in self.arithmetic_operators:
            self.__eval_single(query)
            self.RES.append(self.arithmetic_operate(command, self.RES.pop(), self.RES.pop()))
            
        elif command in self.aggregation_operators:
            self.__eval_single(query)
            self.RES.append(self.aggregation_operate(command, self.RES.pop()))
        
        elif command in self.list_operators:
            self.__eval_single(query)
            self.RES.append(self.list_operate(command, self.RES.pop(), self.RES.pop()))    
                
        elif command in self.Boolean_operators_2:
            self.__eval_single(query)
            self.RES.append(self.Boolean_operate_2(command, self.RES.pop(), self.RES.pop()))
            
        elif command in self.Boolean_operators_1:
            self.__eval_single(query)
            self.RES.append(self.Boolean_operate_1(command, self.RES.pop()))
            
        elif command in self.ValSet:
            self.RES.append([command])
            
        else:
            raise TypeError("Invalid queries: ", command)
        #print("single end RES",self.RES)
        """
        The different operations are mostly either 'a operator b' or 'operator b'        
        But for coding convinience we divide them in more detailed types, though the evaluations are very similar
        """
    
    """
    The __thinlist function is to face all different situation to result different types of output list and thinen them
    e.g. [[a,b,c]] -> [a,b,c];   [[a],[b],[c]] ->[a,b,c]
    """
    def __thinlist(self, la):
        if la != [] and type(la[0]) == list:
            if len(la) == 1:
                return la[0]
            else:
                single = 0
                lb = []
                for e in la:
                    if len(e) > 1:
                        single = 1
                if single == 0:
                    for e in la:
                        if e != []:
                            lb.append(e[0])
                    return lb
        return la
    """
    the functions below were mostly designed for taken input in form like [[a,b],[c,d]] or[a,b,c] 
    So it is in some degree flexible 
    """
    def expand(self, la, Tuple):
        btree = Tuple[0]
        relname = Tuple[1]
        lc = [None] * len(la)
        lc[0] = relname
        
        for k in range(1, len(la)):
            lc[k] = [None] * len(la[k])
            for m in range(len(la[k])):
                #print("find key:",la[k][m] )
                lr = btree.find(la[k][m])
                if lr == None:
                    lr = "Not defined"
                lc[k][m] = lr
        return lc    
    
                
    
    def where(self, l_phi, l_Q):
        la = []
        for i in range(len(l_phi)):
            if l_phi[i] == True:
                la.append(l_Q[i])
        return la
    
    def nested(self, la):
        if type(la[0]) != str:
            #print(type(la[0]))
            lc = [None] * len(la)
            bt = la[0][0]
            name = la[0][1]
            lc[0] = name
            for i in range(1, len(la)):
                lc[i] = bt.find(la[i])
        return lc
    
    def distinct(self, la):
        if type(la[0]) != list:
            setc = set(la)
            la = list(setc)
            return la
        lb = []
        for e in la:
            if type(e) != list:
                e = [e]
            setc = set(e)
            e = list(setc)
            lb.append(e)
        return self.__thinlist(lb)
    
    def deref(self, la, relname):
        lb = [None] * len(la)
        lb[0] = relname
        relation = self.getRelation(relname)
        for i in range(1, len(la)):
            lb[i] = relation.find(la[i])
        return lb
    def seperate(self, MainRelname, keyrelname):
        keynames = self.getRelation(keyrelname).getkeynames()
        relation = self.getRelation(MainRelname)
        attributes = relation.attributes
        seckeyidx = []
        for k in keynames:
            for i in range(len(attributes)):
                if k == attributes[i]:
                    seckeyidx.append(i)
                    break
                if i == len(attributes) - 1:
                    raise NameError("attribute not Found in seperate:", k)
        
        bt = BTree(relation, 5, seckeyidx)
        res = []
        res.append((bt, MainRelname))
        for k in bt.iterkeys():
            res.append(k)
        #print(MainRelname, keyrelname,res)
        return res
        
    def cart(self, lb, la):
        lc = [None]*(len(la) * len(lb))
        for i in range(len(la)):
            for j in range(len(lb)):
                if type(la[i]) != list:
                    la[i] = [la[i]]
                if type(lb[j]) != list:
                    lb[j] = [lb[j]]
                lc[i*len(lb) + j] = la[i] + lb[j]
        return lc
                
    def equljoin(self, lb, la):
        lc = []
        for i in range(len(la)):
            for j in range(len(lb)):
                if type(la[i]) != list:
                    la[i] = [la[i]]
                if type(lb[j]) != list:
                    lb[j] = [lb[j]]
                equal = 0
                for m in la[i]:
                    for n in lb[j]:
                        if self.Dict[m][1] == self.Dict[n][1]:
                            if self.Dict[m][2] == self.Dict[n][2]:
                                equal = 1
                                break
                if equal == 1:
                    lc.append(la[i] + lb[j])
        return self.__thinlist(lc)
    
    #this function is designed to iterate list with objects of all depth and return all the keys in them
    def IterKeyInSet(self, la):
        for e in la:
            if type(e) == list:
                for key in self.IterKeyInSet(e):
                    yield key
            elif type(e) != tuple:
                e = self.Dict[e]
            if type(e) == tuple:
                yield e[0]
                if type(e[2]) == list:
                    for key in self.IterKeyInSet(e[2]):
                        yield key
                
    def proj(self, litname, la):
        lc = [None] * len(la)
        """
        need to modify for different layers
        """
        if litname in self.LitNameSet:
            relname = la[0]
            relation = self.getRelation(relname)
            lc[0] = litname
            attributes = relation.attributes
            keyidx = None
            for i in range(len(attributes)):
                if litname == attributes[i]:
                    keyidx = i
                    break
            for k in range(1, len(la)):
                lc[k] = [None] * len(la[k])
                for r in range(len(la[k])):
                    lc[k][r] = [None] * len(la[k][r])
                    for s in range(len(la[k][r])):
                        #print(k,r,s,keyidx)
                        #print(la[k][r][s], keyidx)
                        lc[k][r][s] = la[k][r][s][keyidx]
        elif litname in self.litrelnames:
            relname = la[0]
            relation = self.getRelation(relname)
            if litname == 'movie':
                keychr = ['m','y']
                lc[0] = keychr
                seckeyidx = []
                attributes = relation.attributes
                for k in keychr:
                    for i in range(len(attributes)):
                        if k == attributes[i]:
                            seckeyidx.append(i)
                            break
                        if i == len(attributes) - 1:
                            raise NameError("attribute not Found in seperate:", k)
                for k in range(1, len(la)):
                    lc[k] = [None] * len(la[k])
                    for r in range(len(la[k])):
                        ly = []
                        for idx in seckeyidx: 
                            #print(ly, la, k ,r, idx)
                            ly.append(la[k][r][idx])   
                        lc[k][r] = ly
        else:
            raise KeyError("litname not found in proj:", litname)
        return lc
        
    def Lname(self, name):
        la = []
        relation = self.getRelation(name)
        la.append(name)
        for item in relation.iterallData():
            la.append(item)
        return la
    def Non_Children(self, la):
        lc = [None]*len(la)
        forchildren = ['E','G','KT','EA','TE','T','U','A','S','K','I']
        for k in range(1, len(la)):
            flag = 0
            for r in range(len(la[k])):
                if not flag:
                    for d in range(len(la[k][r])):
                        if d in forchildren:
                            lc[k] = False
                            flag = 1
                            break
            if not flag:
                lc[k] = True
        return lc
                        
    def compare(self, symbol, lb, la):

        if len(lb) == 1:
            lb = [lb[0]] * len(la)
        elif len(la) == 1:
            la = [la[0]] * len(lb)
        if len(lb) != len(la):
            raise TypeError("different lenght when compare")
        lc = [None] * len(la)
        #this == compare is designed all suitable for [a] == [1,1,1,1] or [a,a,a,a] == [1]
        #in some degree flexible
        if symbol == "==":
            if (la[0] not in self.ValSet) and (lb[0] in self.ValSet):
                la = self.deref(la)
            elif (la[0] in self.ValSet) and (lb[0] not in self.ValSet): 
                lb = self.deref(lb)
            for i in range(len(la)):
                lc[i] = (la[i] == lb[i])
                
        elif symbol == "!=":
            if (la[0] not in self.ValSet) and (lb[0] in self.ValSet):
                la = self.deref(la)
            elif (la[0] in self.ValSet) and (lb[0] not in self.ValSet): 
                lb = self.deref(lb)
            for i in range(len(la)):
                lc[i]=la[i] != lb[i]
        elif symbol == "<":
            for i in range(len(la)):
                lc[i] = la[i] < lb[i]
        elif symbol == ">":
            for i in range(len(la)):
                lc[i] = la[i] > lb[i]
        elif symbol == "<=":
            for i in range(len(la)):
                lc[i] = la[i] <= lb[i]
        elif symbol == ">=":
            for i in range(len(la)):
                lc[i] = la[i] >= lb[i]

        return lc
    
    def aggregation_operate(self, symbol, la):
        if symbol == 'NESTED':
            return self.nested(la)
        if symbol == 'COUNT':
            count = 0
            for e in la:
                if e != None and e != [] and e != False:
                    count += 1
            return count
        
        elif symbol == 'MAX':
            maxm = la[0]
            for e in la:
                if e > maxm:
                    maxm = e
            return maxm
        elif symbol == 'SUM':
            total = 0
            for e in la:
                total += e
            return total
        elif symbol == 'MIN':
            minm = la[0]
            for e in la:
                if e < maxm:
                    minm = e
            return minm
        elif symbol == 'AVERAGE':
            total = 0
            for e in la:
                total += e
            ave = total/len(la)
            return ave
    
    def arithmetic_operate(self, symbol, lb, la):
        lg = len(la)
        lc = [None] * lg
        if symbol == "+":
            for i in range(lg):
                lc[i]=la[i] + lb[i]
        elif symbol == "-":
            for i in range(lg):
                lc[i]=la[i] - lb[i]
        elif symbol == "*":
            for i in range(lg):
                lc[i]=la[i] * lb[i]
        elif symbol == "/":
            for i in range(lg):
                lc[i]=la[i] / lb[i]
        return lc
    
    def Boolean_operate_2(self, symbol, lb, la):
        lg = len(la)
        lc = [None] * lg
        if type(lb[0]) != bool or type(la[0]) != bool:
            raise TypeError("not bool type")
        if symbol == 'and':
            for i in range(lg):
                lc[i] = la[i] and lb[i]
        elif symbol == 'or':
            for i in range(lg):
                lc[i] = la[i] or lb[i]
        return lc
    
    def list_operate(self, symbol, lb, la):
        if symbol == 'IN':
            value = la[0]
            seta = lb
        elif symbol == 'CONTAINS':
            value = lb[0]
            seta = la
        if value not in self.ValSet:
            return [False]
        for key in self.IterKeyInSet(seta):
            if self.Dict[key][2] == value:
                return [True]
        return [False]
    
    def Boolean_operate_1(self, symbol, la):
        lc = [None] * len(la)
        if symbol == "not":
            for i in range(len(la)):
                lc[i] = not la[i]
        return lc
    
        
T = TSAM()
query = "ROLES / PERSONS WHERE (movie # (RESTRICTIONS/MOVIES).d NeverChildren) @ PERSONS"
res = T.eval(query)
print(res)
#res = T.eval(query)
"""
b = T.deref(['id',['00000982'],['00000983'],['00000961'],['00000962']],'PERSONS')          
print(b)
"""
"""

#print(res)
md = MainData()
bt = BTree(md.MOVIES, 5, [1])
la = [bt, [1997], [1998]]
res = T.nested(la)
print(res)

res = T.proj('movie', test3)
print(res)
"""


