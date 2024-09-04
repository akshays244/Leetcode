def romanToInt(s):
    def weight(a):
        return v1[a]
        
    v1 ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    l1=[]
    for i in s:
        for j in v1:
            l1.append(v1[i])
            break
    
    print(l1)
    
    vals = list(v1.values())
    print(vals)
    num =0
    for i in s:
        left= 0 
        right =left+1
        print("i is " +i)
        for j in l1:
            print("j is " + str(j))
            left=0
            print("left index is " + str(left))
            right=left+1
            print("right index is " + str(right ))
            if (right < len(l1)):
                print ("value of left index is ", l1[left])
                print ("value of right index is ", l1[right])
                if l1[left]<l1[right]:
                    num = num + l1[right] -l1[left]
                    print("first if num value is " , num)
                if (l1[left]>l1[right]):
                    num = num +l1[left]
                    print("2nd if num value is " , num)
                break
        left+=1
    return num
            

print(romanToInt('MCMXCIV'))
