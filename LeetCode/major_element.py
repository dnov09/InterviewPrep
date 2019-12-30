def majorElement(nums):
    dct = {}
    for n in nums:
        if n not in dct:
            dct[n] = 1
        else:
            dct[n] += 1
    # Now find the key with the greatest occurence
    max_val = rv = 0
    for k,v in dct.items():
        if v > max_val:
            max_val = v
            rv = k
    return rv


print(majorElement([2, 2, 1, 1, 1, 2, 2]))
