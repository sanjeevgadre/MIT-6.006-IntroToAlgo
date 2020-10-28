# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%% Libraries
import random
import numpy as np

#%% Priorotity Queues class
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
                    
    def pop(self):
        """Removes the element with the smallest key from the priority queue
        
        Returns : the key of the smallest element
        """
        ###############################
        def min_heapify(i, heapsize):
            """If violated, fixes the min_heap property"""
            # if i is a leaf, do nothing
            if i > heapsize // 2:
                return
            
            l = 2 * i + 1
            r = 2 * i + 2
            
            # Which of the three has the smallest key: i, i, r     
            smallest = i
            if l < heapsize and self.queue[l] <= self.queue[smallest]:
                smallest = l
            if r < heapsize and self.queue[r] <= self.queue[smallest]:
                smallest = r
                
            # if the min_heap property is violated, fix it
            if smallest != i:
                tmp = self.queue[i]
                self.queue[i] = self.queue[smallest]
                self.queue[smallest] = tmp
                min_heapify(smallest, heapsize)
        #################################
                
        heapsize = len(self.queue)
        if heapsize < 1:
            raise ValueError('the queue is empty')
            
        popped_key = self.queue[0]
        # set the key of the first element to that of the last element and then pop the last element
        self.queue[0] = self.queue[heapsize - 1]
        self.queue.pop()
        heapsize = heapsize - 1
        min_heapify(0, heapsize)
        
        return popped_key
            
    def min(self):
        """Returns the smallest key in the priority queue"""
        
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]
        
    def append(self, key):
        """Inserts an element in the prority queue"""
        ################################
        def parent_index(i, heapsize):
            """Identifies if element i is a left of a right child of its parent
            
            Returns: index of the parent
            """
            if i >= heapsize:
                raise ValueError("Heap overflow")
            if i % 2 == 1:
                p = (i - 1) / 2
            else:
                p = (i - 2) / 2
            
            return p
        #################################
        
        if key is None:
            raise ValueError('Cannot insert None in the queue')
        
        # append the new key and update heapsize
        self.queue.append(key)
        i = len(self.queue) - 1
        heapsize = i + 1
        
        # Is queue[i] <  queue[p]. If yes, recursively fix the min_heap property
        while i > 0:
            p = parent_index(i, heapsize)
            if self.queue[i] < self.queue[p]:
                tmp = self.queue[p]
                self.queue[p] = self.queue[i]
                self.queue[i] = tmp
                i = p
            else:
                break
        
#%%
foo = PriorityQueue()
for i in range(10, -1, -1):
    foo.append(i)
    print foo.queue

#%%
for i in range(11):
    popped_key = foo.pop()
    print popped_key
    print foo.queue