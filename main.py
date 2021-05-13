# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:06:08 2020

@author: 45242
"""

from TSAM import TSAM
T = TSAM()

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

#############################
from Undirected_Graph import Graph
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
for subgraph in res_cclist:
    vlist = [v for v in subgraph.vertexList]
    reslist1.extend(pairs_l(vlist))
print("\nresult list for Ex4(i):\n(The result graph is in the code)\n", reslist1)
####################################
from Directed_Graph import DiGraph
from BTree import BTree
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

