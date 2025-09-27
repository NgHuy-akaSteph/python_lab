#PY01075: TRÒ CHƠI TRÊN ĐƯỜNG THẲNG
"""
* Giải thích đề:
- Với các bước nhảy a1, a2.. ak thì có thể đi đến được tất cả các số chia hết cho gcd(a1, a2... ak)
- Muốn đi đến mọi điểm nguyên thì gcd(a1, a2,...ak) = 1
=> Bài toán: Tìm các tập ai có gcd bằng 1 và chọn tập có tổng ci là nhỏ nhất

* Ý tưởng:
- Dạng bài toán tối ưu trên gcd - Dùng quy hoạch động
- Định nghĩa:
    + dp[g] = chi phí nhỏ nhất để đạt được gcd = g từ một tập thẻ đã chọn
    + dp[0] = 0 (chưa chọn gì_
    + Với mỗi thẻ (a, c) ta có thể cập nhật lại dp[g] nếu tìm được chi phí mới nhỏ hơn
    hoặc tạo mới nếu dp[g] chưa tồn tại.
    + Sau khi xử lí hết, kết quả cần tìm là dp[1], nếu không có trả về -1

* VD:
n = 3
a = [3, 4, 5]
c = [1, 2, 3]

Bắt đầu: dp = {0:0}
- Xét thẻ (3, 1):
    gcd(0, 3) = 3 => dp[3] = 1 => dp = {0:0, 3:1}
- Xét thẻ (4, 2):
    gcd(0, 4) = 4 => dp[4] = 2 => dp = {0:0, 3:1, 4:2}
    gcd(3, 4) = 1 => dp[1] = 1 + 2 = 3 => dp = {0:0, 3:1, 4:2, 1:3}
- Xét thẻ (5, 3):
    gcd(0, 5) = 5 => dp[5] = 3 => dp = {0:0, 3:1, 4:2, 1:3, 5:3}
    gcd(3, 5) = 1 => dp[1] = 1 + 3 = 4 (không update vì hiện tại dp[1] = 3)
    gcd(4, 5) = 1 => dp[1] = 2 + 3 = 5 (không update vì hiện tại dp[1] = 3)
    gcd(1, 5) = 1 => dp[1] = 3 + 3 = 6 (không update vì hiện tại dp[1] = 3)
"""
from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    dp = {0: 0}  # dp[g] = chi phí tối thiểu để đạt gcd = g

    for ai, ci in zip(a, c):
        # duyệt snapshot các trạng thái cũ
        # print("Kế tiếp: ")
        for g, cost in list(dp.items()):
            new_g = gcd(g, ai)
            new_cost = cost + ci
            # print(f"ai:{ai} ci:{ci} g:{new_g} cost:{new_cost}")
            if new_g not in dp or new_cost < dp[new_g]:
                dp[new_g] = new_cost

    print(dp[1] if 1 in dp else -1)
