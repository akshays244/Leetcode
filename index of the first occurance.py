'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.'''



def strStr(haystack, needle):
    p=''
    index_track=[]
    return_value_index=0
    stringthere = False
    for index,char in enumerate(haystack):
        index_track.append(index)
        p = p + char
        if len(p) > len(needle):
            p=p[1:]
            index_track=index_track[1:]
        #print(p)
        #print(index_track)
        if p==needle:
            stringthere = True
         #   print(index_track)
            #index_track.append(index)
          #  print(index_track)
            return_value_index=index_track[0]
            break
        #index_track=index_track[1:]
    if stringthere==True:
        return index_track[0]
    else:
        return -1

print(strStr("sadbutsad", "sad"))