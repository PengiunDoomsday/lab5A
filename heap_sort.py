# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 23:06:22 2018

@author: Javier Soon
ID:      80436654
Professor: Diego Aguirre
T.A.:      Manoj Saha

Description: Had to created a insert and extract the min for the heap.
after which had to sort the heap.
"""
from lab5 import Heap

def main():
    heap = Heap()
    a = [5, 6, 7, 9, 10, 15, 1, 10, 1, 2, 5, 9, 76]
    heap_sorted = []
    
    for i in (a):
#        print(i)
#        print(heap.insert(i))
        heap.insert(i)
    
    for i in a:  
#        print(heap.extract_min())
        heap_sorted.append(heap.extract_min())
    
    for i in heap_sorted:

        print(i)


main()