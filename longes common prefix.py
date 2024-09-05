from sys import prefix


def longestCommonPrefix(strs):
    a=[]
    b=[]
    prefix = strs[0]

    for strings in strs[1:]:
        i = 0
        while i < len(prefix) and i <len(strings) and prefix[i] == strings[i]:
            i += 1
        prefix= prefix[:i]

        if not prefix:
            return ""

    return prefix



print(longestCommonPrefix(['flower','flying','fleet']))