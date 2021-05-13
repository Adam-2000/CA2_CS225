# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:31:22 2020

@author: 45242
"""
from Relations import MainData    
from BTree import BTree    
class TSAM:
    def __init__(self, database = MainData()):
        self.main = database
        self.RelationSet = database.getallRel()
        self.RelNameSet = database.getRelNames()
        self.LitNameSet = []
        self.ValSet =[]
        self.ENV = []
        self.RES = []
        self.KeySet = []
        self.signs = ['(', ')', '.', '^', '|', '@', '/','#']
        self.litrelnames = ['movie', 'person','role']
        self.arithmetic_operators = ['+','-','*']
        self.comparision_operators = ['==','<','>','<=','>=','!=']
        self.aggregation_operators = ['COUNT','MAX','SUM','MIN', 'AVERAGE', 'NESTED']
        self.list_operators = ['CONTAINS', 'IN', 'IS']
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
        """check"""
        result =  self.__thinlist(self.RES.pop())[:]
        #result = self.distinct(result)
        return result
    def __eval_whole(self, query):
        #print("----------------whole:", query)
        while query != []:
            self.__eval_single(query)
    def __eval_single(self, query):
        #print("----------------single:", query)
        #if query[0] == '.':
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
            #print("WHERE STARTS","**************************single end RES\n",self.RES)
            la = self.RES[-1]
            self.ENV.append(self.nested(la))
            self.__eval_single(query)
            #we obtain a list in the form[True, False, True, False] and use it to select from (1,4,7,10) in TOP(RES)
            #print("WHERE","**************************single end RES\n",self.RES)
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

        #elif command in self.ValSet:
         #   self.RES.append([command])

        else:
            #command should be some value as a string
            self.RES.append([command])
        #if command == '.':
            #print("\n\nsingle end RES",self.RES) #You can check the RES and ENV yourself
        #print("**************************single end RES\n",self.RES)
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

    def expand(self, la, Tuple):
        lc = [None] * len(la)
        #print("expand, Tuple:", Tuple)
        if type(Tuple) == str:
            lc[0] = Tuple
            #it's a bptree
            relation = self.getRelation(Tuple)
            #print("expand, la:", la)
            if la[0] in self.LitNameSet:
                for k in range(1, len(la)):
                    if type(la[k]) != list:
                        lc[k] = relation.find([la[k]])
                    else:
                        lc[k] = [None] * len(la[k])
                        for m in range(len(la[k])):
                            lc[k][m] = relation.find([la[k][m]])
                #print("expand, bptree,!!!!!!!!!!!!!!!", lc)
                return lc
            for k in range(1, len(la)):
                if la[k] == None:
                    lc[k] = None
                    continue
                if type(la[k]) != list:
                    lc[k] = relation.find([la[k]])
                else:
                    if type(la[k][0]) != list:
                        lc[k] = lc[k] = relation.find(la[k])
                    else:
                        lc[k] = [None]* len(la[k])
                        for m in range(len(la[k])):
                            lc[k][m] = relation.find(la[k][m])
            return lc
        #it's a btree
        btree = Tuple[0]
        relname = Tuple[1]
        lc[0] = relname
        for k in range(1, len(la)):
            if type(la[k]) != list:
                lc[k] = btree.find([la[k]])
            elif type(la[k][0]) != list:
                lc[k] = btree.find(la[k])
            else:
                lc[k] = [None] * len(la[k])               
                for m in range(len(la[k])):
                    #print("find key:",la[k][m] )
                    lr = btree.find(la[k][m])
                    if lr == None:
                        lr = None
                    lc[k][m] = lr
        return lc    
    
                
    
    def where(self, l_phi, l_Q):
        la = [l_Q[0]]
        for i in range(1, len(l_phi)):
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
        elif la[0] in self.RelNameSet:
            relation = self.getRelation(la[0])
            lc = [None] * len(la)
            lc[0] = la[0]
            for k in range(1, len(la)):
                data = relation.find(la[k])
                lc[k] = data
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
        if litname in self.LitNameSet:
            relname = la[0]
            #print("proj, la:", la)
            #print("proj, la:--------------------\n",la)
            if relname in self.RelNameSet:
                relation = self.getRelation(relname)
                attributes = relation.attributes
            else:
                attributes = relname
            lc[0] = litname
            keyidx = None
            #print("proj attributes:", attributes, litname)
            for i in range(len(attributes)):
                if litname == attributes[i]:
                    keyidx = i
                    break
            #print("proj!!!!!!!!!!!!!!!!!!!!!!!!\n", keyidx, attributes)
            for k in range(1, len(la)):
                if la[k] == None:
                    lc[k] = None
                    continue
                if type(la[k][0]) != list:
                    if la[k] == None:
                        lc[k] = None
                    else:
                        lc[k] = la[k][keyidx]
                else:
                    lc[k] = [None] * len(la[k])
                    for r in range(len(la[k])):
                        if type(la[k][r][0]) != list:
                            if la[k][r] == None:
                                lc[k][r] = None
                            else:
                                #print("proj:,", k,r,keyidx)
                                lc[k][r] = la[k][r][keyidx]
                        else:
                            lc[k][r] = [None] * len(la[k][r])
                            for s in range(len(la[k][r])):
                                #print(k,r,s,keyidx)
                                #print(la[k][r][s], keyidx)
                                lc[k][r][s] = la[k][r][s][keyidx]
            #print("proj res:", la,lc)
        elif litname in self.litrelnames:
            relname = la[0]
            relation = self.getRelation(relname)
            if litname == 'movie':
                keychr = ['m','y']
            if litname == 'role':
                keychr = ['m','y','d']
                if len(la) == 1:
                    return la
                if type(la[0]) == list:
                    if type(la[1][0]) == list:
                        for k in range(1, len(la)):
                            la[k] = la[k][0]
            
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
                if la[k] == None:
                    lc[k] = None
                    continue
                if type(la[k][0]) != list:
                    ly = []
                    for idx in seckeyidx: 
                        #print(ly, la, k ,r, idx)
                        ly.append(la[k][idx])   
                    lc[k] = ly
                else:
                    lc[k] = [None] * len(la[k])
                    for r in range(len(la[k])):
                        ly = []
                        for idx in seckeyidx: 
                            #print(ly, la, k ,r, idx)
                            ly.append(la[k][r][idx])   
                        lc[k][r] = ly
        else:
            raise KeyError("litname not found in proj:", litname)
        #if litname == 'id':
            #print("proj,????????????????????????????????????????????\n", lc)
        return lc
        
    def Lname(self, name):
        la = []
        relation = self.getRelation(name)
        la.append(name)
        for item in relation.iterallkey():
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
        #print("compare:",la,lb)
        if len(lb) == 1:
            lb = [lb[0]] * len(la)
        elif len(la) == 1:
            la = [la[0]] * len(lb)
        if len(lb) != len(la):
            raise TypeError("different lenght when compare")
        lc = [None] * len(la)
        lc[0] = la[0]
        #this == compare is designed all suitable for [a] == [1,1,1,1] or [a,a,a,a] == [1]
        #in some degree flexible
        if symbol == "==":
            #if (la[0] not in self.ValSet) and (lb[0] in self.ValSet):
                #la = self.deref(la)
            #elif (la[0] in self.ValSet) and (lb[0] not in self.ValSet): 
                #lb = self.deref(lb)
            if type(la[1]) != list:
                for i in range(1, len(la)):
                    if type(la[i]) != str:
                        la[i] = str(la[i])
                    lc[i] = (la[i] == lb[i])
            else:
                for i in range(1, len(la)):
                    for j in range(len(la[i])):
                        if type(la[i][j]) != str:
                            la[i][j] = str(la[i][j])
                        if la[i][j] != lb[i]:
                            lc[i] = False
                            break
                        if j == len(la[i]) - 1:
                            lc[i] = True
                
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
        lc[0] = la[0]
        #if type(lb[0]) != bool or type(la[0]) != bool:
            #raise TypeError("not bool type")
        if symbol == 'and':
            for i in range(1, lg):
                lc[i] = la[i] and lb[i]
        elif symbol == 'or':
            for i in range(1, lg):
                lc[i] = la[i] or lb[i]
        return lc
    
    def list_operate(self, symbol, lb, la):
        if symbol == 'IS':
            lc = [None] * len(la)
            lc[0] = la[0]
            btree = lb[0][0]
            for k in range(1, len(la)):
                if btree.find(la[k]) == None:
                    lc[k] = False
                else:
                    lc[k] = True
            return lc
        if symbol == 'IN':
            value = la[0]
            seta = lb
        elif symbol == 'CONTAINS':
            value = lb[0]
            seta = la
        lc = [None] * len(seta)
        lc[0] = value
        for i in range(1, len(seta)):
            if seta[i] == None:
                lc[i] = False
                continue
            if value in seta[i]:
                lc[i] = True
            else:
                lc[i] = False
        return lc
    def Boolean_operate_1(self, symbol, la):
        lc = [None] * len(la)
        lc[0] = la[0]
        if symbol == "not":
            for i in range(1, len(la)):
                lc[i] = not la[i]
        return lc
    def ListPairs(self, seckey, RelName):
        pass



 

##############################

"""
T = TSAM()
"""
"""
query2_1 = "MOVIES WHERE (g == comedy) WHERE (movie IS (A_AWARDS / MOVIES)) WHERE ((movie # (A_AWARDS / MOVIES).an #AWARDS.c == USA) and (movie # (A_AWARDS / MOVIES).ay == 1994))"
query2_2 = "WHERE (not (movie # (A_AWARDS / MOVIES).role#ROLES.id#(ROLES/PERSONS).movie#MOVIES.g CONTAINS action)"
query2_3 = "and (not (movie # (A_AWARDS / MOVIES).role#ROLES.id#(DIRECTORS/PERSONS).movie#MOVIES.c CONTAINS Italy))"
query2_4 = "and (not (movie # (A_AWARDS / MOVIES).role#ROLES.id#(WRITERS/PERSONS).movie#MOVIES.c CONTAINS Italy)))"
query2 = query2_1 + query2_2 + query2_3 + query2_4
print("Ex2(ii) input:\n", query2)
res = T.eval(query2)
print("Ex2(ii) Result:\n",res)

