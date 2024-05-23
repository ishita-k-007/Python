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

idx = 0

def insertionAlgo(val, int_idx):
    
    idx = 0
    arr3.extend([arr3[-1]])
    while idx < len(arr3):
        if idx == int_idx:
            temp = arr3[idx]
            arr3[idx] = val
        elif idx > int_idx:
            x = arr3[idx]
            arr3[idx] = temp
            temp = x
        idx += 1

insertionAlgo(8, 0)
print('arr3 at index: 0 after insertion', arr3)

insertionAlgo(-2, 3)
print('arr3 at index: 3 after insertion', arr3)