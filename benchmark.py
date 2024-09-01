import time
import random
import matplotlib.pyplot as plt
import platform

# Sorting Algorithms
def selection_sort_algorithm(arr):
    length = len(arr)
    for i in range(length):
        min_val = i
        for j in range(i+1, length):
            if arr[j] < arr[min_val]:
                min_val = j
        arr[i], arr[min_val] = arr[min_val], arr[i]
    return arr

def bubble_sort_algorithm(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort_algorithm(arr):
    length = len(arr)
    for i in range(1, length):
        swap = arr[i]
        j = i-1
        while j >= 0 and swap < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = swap
    return arr

# Benchmark Function
def benchmark_sorting_algorithm(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())  # Use arr.copy() to avoid sorting the same array multiple times
    end_time = time.time()
    return end_time - start_time

# Simple System Information
def get_system_info():
    info = {
        "Processor": platform.processor(),
        "Machine": platform.machine(),
        "Platform": platform.platform(),
    }
    return info

# Run Benchmarks with Varying Input Sizes
def run_benchmarks():
    input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
    selection_sort_times = []
    bubble_sort_times = []
    insertion_sort_times = []

    for size in input_sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
        selection_sort_times.append(benchmark_sorting_algorithm(selection_sort_algorithm, arr))
        bubble_sort_times.append(benchmark_sorting_algorithm(bubble_sort_algorithm, arr))
        insertion_sort_times.append(benchmark_sorting_algorithm(insertion_sort_algorithm, arr))

    return input_sizes, selection_sort_times, bubble_sort_times, insertion_sort_times

# Plot Benchmark Results
def plot_benchmarks(input_sizes, selection_sort_times, bubble_sort_times, insertion_sort_times):
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, selection_sort_times, label='Selection Sort', marker='o')
    plt.plot(input_sizes, bubble_sort_times, label='Bubble Sort', marker='o')
    plt.plot(input_sizes, insertion_sort_times, label='Insertion Sort', marker='o')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Benchmark')
    plt.legend()
    plt.grid(True)
    
    # Save the plot to a file
    plt.savefig('sorting_algorithm_benchmark.png')
    print("Benchmark plot saved as 'sorting_algorithm_benchmark.png'.")

# Main Execution
if __name__ == "__main__":
    system_info = get_system_info()
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")
    
    input_sizes, selection_sort_times, bubble_sort_times, insertion_sort_times = run_benchmarks()
    plot_benchmarks(input_sizes, selection_sort_times, bubble_sort_times, insertion_sort_times)
