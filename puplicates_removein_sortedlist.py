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