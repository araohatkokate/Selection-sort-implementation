def selection_sort_algorithm(arr):
    length = len(arr)
    for i in range(length):
        min_val = i
        for j in range(i+1,length):
            if arr[j]<arr[min_val]:
                min_val = j

        arr[i], arr[min_val] = arr[min_val], arr[i]

    return arr


