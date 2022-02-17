def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


assert quick_sort([6, 9, 5, 4, 3, 1, 2]) == [1, 2, 3, 4, 5, 6, 9]
assert quick_sort([]) == []
assert quick_sort([1]) == [1]
