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

def binarySearch(arr3, val, start_idx=0, exit_idx=len(arr3)):
    
    mid_point_idx = (start_idx + exit_idx)//2
    try:
        if arr3[mid_point_idx] == val:
            print(val, 'occurs at index', mid_point_idx, '\n')
            return mid_point_idx

        elif arr3[mid_point_idx] > val:
            binarySearch(val, start_idx, mid_point_idx)
        
        elif arr3[mid_point_idx] < val:
            binarySearch(val, mid_point_idx, exit_idx)
    except RecursionError:
        print('Recursion Error: maximum recursion depth exceeded. for val', val, '\n')
    finally:
        return
    
idx = binarySearch(arr3=arr3, val=2)
idx = binarySearch(arr3=arr3, val=-1)
idx = binarySearch(arr3=arr3, val=7)

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
res_arr = insertionBeyondIterableHashedAlgo({1: 1, 8: [2, 5, 7], 10: 1})
print('res_arr after insertion', res_arr)

res_arr = insertionBeyondIterableHashedAlgo({-5: [0, 3], 8: 2, -7: []}, res_arr)
print('res_arr after insertion', res_arr)

# Delete element (by default deletes only first occurrence) by in-built operation
print("\n" + "Deleting elements -")
try:
    print('res_arr', res_arr)
    res_arr.remove(-5)
except ValueError:
    print("res_arr doesn't have element", -5)
finally:
    print('res_arr after deletion of element -5 present in it: ', res_arr)

try:
    print('\nres_arr', res_arr)
    res_arr.remove(6)
except ValueError:
    print("res_arr doesn't have element", 6)
finally:
    print('res_arr after deletion of element 6 not present in it: ', res_arr)

# delete implemented
def deletionSingleOccurenceAlgo(val, arr_n):

    # element has to be present if not.. return the iterable as it is
    len_arr = len(arr_n)
    count = 0
    idx = 0
    while idx < len_arr:
        if arr_n[idx] == val:
            count += 1
            while idx < len_arr - count:
                arr_n[idx] = arr_n[idx+1]
                idx += 1
        idx += 1

    if count > 0:
        return arr_n[:idx-1]

    return arr_n

print('\nres_arr before deletion', res_arr)
res_arr = deletionSingleOccurenceAlgo(-5, res_arr)
print('res_arr after deleting an element -5 present in it: ', res_arr)

print('res_arr before deletion', res_arr)
res_arr = deletionSingleOccurenceAlgo(6, res_arr)
print('res_arr after deleting an element 6 not present in it: ', res_arr)

# delete a sequence of elements
def deletionIterableAlgo(arr_temp, arr_x):

    for i in arr_temp:
        arr_x = deletionSingleOccurenceAlgo(i, arr_x)

    return arr_x

print('\nres_arr before deletion', res_arr)
res_arr = deletionIterableAlgo([8, 6], res_arr)
print('res_arr after deleting [8, 6]:', res_arr)

# delete an element at a specific index
def deletionSpecificIndexAlgo(val, idx_specified, arr_x):

    # element has to be present at that index.. return the iterable as it is
    len_arr = len(arr_x)
    idx = 0
    count = 0
    while idx < len_arr:
        if idx == idx_specified and arr_x[idx] == val:
            while idx < len_arr - 1:
                arr_x[idx] = arr_x[idx+1]
                idx += 1
            count += 1
        idx += 1
    if count > 0:
        return arr_x[:idx-1]

    return arr_x

print('\nres_arr before deletion', res_arr)
res_arr = deletionSpecificIndexAlgo(8, 2, res_arr)
print('res_arr after deleting 8 at index 2 where it is not present:', res_arr)

print('\nres_arr before deletion', res_arr)
res_arr = deletionSpecificIndexAlgo(8, 3, res_arr)
print('res_arr after deleting 8 at index 3 where it is present:', res_arr)

# delete a sequence of elements present at specified indices
"""
dict1 = {num1: [idx1, idx2], num2: idx3, num3: []}
"""
def deletionHashedAlgo(dict_temp, arr_x):

    for num_to_del, idx_at_del in dict_temp.items():
        if type(idx_at_del) != list:
            arr_x = deletionSpecificIndexAlgo(num_to_del, idx_at_del, arr_x)
        else:
            if idx_at_del:
                for jdx_at_del in idx_at_del:    
                    arr_x = deletionSpecificIndexAlgo(num_to_del, jdx_at_del, arr_x)
    return arr_x

print('\nres_arr before deletion', res_arr)
res_arr = deletionHashedAlgo({8: [3, 5], 6: [], 10: [], 0: [0, 4]}, res_arr)
print('res_arr after deleting following: 8: [3, 6], 6: [], 10: [], 0: 0, 4: 5:', res_arr)

