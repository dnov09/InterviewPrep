#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bestPros' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY pros
#  2. INTEGER k
#

def bestPros(pros, k):
    # Write your code here

    distance, rating = zip(*pros)
    max_distance = max(distance)

    calc_lst = []

    # pms_score = (max_distance - distance) * rating
    for i in range(len(distance)):
        pms = (max_distance - distance[i]) * rating[i]
        calc_lst.append(pms)

    rv = idxFinder(calc_lst, k)
    return rv


def idxFinder(calc_lst, k):
    max_idx = 0
    rv = []
    while len(rv) < k:
        # pass the idx of the max value to a variable
        # append it to our return value
        # change that max value to -1 so that we can find our next max
            # repeat till len(rv) < k this way it keeps performing the calculations
        max_idx = calc_lst.index(max(calc_lst))
        rv.append(max_idx)
        calc_lst[max_idx] = -1

    return rv



pros, k = [[5,4],[4,3],[6,5],[3,5]], 2

print(bestPros(pros, k))
'''
0th_idx = (6 - 5) * 4 = 4
1st_idx = (6 - 4) * 3 = 6 -> yes
2nd_idx = (6 - 6) * 5 = 0
3rd_idx = (6 - 3) * 5 = 15 -> yes

output = [3, 1] -> where 3 is 3rd_idx and 1 is 1st_idx

'''

