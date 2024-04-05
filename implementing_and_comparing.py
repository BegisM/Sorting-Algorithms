import time
import random
import matplotlib.pyplot as plt

# Sorting Algorithms Implementation

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
# Implementing quick_sort without utilizing additional memory space is not feasible.
 

# Function to measure the running time of a sorting algorithm
def measure_running_time(sorting_function, array):
    start_time = time.time()
    sorting_function(array)
    end_time = time.time()
    elapsed_time_microseconds = (end_time - start_time) * 1_000
    return elapsed_time_microseconds

# Function to generate random input arrays of a given size
def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

# Testing and comparing running times
def test_comparison(sizes):
    bubble_sort_times = []
    insertion_sort_times = []
    merge_sort_times = []
    quick_sort_times = []
    buildin_sort_times = []

    for size in sizes:
        arr = generate_random_array(size)

        bubble_sort_times.append(measure_running_time(bubble_sort, arr.copy()))
        insertion_sort_times.append(measure_running_time(insertion_sort, arr.copy()))
        merge_sort_times.append(measure_running_time(merge_sort, arr.copy()))
        quick_sort_times.append(measure_running_time(quick_sort, arr.copy()))
        buildin_sort_times.append(measure_running_time(sorted, arr.copy()))
        
    plt.plot(sizes, bubble_sort_times, label='Bubble Sort')
    plt.plot(sizes, insertion_sort_times, label='Insertion Sort')
    plt.plot(sizes, merge_sort_times, label='Merge Sort')
    plt.plot(sizes, quick_sort_times, label='Quick Sort')
    plt.plot(sizes, buildin_sort_times, label='Buildin Sort') 

    plt.xlabel('Array Size')
    plt.ylabel('Running Time (ms)')
    plt.title('Comparison of Sorting Algorithms')
    plt.legend()
    plt.show()