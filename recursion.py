def fact(number: int) -> int:
    if number in (0, 1):
        return 1
    return number * fact(number - 1)


assert fact(5) == 120
assert fact(3) == 6
assert fact(1) == 1


def new_sum(array: list) -> int:
    if not array:
        return 0
    return array[0] + new_sum(array[1:])


assert new_sum([2, 4, 6]) == 12
assert new_sum([]) == 0
assert new_sum([1]) == 1


def counter(array: list) -> int:
    if not array:
        return 0
    return 1 + counter(array[1:])


assert counter([1, 2, 10, 25]) == 4
assert counter([1]) == 1
assert counter([]) == 0


def max_number(array: list) -> int:
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = max_number(array[1:])
    return array[0] if array[0] > sub_max else sub_max


assert max_number([1, 5, 25, 116, 98, 52]) == 116
assert max_number([29, 15]) == 29
