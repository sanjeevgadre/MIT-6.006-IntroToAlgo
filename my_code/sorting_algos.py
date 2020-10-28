#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:03:14 2020

@author: sanjeev

Sorting Algorithms

"""
#%% Libraries
import random
import profile

#%% Create a random array
def create_array(n=10):
    u_bound = n * 2    
    a = [random.randint(0, u_bound) for i in range(n)]
    
    return a

#%% Implementing Insertion Sort
def insertion_sort(lst):
    # A list with just one element is already sorted
    if len(lst) <= 1:
        return lst
    
    # get the next number to sort. the first number is always sorted
    for i in range(1, len(lst)):
        key = lst[i]
        # compare the number with the number to its immediate left. If the number is 
        # smaller than its immediate neighbour then it is already sorted, else
        # compare number with all numbers in the list to the left of the number to find its
        # sorted position
        if key <= lst[i-1]:
            pass
        else:
            for j in range(i-1, -1, -1):
                # if the number to sort is larger
                if key > lst[j]:
                    # shift the neighbour  to the right
                    lst[j+1] = lst[j]
                    #insert the number to sort in its place
                    lst[j] = key
    
    return lst

#%% Implementing Merge Sort
def merge_sort(lst):
    
    ##########################################
    def merge(left, right):
        merged_lst = []
        i = 0
        j = 0
        len_left = len(left)
        len_right = len(right)
        while i < len_left and j < len_right:
            if left[i] >= right[j]:
                merged_lst.append(left[i])
                i = i + 1
            else:
                merged_lst.append(right[j])
                j = j + 1
        
        if i < len_left:
            merged_lst = merged_lst + left[i:]
        elif j < len_right:
            merged_lst = merged_lst + right[j:]
            
        return merged_lst
    ###########################################
    
    # A list with one element is already sorted
    if len(lst) <= 1:
        return lst
    
    # Split the list into two halves
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
      
    # Sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the two halves
    lst = merge(left, right)
    
    return lst

           
#%% Implementing Heap Sort
    
def heap_sort(lst):
    
    ###################################
    def max_heapify(lst, i, heap_size):
        
        # if lst[i] is a leaf do nothing
        if i >= heap_size // 2:
            return lst
        
        # Find the largest of node and its children - lst[i], lst[2i + 1] and 
        # lst[2i + 2].
        l = 2*i + 1
        r = 2*i + 2
        largest = i
        if r < heap_size and lst[r] >= lst[i]:
            largest = r
        if l < heap_size and lst[l] >= lst[largest]:
            largest = l
            
        # If max-heap-property is violated, fix it
        if largest != i:
            tmp = lst[i]
            lst[i] = lst[largest]
            lst[largest] = tmp
            lst = max_heapify(lst, largest, heap_size)
        
        return lst
    ###################################
    
    ###################################
    def build_max_heap(lst, heap_size):
        
        # A heap with one element is already a max heap
        if heap_size <= 1:
            return lst
        
        # Starting from the first element of the heap that is not a leaf up to the root
        for i in range((heap_size // 2 - 1), -1, -1):
            lst = max_heapify(lst, i, heap_size)
            
        return lst
    ###################################
    
    heap_size = len(lst)
    lst = build_max_heap(lst, heap_size)
    
    for i in range(heap_size - 1, 0, -1):
        # Move the first (and highest value) element of the current heap to the 
        # back of the current heap
        tmp = lst[0]
        lst[0] = lst[i]
        lst[i] = tmp
        # Reduce the heap size for one, so as to exclude the sorted elements
        heap_size = heap_size - 1
        lst = max_heapify(lst, 0, heap_size)
    
    return lst

#%% Main
n = 100000

lst = create_array(n)
print 'STATISTICS FOR HEAP SORT'
profile.run('lst = heap_sort(lst)')

lst = create_array(n)
print 'STATISTICS FOR MERGE SORT'
profile.run('lst = merge_sort(lst)')

lst = create_array(n)
print 'STATISTICS FOR INSERTION SORT'
profile.run('insertion_sort(lst)')

# for n = 100,000, Heapsort = 16.335s, Mergesort = 18.945s, Insertionsort = 2050s
# One key difference is that for the current implementations, Mergesort and Insertionsort
# sort the elements from largest to smallest and Heapsort from smallest to largest



    
