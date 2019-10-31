VOWELS = "aeiouy"

def translate(phrase):
    new_phrase = []
    counter = 0
    for letter in phrase:
        if counter > 0:
            counter -= 1
            continue
        if letter == ' ':
            new_phrase.append(letter)
            counter = 0
        elif letter not in VOWELS:
            new_phrase.append(letter)
            counter = 1
        elif letter in VOWELS:
            new_phrase.append(letter)
            counter = 2
    return ''.join(new_phrase)

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

