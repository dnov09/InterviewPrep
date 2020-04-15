'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

def moveZeros(nums):
    keep_idx = nums[0]
    for i in range(0, len(nums)):
        if nums[i] == 0:
            keep_idx = nums[i]
            del nums[i]
            nums.append(keep_idx)
    return nums
            

# My thinking would be to use a two-pointer approach somehow
def moveZeros_inplace(nums):
    pass


nums = [0, 1, 0, 3, 12]

print(moveZeros(nums))
print(moveZeros_inplace(nums))
