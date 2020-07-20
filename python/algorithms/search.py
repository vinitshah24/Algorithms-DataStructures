""" Searching Algorithms """
import random
import math


def generate_test_data():
    myList = []
    for i in range(10):
        myList.append(random.randint(0, 50))
    search_num = random.choice(myList)
    return myList, search_num


def apply_searching(algo_name, algo_func, search_list, search_term):
    print("Applying " + algo_name)
    print("Initial List: " + str(search_list))
    print("Search Term: " + str(search_term))
    num_found = algo_func(search_list, search_term)
    print("Search Location: " + str(num_found) + "\n")


def linear_search(myList, search):
    # TIME BEST:       O(1)
    # TIME AVERAGE:    O(n)
    # TIME WORST:      O(n)
    # SPACE WORST:     O(1)
    for i in range(len(myList)):
        if myList[i] == search:
            return i
    return -1


def binary_search(ordered_list, search):
    # TIME BEST:       O(1)
    # TIME AVERAGE:    O(logn)
    # TIME WORST:      O(logn)
    # SPACE WORST:     O(1)
    """ Requires Sorted Array"""
    lower_bound = 0
    upper_bound = len(ordered_list)-1
    while lower_bound <= upper_bound:
        mid_value = (lower_bound + upper_bound) // 2
        if ordered_list[mid_value] == search:
            return mid_value
        else:
            if ordered_list[mid_value] < search:
                lower_bound = mid_value + 1
            else:
                upper_bound = mid_value - 1
    return -1


def jump_search(ordered_list, search):
    pointer = 0
    step = int(math.sqrt(len(ordered_list)))
    for i in range(0, len(ordered_list), step):
        if ordered_list[i] < search:
            pointer = i
        elif ordered_list[i] == search:
            return i
        else:
            break
    for j in ordered_list[pointer:]:
        if j == search:
            return pointer
        pointer += 1
    return -1


# Sorted array of uniformily distributed values 1-3-5-7
#         search_val - arr[low]
# low +  ----------------------- * (high - low)
#         arr[high] - arr[low]
def nearest_mid(ordered_list, low_index, high_index, search_val):
    return low_index + \
        (
            (search_val - ordered_list[low_index]) //
            (ordered_list[high_index] - ordered_list[low_index])
        ) * (high_index - low_index)


def interpolation_search(ordered_list, search_val):
    list_size = len(ordered_list) - 1
    first_index = 0
    last_index = list_size
    while first_index <= last_index:
        mid_point = nearest_mid(
            ordered_list, first_index, last_index, search_val)
        if mid_point > last_index or mid_point < first_index:
            return -1
        if ordered_list[mid_point] == search_val:
            return mid_point
        if search_val > ordered_list[mid_point]:
            first_index = mid_point + 1
        else:
            last_index = mid_point - 1
    return -1


# Uses bnary search when the exponential jumnp goes over limit
def binarySearch(arr, lower_bound, upper_bound, search_term):
    if upper_bound >= lower_bound:
        mid = int(lower_bound + (upper_bound-lower_bound) // 2)
        if arr[mid] == search_term:
            return mid
        if arr[mid] > search_term:
            return binarySearch(arr, lower_bound, mid - 1, search_term)
        return binarySearch(arr, mid + 1, upper_bound, search_term)
    return -1


def exponential_search(ordered_list, search_term):
    if ordered_list[0] == search_term:
        return 0
    i = 1
    while i < len(ordered_list) and ordered_list[i] <= search_term:
        i = i * 2
    return binarySearch(ordered_list, i / 2, min(i, len(ordered_list)), search_term)


def ternarySearch_(ordered_list, search_term):
    left = 0
    right = len(ordered_list) - 1
    while right >= left:
        mid1 = left + (right-left) // 3
        mid2 = right - (right-left) // 3
        if search_term == ordered_list[mid1]:
            return mid1
        if search_term == ordered_list[mid2]:
            return mid2
        if search_term < ordered_list[mid1]:
            # key lies between l and mid1
            right = mid1 - 1
        elif search_term > ordered_list[mid2]:
            # key lies between mid2 and r
            left = mid2 + 1
        else:
            # key lies between mid1 and mid2
            left = mid1 + 1
            right = mid2 - 1
    return -1


def ternary_search(arr, to_find):
    left = 0
    right = len(arr) - 1
    while left <= right:
        temp2 = left + (right - left) // 3
        temp3 = left + 2 * (right - left) // 3
        if to_find == arr[left]:
            return left
        elif to_find == arr[right]:
            return right
        elif to_find < arr[left] or to_find > arr[right]:
            return -1
        elif to_find <= arr[temp2]:
            right = temp2
        elif to_find > arr[temp2] and to_find <= arr[temp3]:
            left = temp2 + 1
            right = temp3
        else:
            left = temp3 + 1
    return -1


def ternarySearch(ordered_list, left, right, search_term):
    if right - left > 0:
        mid1 = left + (right-left) // 3
        mid2 = mid1 + (right-left) // 3
        if ordered_list[mid1] == search_term:
            return mid1
        if ordered_list[mid2] == search_term:
            return mid2
        # 0 - mid1
        if search_term < ordered_list[mid1]:
            return ternarySearch(ordered_list, left, mid1, search_term)
        # mid2 - end
        if search_term > ordered_list[mid2]:
            return ternarySearch(ordered_list, mid2 + 1, right, search_term)
        return ternarySearch(ordered_list, mid1, mid2, search_term)
    else:
        return -1


def fibonacci_search(ordered_list, search_val):
    # Initialize the Fibonacci numbers
    fib1, fib2 = 1, 0
    fibn = fib2 + fib1
    data_len = len(ordered_list)
    while fibn < data_len:
        fib2 = fib1
        fib1 = fibn
        fibn = fib2 + fib1
    offset = -1
    while fibn > 1:
        n = min(offset + fib2, data_len - 1)
        if ordered_list[n] > search_val:
            fibn = fib2
            fib1 = fib1 - fib2
            fib2 = fibn - fib1
        elif ordered_list[n] < search_val:
            fibn = fib1
            fib1 = fib2
            fib2 = fibn - fib1
            offset = n
        else:
            return n
    if ordered_list[offset + 1] == n and fib1 == 1:
        return offset + 1
    return -1


def FibonacciSearch(ordered_list, search_val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while fibM < len(ordered_list):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while fibM > 1:
        i = min(index + fibM_minus_2, (len(ordered_list)-1))
        if ordered_list[i] < search_val:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif ordered_list[i] > search_val:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i
    if fibM_minus_1 and index < (len(ordered_list)-1) and ordered_list[index+1] == search_val:
        return index+1
    return -1


input_list, search_num = generate_test_data()
apply_searching("Linear Search", linear_search, input_list, search_num)
# Requires Sorted List
input_list.sort()
apply_searching("Binary Search", binary_search, input_list, search_num)
apply_searching("Jump Search", jump_search, input_list, search_num)
apply_searching("Interpolation Search",
                interpolation_search, input_list, search_num)
apply_searching("Exponential Search", exponential_search,
                input_list, search_num)
apply_searching("Ternary Search", ternary_search, input_list, search_num)
apply_searching("Fibonacci Search", fibonacci_search, input_list, search_num)
