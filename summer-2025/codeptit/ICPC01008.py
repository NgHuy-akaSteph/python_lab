# SUM TRIPLE ZERO: Bộ ba số có tổng bằng 0

# C1: Brute force O(N^3)
def solve_brute_force(a, n):
    res = 0
    for i in range(0, n-2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if a[i] + a[j] + a[k] == 0:
                    res += 1
    return res

# C2: Two pointer O(N^2)
def solve_two_pointer(a, n):
    a.sort() # O(NlogN)
    res = 0
    for i in range(n - 2):
        l, r = i + 1, n - 1
        while l < r:
            s = a[i] + a[l] + a[r]
            if s == 0:
                res += 1
                l += 1
                # r -= 1: không giảm vì còn những giá trị trùng nhau nằm liền kề
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # print(solve_brute_force(a, n))
    # print(solve_two_pointer(a, n))