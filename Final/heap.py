# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:24:10 2020

@author: 45242
"""

class heap():
    def __init__(self, content = []):
        self.heap = []
        for i in range(len(content)):
            self.heap.append(content[i])
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.siftdown(i)
            
    def mminitem(self):
        return self.heap[0]
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def getLenght(self):
        return len(self.heap)
    
    def remove_min(self):
        if len(self.heap) == 0:
            raise IndexError("heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        max_elmt = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.siftdown(0)
        return max_elmt
    
    def remove(self, i):
        if i >= len(self.heap):
            raise IndexError("index out of range")
        if i == len(self.heap) - 1:
            return self.heap.pop()
        elmt = self.heap[i]
        self.heap[i] = self.heap.pop()
        self.siftdown(i)
        return elmt
    
    def insert(self, k):
        self.heap.append(k)
        self.siftup(len(self.heap) - 1)
        
    def siftdown(self, i):
        if (2 * i + 1) >= len(self.heap):
            return
        min_idx = i
        min_elmt = self.heap[i]
        left_elmt = self.heap[2 * i + 1]
        if min_elmt > left_elmt:
            min_idx = 2 * i + 1
            min_elmt = left_elmt
        if (2 * i + 2) < len(self.heap):
            right_elmt = self.heap[2 * i + 2]
            if min_elmt > right_elmt:
                min_idx = 2 * i + 2
                min_elmt = right_elmt
        if min_idx == i:
            return
        temp = self.heap[i]
        self.heap[i] = self.heap[min_idx]
        self.heap[min_idx] = temp
        self.siftdown(min_idx)
        
    def siftup(self, i):
        if i <= 0:
            return
        par_idx = (i - 1) // 2
        par_elmt = self.heap[par_idx]
        elmt = self.heap[i]
        if par_elmt <= elmt:
            return
        self.heap[par_idx] = elmt
        self.heap[i] = par_elmt
        self.siftup(par_idx)
        
def heapsort(la):
    h = heap(la)
    lb = []
    while not h.is_empty():
        lb.append(h.remove_min())
    return lb

