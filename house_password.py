def checkio(data: str) -> bool:
    if not 10 <= len(data) <= 64:
        return False
    upper = False
    lower = False
    number = False
    for each in data:
        if each.isupper():
            upper = True
        elif each.islower():
            lower = True
        elif each.isnumeric():
            number = True
    return upper and lower and number

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
