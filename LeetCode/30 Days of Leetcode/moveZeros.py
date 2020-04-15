'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

def moveZeros(nums):
    for vals in nums:
        if vals == 0:
            print("Zero Found")
        else:
            print(vals)


nums = [0, 1, 0, 3, 12]

print(moveZeros(nums))
