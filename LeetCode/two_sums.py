import timeit
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
#%%
nums, target = [2, 7, 11, 15, 45, 56, 12, 13, 14, 67, 78, 34, 35],  78

# brtue force solution (O(n^2)) -> too slow
def two_sums(nums, target):
    lst = list()
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[j] == target - nums[i] and i != j:
                lst.append(i)
                lst.append(j)
        if len(lst) == 2:
            break
    return lst


print(two_sums(nums, target))

#%%
# Faster more optimized solution using dictionary
def two_sums_faster(nums, target):
    keep = dict()
    for i in range(len(nums)):# O(n) runtime
        if nums[i] in keep:  
            return [keep[nums[i]], i]  # O(1)
        else:
            keep[target - nums[i]] = i  # O(1)

# two_sums_faster(nums, target)