#


##############################
print("\n\n")
query3 = "ROLES / PERSONS WHERE (movie # (RESTRICTIONS/MOVIES).d NeverChildren) @ PERSONS"
print("Input query for Ex2(iii) is:\n", query3)
res = T.eval(query3)
names = [e[1]+' '+ e[2] for e in res]
print("Result for Ex2(iii):")
print(names)

"""

################################
#from AssociativeArray import AssociativeArray
"""
#from Undirected_Graph import Graph
def pairs_l(la):
    if len(la) < 2:
        raise TypeError("Cannot form a pair:", la)
    pairlist = []
    for i in range(len(la) - 1):
        for j in range(i + 1, len(la)):
            pairlist.append((la[i], la[j]))
    return pairlist
def pairs_g(groups):
    allpairs = []
    for g in groups:
        pairs = pairs_l(g)
        for p in pairs:
            allpairs.append(p)
    return allpairs
"""
"""
query5 = "NESTED(APPEARANCES/SCENES).role #ROLES.id"
res = T.eval(query5)[1:]
#print(res)
groups1 = []
for g in res:
    if len(g) > 1:
        groups1.append(g)
pairs = pairs_g(groups1)
g = Graph(pairs)
res_cclist = g.cc_undirected()
reslist1 = []
for subgraph in cclist:
    vlist = [v for v in subgraph.vertexList]
    res.extend(pairs_l(vlist))
