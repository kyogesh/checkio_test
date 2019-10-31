def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    if not line:
        return 0
    max_len = 0
    char = ''
    counter = 0
    for each in line:
        if char == each:
            counter += 1
        elif char != each:
            char = each
            counter = 1
        if counter > max_len:
            max_len = counter
    print(max_len)
    return max_len


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
