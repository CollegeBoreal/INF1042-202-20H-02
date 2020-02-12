# -*- coding : utf-8 -*-

def quicksort (array):
    if len(array) < 2 :
        return array
    else:
        pivot = array [0]
        less = [i for i in array [1:] if 1<= pivot]
        greater = [i for i in array [1:] if 1 > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print (quicksort([15,4,21,40,5,2]))