from collections import Counter


def checkio(text: str) -> str:
    text_list = [each.lower() for each in text.replace(' ', '') if each.isalpha()]
    counter = Counter(text_list)
    max_count = 0
    common_list = list()
    for each in counter.most_common():
        if each[1] >= max_count:
            common_list.append(each[0])
            max_count = each[1]
        else:
            break
    return sorted(common_list)[0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")