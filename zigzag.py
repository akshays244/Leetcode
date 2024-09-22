def convert(s, numRows):
    str=[]
    b=0
    while b<numRows:
        for i in s:
            p=b
            if (p==b):
                print(i)
                str.append(i)
            b+=1

    return str


print(convert("paypalishiring",3))