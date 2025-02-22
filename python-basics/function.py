import math
# Viet ham tinh tong va dem uoc cua 1 so nguyen: Duyet toi can bac 2 cua n
def dem_uoc(n):
    cnt = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            cnt += 1 if i * i == n else 2
    return cnt

# Viet ham kiem tra so nguyen to
def is_prime(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 2

#
prime = [1] * 1000001
def sieve():
    prime[0] = prime[1] = 0
    for i in range(2, 1001):
        if prime[i]:
            for j in range(i * i, 1000001, i):
                prime[j] = 0



if __name__ == '__main__':
    sieve()
    n = int(input('Nhap n: '))
    if prime[n]:
        print('La so nguyen to')