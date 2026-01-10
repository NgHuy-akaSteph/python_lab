import math


def sum2(a, b):
    return a + b


def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return False


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(sum2(a, b))
    print(math.pi)
