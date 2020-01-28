def binary_search(list, item):
    
    low = 0
    
    high = len (list) - 1
    
    while low <= high :
        
        mid = (low+high ) // 2
        
        guess = list[mid]
        
        if guess == item :
            
            return mid 
        if guess > item :
            
            high = mid - 1
            
        else : 
            
            low = mid + 1
            
    return None

my_list = [ 5, 7, 11, 14, 19, 20, 22 ]

print( binary_search ( my_list, 14))
        
print( binary_search ( my_list, 22))