# delete substrings
"""
list1 = [(start_idx1, end_idx1), (start_idx2, end_idx2)]
"""
def deletionIdxAlgo(start_idx, end_idx, arr_x):

    # element has to be present at that index.. return the iterable as it is
    len_arr = len(arr_x)
    idx = 0
    count = 0
    while idx < len_arr:
        if idx == start_idx:
            while idx < end_idx and end_idx < len(arr_x):
                arr_x[idx] = arr_x[idx + 1]
                idx += 1
            count += 1
        idx += 1

    if count > 0:
        return arr_x[: len_arr - (end_idx - start_idx)]

    return arr_x

def deletionSubstringsIterableAlgo(temp_list, arr_temp):

    count = 0
    while count < len(temp_list) and temp_list[count][0] < len(arr_temp):
        arr_temp = deletionIdxAlgo(temp_list[count][0], temp_list[count][1], arr_temp)        
        count += 1

    return arr_temp

print('\nres_arr before deletion', res_arr)
res_arr = deletionSubstringsIterableAlgo([(2, 4)], res_arr)
print('res_arr after deleting indices: [(2, 4)]', res_arr)


print('\nres_arr before deletion', arr3)
res_arr = deletionSubstringsIterableAlgo([(2, 4), (7, 13), (7, 10)], arr3)
print('res_arr after deleting indices: [(2, 4), (7, 13), (7, 10)]', res_arr)

# delete element occurring multiple times
def deletionMultipleOccurrenceLinearSearchAlgo(val, arr_x):

    len_arr = len(arr_x)
    for kdx in arr_x:
        if kdx == val:
            arr_x = deletionSingleOccurenceAlgo(kdx, arr_x)

    return arr_x

print('\nres_arr before deletion', res_arr)
res_arr = deletionMultipleOccurrenceLinearSearchAlgo(8, res_arr)
print('res_arr after deleting an element 8 present in it multiple times: ', res_arr)

print('res_arr before deletion', res_arr)
res_arr = deletionMultipleOccurrenceLinearSearchAlgo(0, res_arr)
print('res_arr after deleting an element 0 present in it multiple times: ', res_arr)

# delete elements occurring multiple times in random array
# delete elements repeated leaving except 1
# delete repeat elements except at 1 particualr index
"""
arr1 = [1, 2, 4, 4, 4, 8, 3, 3, 5, 6, 7, 4, 4, 4, 4, 4, 6, 4, 4, 4]
"""
# def deleteMultipleOccurrenceBinarySearchAlgo(val, arr_x):

#     idx = binarySearch(arr_x, val)
#     if not idx:
#         return arr_x

#     arr_x = deletionSingleOccurenceAlgo(val, arr_x)

# print('\nres_arr before deletion', res_arr)
# res_arr = deletionMultipleOccurrenceBinarySearchAlgo(8, res_arr)
# print('res_arr after deleting an element 8 present in it multiple times: ', res_arr)

# print('res_arr before deletion', res_arr)
# res_arr = deletionMultipleOccurrenceBinarySearchAlgo(0, res_arr)
# print('res_arr after deleting an element 0 present in it multiple times: ', res_arr)

# largest window with start_idx and end_idx
def valMaxParseData(tuples_windows):

    len_windows_tuple = len(tuples_windows)
    odd_nums = even_nums = []
    _diffs = {}
    idx = 0
    while idx < len_windows_tuple:
        diff = tuples_windows[idx+1] - tuples_windows[idx]
        if diff in _diffs:
            z = len(_diffs[diff])
            _diffs[diff][len(_diffs[diff]):] = [(tuples_windows[idx+1], tuples_windows[idx])]
        else:
            _diffs[diff] = [(tuples_windows[idx+1], tuples_windows[idx])]
        idx += 2

    max_data = max(sorted(_diffs))
    return max_data, _diffs[max_data]

def largestWindowSearchElementAlgo(val, arr_x):

    idx = 0
    len_arrx = len(arr_x)

    window_tuples_list = []    
    while idx < len_arrx:
        if arr_x[idx] == val:
            jdx = idx + 1
            count = 0
            while jdx < len_arrx and arr_x[jdx] == val:
                jdx += 1
                count += 1
            window_tuples_list[len(window_tuples_list):] = (idx, jdx)
            idx += count
        idx += 1

    if len(window_tuples_list) == 0:
        return "Element doesn't exist in arr."

    if len(window_tuples_list) == 2:
        return window_tuples_list[1] - window_tuples_list[0]

    max_val, windows_list_groups = valMaxParseData(window_tuples_list)

    smallest_idx_window = windows_list_groups[0] 
    largest_idx_window = windows_list_groups[-1]

    return {
        'window size': max_val,
        'smallest_idx': smallest_idx_window,
        'largest_idx': largest_idx_window
    }

print("\n" + "Largest window search for element")
arr_x = arr.array("i", [1, 2, 4, 4, 4, 8, 3, 3, 5, 6, 7, 4, 4, 4, 4, 4, 6, 8, 4, 4, 4, 4, 4])
print('arr_x: ', arr_x)
res_arr = largestWindowSearchElementAlgo(-5, arr_x)
print('largest window search element algo for arr_x: ', res_arr)

print('arr_x: ', arr_x)
res_arr = largestWindowSearchElementAlgo(4, arr_x)
print('largest window search element algo for arr_x: ', res_arr)
