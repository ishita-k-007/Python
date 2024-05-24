"""
Arrays: homogenous contiguous memory locations.
    - Accessing every element in array: O(1) in space-complecity and O(1) in time complexity.
    - Searching for specific element in array:
        - O(len(n)) for traversing the unsorted array.
        - O(log(len(n))) traversing the sorted array.
    - Insertion/deletion of element:
        - O(1) if element to be inserted/deleted at the end.
        - O(len(m)) for inserting in the array somewhere at mth position and shifting the rest elements likewise.
"""

import array as arr
from array import *

# array initializations
arr1 = [1, 2, 3.4, 5]
print('arr1: ', arr1)

arr2 = [-1.3, 4.0, 6, 7]
print('arr2: ', arr2)

print("\n" + 'These are defined as lists.' + "\n")

# i: integer type; d: float type
arr3 = arr.array("i", [1, 2, 3, 4])
print('arr3: ', arr3)

arr4 = arr.array("d", [1, 2.3, 5.6, -7])
print('arr4: ', arr4)

print("\n" + 'These are defined as arrays.')

# Accessing elements
print("\n" + "Accessing elements - 0-based indexing")
print(arr3[2], 'second in arr3')
print(arr4[3], 'third in arr4')

# Traversing elements
print("\n" + "Traversing array elements - 0-based indexing")
print("arr3 elements: ")
for i in arr3:
    print(i)

print("\n" + "arr4 elements: ")
for j in arr4:
    print(j)

# Searching elements
print("\n" + "Searching elements -")
print("2 in sorted arr3: linear search - ")
for i in arr3:
    if i == 3:
        print("3 occurs at:", arr3.index(i))

print("\n" + "2 in sorted arr3: binary search - ")

def binarySearch(val, start_idx=0, exit_idx=len(arr3)):
    
    mid_point_idx = (start_idx + exit_idx)//2
    try:
        if arr3[mid_point_idx] == val:
            print(val, 'occurs at index', mid_point_idx, '\n')

        elif arr3[mid_point_idx] > val:
            binarySearch(val, start_idx, mid_point_idx)
        
        elif arr3[mid_point_idx] < val:
            binarySearch(val, mid_point_idx, exit_idx)
    except RecursionError:
        print('Recursion Error: maximum recursion depth exceeded. for val', val, '\n')
    finally:
        return
    
binarySearch(val=2)
binarySearch(val=-1)
binarySearch(val=7)

print("2.3 in un-sorted arr4: linear search - ")
for i in arr4:
    if i == 2.3:
        print("2.3 occurs at:", arr4.index(i))

# Insert elements
print("\n" + "Inserting elements -")
print("5 at last index in arr3: ")

arr3.insert(len(arr3), 5)
print('arr3 after insertion at end: ', arr3)

arr3.insert(2, 6)
print('arr3 after insertion at index-2: ', arr3)

# inserting a single element at an index
def insertionAlgo(val, int_idx, arr3):
    
    len_arr3 = len(arr3)

    # start index = 0
    if int_idx == 0:
        arr_temp = arr.array("i", [val])
        arr_temp[len(arr_temp):] = arr.array("i", arr3)
        arr3 = arr_temp
        return arr3

    # end index = len(arr)
    if int_idx == len_arr3:
        arr3[len_arr3: ] = arr.array("i", [val])
        return arr3

    # middle index != 0 and != len(arr) --> increase the size of the array
    arr3[len_arr3:] = arr.array("i", [arr3[len_arr3-1]])

    idx = 0
    while idx < len_arr3:
        if idx == int_idx:
            temp = arr3[idx]
            arr3[idx] = val
        elif idx > int_idx:
            x = arr3[idx]
            arr3[idx] = temp
            temp = x
        idx += 1
    return arr3

arr_res = insertionAlgo(8, 0, arr3)
print('arr3 at index: 0 after insertion', arr_res)

arr_res = insertionAlgo(-2, 3, arr3)
print('arr3 at index: 3 after insertion', arr_res)

arr_res = insertionAlgo(-1, 7, arr3)
print('arr3 at index: last indx after insertion', arr_res)

# inserting an iterable
def insertionIterableAlgo(arr_temp, start_idx, arr3):
    
    len_arr3 = len(arr3)

    # start index = 0
    if start_idx == 0:
        arr_temp = arr.array("i", arr_temp)
        arr_temp[len_arr3:] = arr.array("i", arr3)
        arr3 = arr_temp
        return arr3

    # end index = len(arr)
    if start_idx == len_arr3:
        arr3[len_arr3: ] = arr.array("i", arr_temp)
        return arr3

    # middle index != 0 and != len(arr) --> increase the size of array
    len_arr_temp = len(arr_temp)
    _temp = arr.array("i", arr_temp)
    arr3[len_arr3:] = arr.array("i", _temp)
    arr_temp[len(arr_temp):] = arr.array("i", arr3[start_idx: len_arr3])

    idx = 0
    while idx < len_arr3:
        if idx == start_idx:
            jdx = 0
            while jdx < len(arr_temp):
                arr3[idx] = arr_temp[jdx]
                jdx += 1
                idx += 1
        idx += 1
    return arr3

