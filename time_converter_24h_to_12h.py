from datetime import datetime


def time_converter(time):
    time12 = datetime.strptime(time, '%H:%M').strftime('%-I:%M %p')
    if time12.endswith('AM'):
        time12 = time12.split(' ')[0] + ' a.m.'
    elif time12.endswith('PM'):
        time12 = time12.split(' ')[0] + ' p.m.'
    return time12


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
