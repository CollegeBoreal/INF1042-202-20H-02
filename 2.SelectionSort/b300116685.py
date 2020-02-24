def selectionSort(arr):
    smallest = arr[0]
    smallest_index = 0

for i in range(1, len(arr)):


    if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            
 
      return smallest_index



def selectionSort(arr):
    nouveau_arr = []

for i in range(len(arr)):
        smallest = selectionSort(arr)
        nouveau_arr.append(arr.pop(smallest))

  
     return nouveau_arr


print(selectionSort([5,3,6,2,10]))
