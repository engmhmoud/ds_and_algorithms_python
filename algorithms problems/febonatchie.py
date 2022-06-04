# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")

# def solution(N):

#     N = bin(N)
#     print(N)

#     val = str(N)
#     val = val[2:]
#     print(val)
#     max_gab = 0
#     idx = -1
#     val_len = len(val)
#     is_prev_gap = False
#     counter = 0
#     for i in val:
#         idx += 1
#         if idx == 0:
#             continue
#         if idx == val_len-1 and i == 1 and is_prev_gap and counter > max_gab:
#             max_gab = counter
#             continue

#         if i == 0:
#             counter += 1
#             is_prev_gap = True

#         elif i == 1:
#             if is_prev_gap and counter > max_gab:
#                 max_gab = counter

#             is_prev_gap = False
#             counter = 0
#     return max_gab


# print(solution(1041))
cal = 0
cal2 = 0


def rec(val):
    global cal
    cal += 1

    if val <= 1:
        return 1
    else:
        return rec(val-1)+rec(val-2)


def feb_dynamic_programming(val):
    saved_answer = [None]*(val+1)
    saved_answer[0], saved_answer[1] = 1, 1
    # feb_res = [1, 1]

    # for el in range(val):
    #     feb_res.append(feb_res[el-1]+feb_res[el-2])

    # return feb_res[-1]
    def _feb(val):

        global cal2
        cal2 += 1

        if val <= 1:
            return 1
        if saved_answer[val]:
            return saved_answer[val]

        saved_answer[val] = _feb(val-1)+_feb(val-2)
        return saved_answer[val]

    return _feb(val)


res1 = rec(30)
res2 = feb_dynamic_programming(30)
print(f'res1{res1},cal1{cal}')
print(f'res2{res2},cal1{cal2}')
