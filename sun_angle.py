from datetime import datetime


def sun_angle(time):
    x = 90/(60*60)
    delta = datetime.strptime(time, '%H:%M') - datetime.strptime('06:00', '%H:%M')
    angle = (delta.seconds/6)*x
    if angle > 180:
        return "I don't see the sun!"
    return angle

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
