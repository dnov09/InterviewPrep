def countElements(nums):
    dct = {}
    for vals in nums:
        if vals not in dct:
            dct[vals] = 1
        else:
            dct[vals] += 1
            
    count = 0
    for vals in nums:
        if vals+1 in dct:
            count += 1
    return count


print(countElements([1, 3, 2, 3, 5, 0]))
    
