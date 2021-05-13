# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:58:56 2020

@author: 45242
"""

# Definition of FIFO class
class Fifo:
    def __init__(self,size=20):
        self.items = [None] * size
        self.first = 0
        self.last = -1
        self.size = size
        self.length = 0
    def computelength(self):
        if self.last >= self.first:
            self.length = self.last - self.first + 1
        else:
            self.length = self.last - self.first + 1 + self.size
    def isEmpty(self):
        if self.length != 0:
            return False
        return True
    def front(self):
        if self.length != 0:
            return self.items[self.last]
        raise Error("Queue is empty")
    def back(self):
        if self.length != 0:
            return self.items[self.first]
        raise Error("Queue is empty")
    def pushback(self,item):
        if self.length == self.size:
            self.allocate()
        self.last = (self.last + 1) % self.size
        self.items[self.last] = item
        self.computelength()
    def popfront(self):
        if self.length == self.size / 4:
            self.deallocate()
        if self.last - self.first + 1 != 0:
            frontelement = self.items[self.first]
            self.first = (self.first + 1) % self.size
            if self.last - self.first + 1 == 0:
                self.length = 0
            else:
                self.computelength()
            return frontelement
        raise Error("Queue is empty")
    def __iter__(self):
        rlast = self.first + self.length
        for i in range(self.first,rlast):
            yield self.items[i % self.size]
    def allocate(self):
        newlength = 2 * self.size
        newQueue = [None] * newlength
        for i in range(self.size):
            pos = (i + self.first) % self.size
            newQueue[i] = self.items[pos]
        self.items = newQueue
        self.first = 0
        self.last = self.size - 1
        self.size = newlength
        self.computelength()
    def deallocate(self):
        newlength = round(self.size / 2)
        newQueue = [None] * newlength
        length = (self.last - self.first +1) % self.size
        for i in range(length):
            pos = (i + self.first) % self.size
            newQueue[i] = self.items[pos]
        self.items = newQueue
        self.first = 0
        self.last = length - 1
        self.size = newlength
        self.computelength()

# Definition of Stack class
class Stack:
    def __init__(self,size=20):
        self.items = [None] * size
        self.numItems = 0
        self.size = size
        
    def top(self):
        if self.numItems != 0:
            return self.items[self.numItems-1]
        raise Error("Stack is empty")
        
    def push(self,item):
        if self.numItems == self.size:
            self.allocate()
        self.items[self.numItems] = item
        self.numItems += 1
        
    def allocate(self):
        newlength = 2 * self.size
        newStack = [None] * newlength
        for i in range(self.numItems):
            newStack[i] = self.items[i]
        self.items = newStack
        self.size = newlength
        
    def pop(self):
        if self.numItems == self.size / 4:
            self.deallocate()
        if self.numItems != 0:
            topelement = self.items[self.numItems-1]
            self.numItems -= 1
            return topelement
        raise Error("Stack is empty")
        
    def deallocate(self):
        newlength = self.size // 2
        newStack = [None] * newlength
        for i in range(self.numItems):
            newStack[i] = self.items[i]
        self.items = newStack
        self.size = newlength
        
    def isEmpty(self):
        if self.numItems != 0:
            return False
        return True
    
class Error(Exception):
    def __init__(self, content = None):
        self.content = content
    def __str__(self):
        return self.content

        