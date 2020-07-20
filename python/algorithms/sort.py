""" Sorting Algorithms """
from random import randint


def generate_random_list():
    myList = []
    for i in range(10):
        myList.append(randint(0, 50))
    return myList


def apply_sorting(algo_name, algo_func, input_list):
    print("Applying " + algo_name)
    print("Initial List: " + str(input_list))
    sorted_list = algo_func(input_list)
    print("Sorted List: " + str(sorted_list) + "\n")


def selection_sort(myList):
    # TIME BEST:       O(n^2)
    # TIME AVERAGE:    O(n^2)
    # TIME WORST:      O(n^2)
    # SPACE WORST:     O(1)
    for i in range(len(myList) - 1):
        min_pos = i
        for j in range(i, len(myList)):
            if myList[min_pos] > myList[j]:
                min_pos = j
        temp = myList[i]
        myList[i] = myList[min_pos]
        myList[min_pos] = temp
    return myList


def bubble_sort(myList):
    # TIME BEST:       O(n)
    # TIME AVERAGE:    O(n^2)
    # TIME WORST:      O(n^2)
    # SPACE WORST:     O(1)
    for i in range(len(myList)-1, 0, -1):
        for j in range(i):
            if myList[j] > myList[j+1]:
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
    return myList


def insertion_sort(myList):
    # TIME BEST:       O(n)
    # TIME AVERAGE:    O(n^2)
    # TIME WORST:      O(n^2)
    # SPACE WORST:     O(1)
    for i in range(1, len(myList)):
        while i > 0 and myList[i-1] > myList[i]:
            temp = myList[i]
            myList[i] = myList[i-1]
            myList[i-1] = temp
            i = i - 1
    return myList


def insertionSort(myList):
    for i in range(1, len(myList)):
        j = i-1
        while j >= 0 and myList[i] < myList[j]:
            myList[j+1] = myList[j]
            j -= 1
        myList[j+1] = myList[i]
    return myList


def merge_sort(myList):
    # TIME BEST:       O(nlogn)
    # TIME AVERAGE:    O(nlogn)
    # TIME WORST:      O(nlogn)
    # SPACE WORST:     O(n)
    if len(myList) <= 1:
        return myList
    mid = int(len(myList)/2)
    # Recursively break the array
    left = merge_sort(myList[:mid])
    right = merge_sort(myList[mid:])
    # After complete breakdown, combine
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j = j+1
    result += left[i:]
    result += right[j:]
    return result


def quick_sort(myList):
    # TIME BEST:       O(nlogn)
    # TIME AVERAGE:    O(nlogn)
    # TIME WORST:      O(n^2)
    # SPACE WORST:     O(logn)
    # base case
    if len(myList) <= 1:
        return myList
    smaller, equal, larger = [], [], []
    if len(myList) > 1:
        pivot = myList[0]
        for i in myList:
            if i < pivot:
                smaller.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                larger.append(i)
        # Call recursively
        return quick_sort(smaller) + equal + quick_sort(larger)


def quickSort(myList):
    length = len(myList)
    if length <= 1:
        return myList
    else:
        pivot = myList.pop()
    items_greater = []
    items_lower = []
    for item in myList:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quickSort(items_lower) + [pivot] + quickSort(items_greater)


def bucket_sort(myList):
    largest = max(myList)
    length = len(myList)
    size = largest/length
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(myList[i]/size)
        if j != length:
            buckets[j].append(myList[i])
        else:
            buckets[length - 1].append(myList[i])
    for i in range(length):
        insertion_sort(buckets[i])
    result = []
    for i in range(length):
        result = result + buckets[i]
    return result


def bucket_sort_decimal(myList):
    bucket = []
    # Create empty buckets
    for i in range(len(myList)):
        bucket.append([])
    # Insert elements into their respective buckets
    for j in myList:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    # Sort the elements of each bucket
    for i in range(len(myList)):
        bucket[i] = sorted(bucket[i])
    # Get the sorted elements
    k = 0
    for i in range(len(myList)):
        for j in range(len(bucket[i])):
            myList[k] = bucket[i][j]
            k += 1
    return myList


def counting_sort(myList):
    max_value = max(myList)
    counts = [0] * (max_value + 1)
    for item in myList:
        counts[item] += 1
    # Overwrite counts to hold the next index an item with a given value goes
    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count
    # Output list to be filled in
    sorted_list = [None] * len(myList)
    # Run through the input list
    for item in myList:
        # Place the item in the sorted list
        sorted_list[counts[item]] = item
        # Next item we see with the same value goes after the one just placed
        counts[item] += 1
    return sorted_list


def gap_insertion_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position-gap
        alist[position] = currentvalue


def shell_sort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(alist, startposition, sublistcount)
        sublistcount = sublistcount // 2
    return alist


apply_sorting("Selection Sort", selection_sort, generate_random_list())
apply_sorting("Bubble Sort", bubble_sort, generate_random_list())
apply_sorting("Insertion Sort", insertion_sort, generate_random_list())
apply_sorting("Merge Sort", merge_sort, generate_random_list())
apply_sorting("Quick Sort", quick_sort, generate_random_list())
apply_sorting("Bucket Sort", bucket_sort, generate_random_list())
apply_sorting("Bucket Sort Decimal", bucket_sort_decimal,
              [.42, .32, .33, .52, .37, .47, .51])
# Works best for duplicates and stable outputs
apply_sorting("Counting Sort", counting_sort, generate_random_list())
apply_sorting("Shell Sort", shell_sort, generate_random_list())
