def trouvepetit (arr):
    petit = arr [0]
    petit_index = 0
    for i in range (1, len (arr)) :
        if arr[i] < petit:
            petit = arr [i]
            petit_index = i
    return petit_index

def selectionSort (arr):
    newArr = []
    for i in range (len(arr)):
        petit = trouvepetit (arr) 
        newArr.append(arr.pop(petit))
    return newArr

print (selectionSort([10, 90, 80, 20, 30]))
