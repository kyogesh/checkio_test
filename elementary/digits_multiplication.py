from functools import reduce


def checkio(number: int) -> int:
    return reduce(lambda x, y: x*y, [int(each) for each in str(number) if each != '0'])


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print(
        "Coding complete? Click 'Check' to review your tests and earn cool rewards!")

