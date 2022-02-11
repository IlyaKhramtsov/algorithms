def binary_search(arr: list, item: int):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return guess
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


new_list = [i for i in range(1, 101)]

assert binary_search(new_list, 64) == 64
assert binary_search(new_list, -5) is None
assert binary_search(new_list, 140) is None
