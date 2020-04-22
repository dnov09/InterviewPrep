'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

def groupAnagrams(strs):
    dct = {}
    for vals in strs:
        s = ''.join(sorted(vals))
        if s not in dct:
            dct[s] = [vals]
        else:
            dct[s].append(vals)
    return [v for v in dct.values()]


input_lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input_lst))