print("\nInsert a sequence of elements - iterables")
res_arr = insertionIterableAlgo([1,8], 0, arr3)
print('arr3 at index: 0 after insertion', res_arr)

res_arr = insertionIterableAlgo([4, -2], 3, arr3)
print('arr3 at index: 3 after insertion', res_arr)

res_arr = insertionIterableAlgo([4, -2, 7], 3, arr3)
print('arr3 at index: 3 after insertion', res_arr)

res_arr = insertionIterableAlgo([7, -2], len(res_arr), arr3)
print('arr3 at index: last after insertion', res_arr)

# inserting various elemenst at defined positions from a dict/hash
"""
dict = {num1: idx1, num2: idx2}
"""
def insertionHashedAlgo(dict_temp, arr3):

    for num_to_insert, idx_to_insert in dict_temp.items():
        arr3 = insertionAlgo(num_to_insert, idx_to_insert, arr3)
    return arr3

print("\nInsert a hash of elements with defined indices- dict")
res_arr = insertionHashedAlgo({1: 1, 8: 2}, arr3)
print('arr3 after insertion', res_arr)

res_arr = insertionHashedAlgo({-5: 0, 8: 2, 3: 6}, arr3)
print('arr3 after insertion', res_arr)

# inserting elements at various multiple places from a dict/hash
"""
dict = {num1: [idx1, idx2], num2: idx3, num3: [idx4]}
"""
def insertionIterableHashedAlgo(dict_temp, arr3):

    for num_to_insert, idx_to_insert in dict_temp.items():
        if type(idx_to_insert) != list:
            arr3 = insertionAlgo(num_to_insert, idx_to_insert, arr3)
        else:
            if idx_to_insert:
                for jdx_to_insert in idx_to_insert:               
                    arr3 = insertionAlgo(num_to_insert, jdx_to_insert, arr3)
    return arr3

arr_n = arr.array("i", [-3, 2, 6, 5])
print("\nInsert a hash of elements with defined indices in a list or as single idx values - dict")
res_arr = insertionIterableHashedAlgo({1: 1, 8: [2, 5], 10: 1}, arr_n)
print('arr3 after insertion', res_arr)

res_arr = insertionIterableHashedAlgo({-5: [0, 3], 8: 2, -7: []}, arr_n)
print('arr3 after insertion', res_arr)

# inserting elements at various multiple places with 0 at non-specified indices being replaced
"""
dict = {num1: [idx1, idx2], num2: idx3, num3: [idx4]}
"""
def increase_len_arr(arr3, size_max):

    len_arr3 = len(arr3)
    max_size = size_max - len_arr3
    arr3[len_arr3:] = arr.array("i", [0]*max_size)
    return arr3

def insertionBeyondIterableHashedAlgo(dict_temp, arr3=arr.array("i", [])):

    max_len = 0
    for num_to_insert, idx_to_insert in dict_temp.items():
        if type(idx_to_insert) != list:
            max_len = max(max_len, idx_to_insert)
            if max_len != len(arr3):
                arr3 = increase_len_arr(arr3, max_len)
            arr3 = insertionAlgo(num_to_insert, idx_to_insert, arr3)
        else:
            if idx_to_insert:
                for jdx_to_insert in idx_to_insert:               
                    max_len = max(max_len, jdx_to_insert)
                    if max_len > len(arr3):
                        arr3 = increase_len_arr(arr3, max_len)
                    arr3 = insertionAlgo(num_to_insert, jdx_to_insert, arr3)
    return arr3

print("\nInsert a hash of elements with defined indices in a list or as single idx values - dict")
res_arr = insertionBeyondIterableHashedAlgo({1: 1, 8: [2, 5], 10: 1})
print('arr3 after insertion', res_arr)

res_arr = insertionBeyondIterableHashedAlgo({-5: [0, 3], 8: 2, -7: []}, res_arr)
print('arr3 after insertion', res_arr)

# Delete elements
# print("\n" + "Deleting elements -")
# print("-5 in arr3: ")

# arr3.insert(len(arr3), 5)
# print('arr3 after insertion at end: ', arr3)

# arr3.insert(2, 6)
# print('arr3 after insertion at index-2: ', arr3)

# idx = 0

# def insertionAlgo(val, int_idx):
    
#     idx = 0
#     len_arr3 = len(arr3)
#     arr3[len_arr3:] = arr.array("i", [arr3[len_arr3-1]])
#     while idx < len_arr3:
#         if idx == int_idx:
#             temp = arr3[idx]
#             arr3[idx] = val
#         elif idx > int_idx:
#             x = arr3[idx]
#             arr3[idx] = temp
#             temp = x
#         idx += 1

# insertionAlgo(8, 0)
# print('arr3 at index: 0 after insertion', arr3)

# insertionAlgo(-2, 3)
# print('arr3 at index: 3 after insertion', arr3)