"""
"""
from Directed_Graph import DiGraph
query6 = "NESTED (ROLES/MOVIES).id"
groups2 = T.eval(query6)[1:]
#print(groups)
admirelist = []
btree_roles = BTree(T.getRelation('ROLES'), 5, 0)
btree_a_awards = BTree(T.getRelation('A_AWARDS'), 5, [0, 1, 2])
j = 0
for i in range(len(groups2)):
    if len(groups2[i]) > 1:
        admirelist.append([groups2[i]])
        admirelist[j].append([])
        for p in groups2[i]:
            roles = btree_roles.find(p)
            if roles != None:
                flag = 0
                for role in roles:
                    if flag == 0:
                        awards = btree_a_awards.find(role[1:4]) 
                        if awards != None:
                            for award in awards:
                                if award[6] == 'won':
                                    admirelist[j][1].append(p)
                                    flag = 1
                                    break
        j += 1
        
admirepairs = []

for t in admirelist:
    if len(t[1]) > 0:
        for star in t[1]:
            for p in t[0]:
                if p != star:
                    admirepairs.append((p, star))

resdg = DiGraph(admirepairs)
resdg.allDFS()
reslist2 = []
for subtree in resdg.tree:
    edges = [e for e in subtree]
    reslist2.extend(edges)
print("\nResult list of Ex4(ii):\n", reslist2, '\n')
"""
