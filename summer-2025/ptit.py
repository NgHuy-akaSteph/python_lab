from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    dp = {0: 0}  # dp[g] = chi phí tối thiểu để đạt gcd = g

    for ai, ci in zip(a, c):
        # duyệt snapshot các trạng thái cũ
        for g, cost in list(dp.items()):
            new_g = gcd(g, ai)
            new_cost = cost + ci
            if new_g not in dp or new_cost < dp[new_g]:
                dp[new_g] = new_cost

    print(dp[1] if 1 in dp else -1)