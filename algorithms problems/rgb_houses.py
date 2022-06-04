# problem 6680 topcode
# min cost of houses colors
# solution calulate min cost of


# for n = 3
# for RGB cost
from json.encoder import INFINITY


house_cost_color = [
    # [ R , G , B] cost
    [1, 100, 100],
    [100, 1, 100],
    [100, 100, 100],
    [1, 100, 1],
    [1, 1, 100],
    [1, 100, 1],
    [100, 1, 1],
    [100, 1, 1],
    [100, 100, 1],
    [100, 100, 100],
    [1, 100, 1],
    [1, 100, 1],
    [1, 100, 1],
    [1, 1, 1],
    [1, 100, 1],
    [1, 100, 1],
    [100, 1, 1],
    [1, 100, 100],
    [1, 100, 100],
    [1, 100, 100],
    [1, 100, 100],
]
# R == 0
# G == 1
# B == 2
# 3 Wrong

INFINITY = 10000000000000


def cal_min_cost(n, house_cost_color):

    def calc_cost(last, index):
        ret = INFINITY
        if index == n:
            return 0
        if last != 0:
            ret = min(ret, house_cost_color[index][0] + calc_cost(0, index+1))
        if last != 1:
            ret = min(ret, house_cost_color[index][1] + calc_cost(1, index+1))
        if last != 2:
            ret = min(ret, house_cost_color[index][2] + calc_cost(2, index+1))

        return ret

    return calc_cost(3, 0)


def cal_min_cost_memorize(n, house_cost_color):

    saved_answer = [[None] * 4] * n

    def calc_cost(last, index):

        if index == n:
            return 0
        ret = saved_answer[index][last]
        if ret:
            return ret

        ret = INFINITY

        if last != 0:
            ret = min(ret, house_cost_color[index][0] + calc_cost(0, index+1))
        if last != 1:
            ret = min(ret, house_cost_color[index][1] + calc_cost(1, index+1))
        if last != 2:
            ret = min(ret, house_cost_color[index][2] + calc_cost(2, index+1))
        saved_answer[index][last] = ret
        return ret

    return calc_cost(3, 0)


res = cal_min_cost_memorize(20, house_cost_color)
print(res)
