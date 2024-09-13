def lengthOfLongestSubstring(s):
    a=[]
    ai=[]
    i=0
    j=1
    if s=="" :
        return ""
    else:
        a.append(s[0])
    while j <len(s):
        if s[i]!=s[j] and s[i] not in a:
            a.append(s[i])
            ai.append(i)
        elif s[i] == s[j] and s[i] not in a:
            j+=1
            i+=1

        i+=1
        j+=1

    print(ai)
    print(a)
    if s=="" :
        return ""
    else:
        return len(a)

print(lengthOfLongestSubstring("abcabcaa"))