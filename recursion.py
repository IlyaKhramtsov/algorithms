def fact(number: int) -> int:
    if number in (0, 1):
        return 1
    return number * fact(number - 1)


assert fact(5) == 120
assert fact(3) == 6
assert fact(1) == 1
