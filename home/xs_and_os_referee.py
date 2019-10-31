from typing import List


def checkio(game_result: List[str]) -> str:
    result = game_result
    for i in range(3):
        a = list()
        for j in range(3):
            a.append(game_result[j][i])
        result.append(''.join(a))
    a = list()
    b = list()
    for i in range(3):
        a.append(game_result[i][i])
        b.append(game_result[i][2-i])
    result.append(''.join(a))
    result.append(''.join(b))
    winner = [each[0] for each in result if set(each) == set(each[0]) and each[0] != '.']
    print(winner)
    return winner[0] if winner else 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    assert checkio(["OOO","XX.",".XX"]) == 'O'
    assert checkio(["...","XXX","OO."]) == 'X'
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")