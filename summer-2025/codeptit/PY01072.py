def generate(a, k):
    n = len(a)
    c = list(range(k))
    while True:
        print(' '.join(map(str, [a[i] for i in c])))
        i = k - 1
        while i >= 0 and c[i] == n - k + i:
            i -= 1
        if i < 0:
            break
        c[i] += 1
        for j in range(i + 1, k):
            c[j] = c[j - 1] + 1

def backtrack(a, k, start, comb):
    if len(comb) == k:
        print(' '.join(map(str, comb)))
    n = len(a)
    for i in range(start, n):
        if n - i < k - len(comb): break;
        comb.append(a[i])
        backtrack(a, k , i + 1, comb)
        comb.pop()


n, k = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(set(a))
# generate(a, k)
backtrack(a, k, 0, [])


