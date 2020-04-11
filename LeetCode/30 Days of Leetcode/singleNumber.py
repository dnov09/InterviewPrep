'''
Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.

Input: [2,2,1]
Output: 1

Input: [4,1,2,1,2]
Output: 4
'''


def singleNumber(nums):
    keep = {}
    for vals in nums:
        if vals not in keep:
            keep[vals] = 1
        else:
            keep[vals]+= 1
    
    for k,v in keep.items():
        if v == 1:
            return k

input = [4,1,2,1,2]

print(singleNumber(input))