import math
import os
import random
import re
import sys
# Complete the 'categorySuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY categories
#  2. STRING_ARRAY projects
#  3. INTEGER k
#

def categorySuggestions(categories, projects, k):
    # Write your code here
    
    # categorySuggestions() -> [[Suggestion1],[Suggestion2]
    pass


def sortRelevance(categories):
    split_lst = []
    for jobs in categories:
        # turn our string input into list for easier sorting
        delim = jobs.split(",")
        split_lst.append(delim)

    # sorting by the relevance index
    split_lst.sort(key = lambda split_lst: split_lst[2], reverse=True)
    return toDict(split_lst)

def toDict(lst):
    dct = {}
    for recs in lst:
        for i in recs:
            if i not in dct:
                dct[i] = recs[-1]
    
    for k, v in dct.items():
        if k.isnumeric() == True:
            dct.pop(k)
    
    return dct
    

categories = [
    "House Painting,Interior Painting,0.9",
    "Handyman,Massage Therapy,0.1",
    "Handyman,House Painting,0.5",
    "House Painting,House Cleaning,0.6",
    "Furniture Assembly,Handyman,0.8",
    "Furniture Assembly,Massage Therapy,0.1",
    "Plumbing Drain Repair,Junk Removal,0.3"
]

projects, k = ["House Painting", "Handyman"], 3

# categorySuggestions(categories, projects, k) -> [
# ["House Painting", "Interior Painting", "House cleaning"],
#  ["Handyman", "House Painting", "Interior Painting"]
# ]
'''
new_dct = {} 
    ...: for recs in sorted_cat: 
    ...:     for i in recs: 
    ...:         if i not in new_dct: 
    ...:             new_dct[i] = recs[-1] 
    ...:         elif i in new_dct: 
    ...:             new_dct[i] = recs[-1] 
'''
print(sortRelevance(categories))
