from itertools import count
from operator import truediv


def isValid(s):
    left_cir='('
    right_cir=')'
    left_square='['
    right_square=']'
    left_tilt='{'
    right_tilt='}'

    count_circle_left=0
    count_circle_right=0
    count_left_square =0
    count_right_square =0
    count_left_tilt = 0
    count_right_tilt = 0

    for i in s:
        if i==left_cir:
            count_circle_left+=1
        elif i==right_cir:
            count_circle_right+=1
        elif i==left_square:
            count_left_square+=1
        elif i==right_square:
            count_right_square+=1
        elif i==left_tilt:
            count_left_tilt+=1
        elif i==right_tilt:
            count_right_tilt+=1


    print(count_circle_left)
    print(count_circle_right)
    print(count_left_square)
    print(count_right_square)
    print(count_left_tilt)
    print(count_right_tilt)

    if count_circle_left == count_circle_right and count_left_square == count_right_square and count_left_tilt == count_right_tilt :
        return True
    else:
        return False

print(isValid("     {}   "))