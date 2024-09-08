import math
from operator import index
'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

def searchInsert(nums, target):
    first =nums[0]
    #print("first element" ,first)
    last_index=len(nums)-1
    #print("last index is " ,last_index)
    last=nums[-1]
    #print("last element is " ,last)
    mid_index =  int(len(nums)/2)
    #print("mid index is  " ,mid_index)
    mid_index_value = nums[mid_index]
    #print("mid index value is ", mid_index_value)
    first_index_value =0
    trace=[]
    while target <= nums[-1] and len(trace)<=len(nums)/2:
        mid_index_value = nums[mid_index]
        trace.append(mid_index)
        if target == mid_index_value :
            return mid_index
        elif target < mid_index_value :
            mid_index=mid_index-1
        elif target > mid_index_value :
            mid_index=mid_index+1
        else:
            return -1

    if target not in nums:
        if target > nums[-1] :
            return len(nums)
        elif target < mid_index_value :
             return trace[-1]
        elif target > mid_index_value :
            return trace[-1] + 1
        else:
            return trace[-1]

print("lets see your return value " ,searchInsert([1,3,5,6],7)) #out 2