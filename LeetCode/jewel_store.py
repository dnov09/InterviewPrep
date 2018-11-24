'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:

    S and J will consist of letters and have length at most 50.
    The characters in J are distinct.
'''

#%%
# store char_count in 2 different hashmaps
# check how many times the character occurs.
def jewel_store(J, s):
    jewel = dict()
    store = dict()
    count = 0

    for i in range(len(J)): # O(N)
        if J[i] in jewel:
            jewel[J[i]] += 1
        else:
            jewel[J[i]] = 1
    
    for j in range(len(s)): # O(N)
        if s[j] in store:
            store[s[j]] += 1
        else:
            store[s[j]] = 1

    # if the jewel_chars in store_chars:
        # add up the values of the existing chars in stores dict
    # return int
    for key in store: # O(N)
        if key in jewel:
            count += store[key]
    return count

jewel_store("aazzAA","bAaZAZ")
