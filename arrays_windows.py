"""
Arrays: 
    - Largest window search for element repeats in array
    - Larget window search for elements in ascending order in array with consecutive difference d
"""

import array as arr
from array import *

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

# larget window search element
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

print("Largest window search for element")
arr_x = arr.array("i", [1, 2, 4, 4, 4, 8, 3, 3, 5, 6, 7, 4, 4, 4, 4, 4, 6, 8, 4, 4, 4, 4, 4])
print('arr_x: ', arr_x)
res_arr = largestWindowSearchElementAlgo(-5, arr_x)
print('largest window search element algo for arr_x: ', res_arr)

print('arr_x: ', arr_x)
res_arr = largestWindowSearchElementAlgo(4, arr_x)
print('largest window search element algo for arr_x: ', res_arr)


