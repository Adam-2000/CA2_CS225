# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:18:06 2020

@author: 45242
"""
import BpTree
class Relation(BpTree.BpTree):
    def __init__(self, order = 8, keyrange = 1, content = [], attributes = None):
        self.blocksize = order * 2
        self.keyrange = keyrange
        self.attributes = attributes 
        self.root = BpTree.LeafNode(None, self.blocksize - 1, keyrange)
        self.insCtnt(content)
    def insCtnt(self, content):
        for e in content:
            self.insert(e)
    def getkeynames(self):
        if type(self.keyrange) == int:
            return self.attributes[:self.keyrange]
        res = []
        for idx in self.keyrange:
            res.append(self.attributes[idx])
        return res
from movies import movies
from roles import roles
from restrictions import restrictions
from persons import persons
from ActorAwards import ActorAwards
from awards import awards
from directors import directors
from writers import writers
from appearances import appearances
from scenes import scenes
class MainData():
    def __init__(self, order = 8):
        self.numRel = 10
        self.MOVIES = Relation(order, 2, movies, ['m', 'y', 'c', 't', 'g'])
        self.ROLES = Relation(order, [1,2,3], roles, ['id', 'm', 'y', 'd', 'cr'])
        self.RESTRICTIONS = Relation(order, 4, restrictions, ['m', 'y', 'd', 'c'])
        self.PERSONS = Relation(order, 1, persons, ['id', 'f', 'n', 'y'])
        self.A_AWARDS = Relation(order, 4, ActorAwards, ['m', 'y', 'd', 'an', 'ay', 'cg', 'r'])
        self.AWARDS = Relation(order, 1, awards, ['an', 'i', 'c'])
        self.WRITERS = Relation(order, 3, writers, ['id', 'm', 'y', 'cr'])
        self.DIRECTORS = Relation(order, 3, directors, ['id', 'm', 'y'])
        self.APPEARANCES = Relation(order, 4, appearances, ['m', 'y', 'd', 'sn'])
        self.SCENES = Relation(order, 3, scenes, ['m','y','sn','sd'])
        self.content = ['MOVIES', 'ROLES', 'RESTRICTIONS', 'PERSONS', 'A_AWARDS', 'AWARDS', 'WRITERS', 'DIRECTORS', 'APPEARANCES', 'SCENES']
        self.relations = [self.MOVIES, self.ROLES, self.RESTRICTIONS, self.PERSONS, self.A_AWARDS, self.AWARDS, self.WRITERS, self.DIRECTORS, self.APPEARANCES, self.SCENES]
    def IterRelations(self):
        for e in self.relations:
            yield e
    def getRelNames(self):
        return self.content
    def getRelation(self, name):
        for i in range(self.numRel):
            if self.content[i] == name:
                return self.relations[i]
        raise NameError("Relation not Found in Maindata:", name)
    def getallRel(self):
        return self.relations
"""     
md = MainData()
b = md.MOVIES.getkeynames()
print(b)
"""