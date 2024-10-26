from typing import List

def sum_top_two(arr: List[int]) -> int:
    # Sort the array in descending order and sum the first two elements
    if len(arr) < 2:
        raise ValueError("Array must contain at least two integers.")
    
    # Sort the array in descending order and pick the top two elements
    arr_sorted = sorted(arr, reverse=True)
    return arr_sorted[0] + arr_sorted[1]