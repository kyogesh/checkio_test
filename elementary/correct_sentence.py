def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    if text[0].isupper() and text[-1] == '.':
        return text
    elif text[0].isupper() and text[-1] != '.':
        return text + '.'
    elif not text[0].isupper() and text[-1] == '.':
        return text[0].upper() + text[1:]
    elif not text[0].isupper() and text[-1] != '.':
        return text[0].upper() + text[1:] + '.'


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
