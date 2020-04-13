'''
Given an integer array nums, 
find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_ending_here < 0)
            max_ending_here = 0
  (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
return max_so_far

'''

def maxSubArray(nums):
    max_sum = max(nums)
    curr_sum = 0
    for vals in nums:
        curr_sum += vals
        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    return max_sum
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
