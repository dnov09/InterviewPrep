def romanToInt(s):
    # i, v, x, l, c, d, m = 1, 5, 10, 50, 100, 500, 1000
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # doing it in reverse because it makes more sense
    s = s[::-1]
    # we want to keep track of the prev and curr values
    prev = total = 0
    for i in range(len(s)):
        curr = roman_dict[s[i]]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    
    return total

'''
say `romanToInt("IV") -> 4`

going through the for loop
prev = 0
total = 0
***when i = 0:***
    roman[s[i]] = 5
    curr = 5
    runnin_total = 5
    prev = 5
						 
***when i = 1:***
    romans[s[i]] = 1
    curr = 1
    since curr < prev which is 5
    total = 5 -1 = 4
'''
