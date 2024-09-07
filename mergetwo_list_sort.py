
def mergeTwoLists(list1, list2):
    l3 = []
    l3 = list1 + list2
    l3.sort()
    print(l3)
    return l3



print(mergeTwoLists([1,2,3] ,[1,0,2,5] ))