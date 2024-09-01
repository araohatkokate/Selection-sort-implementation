def insertion_sort_algorithm(arr):
    length = len(arr)
    for i in range(1,length):
        swap = arr[i]
        j=i-1
        while j>=0 and swap<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
            arr[j+1] = swap
    return arr