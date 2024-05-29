def quicksort (arr):
    if len(arr) <= 1: # Si la lista (que luego seran los subarrays) tiene 1 o 0 elementos, retorno la lista
        return arr
    pivot = arr[0] # Tomo de pivot al primer elemento de la lista
    less = [i for i in arr[1:] if i <= pivot] # Tomo todos los elementos menores o iguales al pivot y los guardo en less
    greater = [i for i in arr[1:] if i > pivot] # Tomo todos los elementos mayores al pivot y los guardo en greater
    return quicksort(less) + [pivot] + quicksort(greater) # Retorno el quicksort de less, el pivot y el quicksort de greater

assert quicksort([3,6,8,10,1,2,1]) == [1,1,2,3,6,8,10]