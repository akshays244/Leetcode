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
    for i in s:
        if i==left_cir:
            count_circle_left+=1
        elif i==right_cir:
            count_circle_right+=1


    print(count_circle_left)

    if count_circle_left == count_circle_right :
            return True
    else:
            return False

print(isValid("{}}"))