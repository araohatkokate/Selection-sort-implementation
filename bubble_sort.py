def bubble_sort_algorithm(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0,length-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr = [64,34,25,12,22,11,90]
sort = bubble_sort_algorithm(arr)
print(sort)
