def find_smallest(arr: list) -> int:
    """Finding the smallest element in an array."""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    """
    Sort the array.
    Time Complexity: O(n^2).
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


arr = [i for i in range(15, 0, -1)]
sorted_arr = [i for i in range(1, 16)]

assert selection_sort(arr) == sorted_arr
