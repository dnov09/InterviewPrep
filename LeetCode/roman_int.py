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


