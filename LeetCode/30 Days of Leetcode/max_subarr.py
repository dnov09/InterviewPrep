'''
Given an integer array nums, 
find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

'''

def maxSubArray(nums):
    max_sum = max(nums)
    curr_sum = 0
    for vals in nums:
        curr_sum += vals
        max_sum = max(max_sum, curr_sum)
        print("Current Sum: {}\nMax Sum: {}".format(curr_sum, max_sum))

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
