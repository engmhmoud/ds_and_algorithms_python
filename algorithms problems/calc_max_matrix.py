

matrix = [[5, 1, 2],
          [6, 1, 8],
          [1, 4, 9]]

# possible solution ;
# d=5{1{2{8{9}},1{}},6{1{8},1{}}}

# to get max path possible


def cal_path_rec(matrix):
    n = len(matrix[0])

    def calc(r, c):
        if r > n-1 or c > n-1:
            return 0
        if r == n-1 and c == n-1:
            return matrix[r][c]  # base

        rigth = calc(r, c+1)
        down = calc(r+1, c)

        return matrix[r][c]+max(rigth, down)

    return calc(0, 0)


def cal_path_memoization(matrix):
    n = len(matrix[0])
    res_saved = []

    def calc(r, c):
        if r > n-1 or c > n-1:
            return 0
        if r == n-1 and c == n-1:
            return matrix[r][c]  # base

        rigth = calc(r, c+1)
        down = calc(r+1, c)

        return matrix[r][c]+max(rigth, down)

    return calc(0, 0)


res_Rec = cal_path_rec(matrix)
print(res_Rec)
res_Mem = cal_path_memoization(matrix)
print(res_Mem)
