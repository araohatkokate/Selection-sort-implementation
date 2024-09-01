import timeit
import random
import matplotlib

import matplotlib.pyplot as plt

def bubble_sort_algorithm(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0,length-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

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

def selection_sort_algorithm(arr):
    length = len(arr)
    for i in range(length):
        min_val = i
        for j in range(i+1,length):
            if arr[j]<arr[min_val]:
                min_val = j

        arr[i], arr[min_val] = arr[min_val], arr[i]

    return arr

def benchmark_sorting_algorithms():
    input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
    bubble_sort_times = []
    insertion_sort_times = []
    selection_sort_times = []

    for size in input_sizes:
        random_array = [random.randint(0, 10000) for _ in range(size)]

        bubble_sort_time = timeit.timeit(stmt='bubble_sort_algorithm(arr.copy())',
                                         setup=f"from __main__ import bubble_sort_algorithm; arr={random_array}",
                                         number=10)
        bubble_sort_times.append(bubble_sort_time)

        insertion_sort_time = timeit.timeit(stmt='insertion_sort_algorithm(arr.copy())',
                                            setup=f"from __main__ import insertion_sort_algorithm; arr={random_array}",
                                            number=10)
        insertion_sort_times.append(insertion_sort_time)

        selection_sort_time = timeit.timeit(stmt='selection_sort_algorithm(arr.copy())',
                                            setup=f"from __main__ import selection_sort_algorithm; arr={random_array}",
                                            number=10)
        selection_sort_times.append(selection_sort_time)

    plt.figure(figsize=(12, 6))
    plt.plot(input_sizes, bubble_sort_times, label='Bubble Sort')
    plt.plot(input_sizes, insertion_sort_times, label='Insertion Sort')
    plt.plot(input_sizes, selection_sort_times, label='Selection Sort')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithms Benchmark using timeit')
    plt.legend()
    plt.grid(True)
    plt.show()

benchmark_sorting_algorithms()