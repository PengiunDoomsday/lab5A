# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:04:47 2018

@author: Javier Soon
ID:      80436654
Professor: Diego Aguirre
T.A.:      Manoj Saha

Description: Had to created a insert and extract the min for the heap.
after which had to sort the heap.
"""


class Heap:
    
    
    def __init__(self):
        self.heap_array = []
     
     
    def insert(self, k):
        self.heap_array.append(k)
        
        i = len(self.heap_array) - 1
        
        while (i - 1 // 2) > 0:      # parent is greater than 0 

            if self.heap_array[i] < self.heap_array[(i - 1) // 2]:      # if the child is less than the parent it  will swap the parent with the child
                temp = self.heap_array[(i - 1) // 2]
                self.heap_array[(i - 1) // 2] = self.heap_array[i]
                self.heap_array[i] = temp
            i = (i - 1) // 2         # makes the index the parent to check again
        return self.heap_array

     
    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]       # changed the heap_array.append[0] to this because it would not work
                                            # makes a temp where the min is the temp
        
#        print('yo the min is ' , min_elem)  # made to check what the min was printing
 
        self.heap_array[0] = self.heap_array[len(self.heap_array) - 1]      # makes the first index of the list be the last item in the list
        self.heap_array.pop(len(self.heap_array) - 1)  # removes the last index in the list
        
        i = 0
      
        while (2 * i + 1) <= len(self.heap_array) - 1:      #if the "left_child" is not out of bounds it'll do this
            if (2 * i + 2) > len(self.heap_array) - 1:      # if the "right_child" is out of bounds it'll make the child the "left child"
                child = 2 * i + 1
                
            elif self.heap_array[2 * i + 1] < self.heap_array[2 * i + 2]:   # if the "left child" is less than the "right child" it'll make the child be the "left child"
                child = 2 * i + 1
            
            else:
                child = 2 * i + 2       # makes the child be the "right child
        
            if self.heap_array[i] > self.heap_array[child]: # swaps if the child with the parent
                temp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[child]
                self.heap_array[child] = temp
            
            i = child
                
        return min_elem
            
    
            
    
    def is_empty(self):
        return len(self.heap_array) == 0




