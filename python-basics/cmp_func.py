from math import *
from functools import cmp_to_key

# -1, 1, 0
# if fi < se:
#     return -1
# elif fi > se:
#     return 1
# return 0

def tong_cs(n):
    res = 0
    while n != 0:
        res += n % 10
        n /= 10
    return res

def cmp(a, b):
    tong1 = tong_cs(a)
    tong2 = tong_cs(b)
    if tong1 != tong2:
        return tong1 - tong2
    return a - b

if __name__ == '__main__':
    # a = [[1, 2], [3,2], [1,1], [4,1], [3,1]]
    # a.sort(key = lambda x : (x[0], -x[1]))
    # print(a)

    ls = [10, 2, 3, 5, 1, 4, 6, 0, 3]
    ls.sort(key = cmp_to_key(cmp))
    print(ls)

