def plusOne(digits):
    num = int(''.join(map(str, digits)))
    num += 1

    lst = [int(p) for p in str(num)]

    return lst

print(plusOne([9]))
