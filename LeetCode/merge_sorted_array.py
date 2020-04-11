'''
Given two sorted integer arrays nums1 and nums2, 
merge nums2 into nums1 as one sorted array.

Note:
    The number of elements initialized in nums1 and nums2 
    are m and n respectively.
    You may assume that nums1 has enough space 
    (size that is greater or equal to m + n) 
    to hold additional elements from nums2.

Example:

Input:

Output: [1,2,2,3,5,6]
'''
nums1, m = [1,2,3,0,0,0,], 3
nums2, n = [2,5,6], 3

def merge(nums1, m, nums2, n):
    i = len(nums1) - 1
    j = len(nums2) - 1

    while j > -1:
        if nums1[m - 1] < nums2[j]:
            nums1[i] = nums2[j]
            i -= 1
            j -= 1
        elif nums1[m - 1] > nums2[j]:
            temp = nums1[m - 1]
            nums1[m - 1] = nums2[j]
            nums1[m] = temp
            i -= 1
            j -= 1

    return nums1

print(merge(nums1, m, nums2, n))
    


