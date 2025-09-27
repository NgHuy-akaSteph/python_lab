# DÃY SỐ PHÙ HỢP - PY02006
def check(a, b):
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True

for _ in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("YES" if check(a, b) else "NO")