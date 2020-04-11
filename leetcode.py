# def luckynumbers(matrix):
#     min_lst = []
#     for row in matrix:
#         min_lst.append(min(row))
#     return [max(min_lst)]


# matrix = [
#     [36376, 85652, 21002, 4510],
#     [68246, 64237, 42962, 9974],
#     [32768, 97721, 47338, 5841],
#     [55103, 18179, 79062, 46542]]


# print(luckynumbers(matrix))


def luckyNumbers(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    small = 9999999
    large = 0
    lucky = []
    col = 0
    row = -1
    for i in matrix:
        row = row+1
        for j in i:
            checkmax(j, matrix, col)
            if checkmin(j, matrix, row) and checkmax(j, matrix, col):
                lucky.append(j)
            col = col+1

        col = 0

    return lucky


def checkmin(num, matrix, row):
    small = 9999999
    for i in matrix[row]:
        small = min(i, small)

    if small == num:
        return True
    else:
        return False


def checkmax(num, matrix, col):
    large = -1
    for i in matrix:
        p = i[col]
        # print(p)
        large = max(p, large)

    if large == num:
        return True
    else:
        return False


matrix = [[36376, 85652, 21002, 4510], [68246, 64237, 42962, 9974],
          [32768, 97721, 47338, 5841], [55103, 18179, 79062, 46542]]

print(luckyNumbers(matrix))
