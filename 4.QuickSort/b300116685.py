def quicksort(array):
    # base case
    if len(array) < 2:
        return array
    else:
        #recursive case
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less ) + [pivot] + quicksort(greater)

print(quicksort([ 75, 50, 95, 105,25]))