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

    result = 0
    roman_list = [x for x in s]
    for k, v in roman_dict.items():
        for i in range(len(roman_list)):
            if roman_list[i] == k:
                result += v
    # return result

    # print(result)
    print(list(enumerate(roman_dict)))


romanToInt("XXVII")
