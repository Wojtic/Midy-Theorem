import matplotlib.pyplot as plt
import numpy as np
from functools import lru_cache
from math import gcd

# Naming convention:
# n - n-th member of sequence
# m - m-fib numbers
# q - modulo
# If they appear then it must be in this order


@lru_cache(maxsize=None)
def mFib(n, m=1):
    if n <= 1:
        return n
    return m * mFib(n - 1, m) + mFib(n - 2, m)


@lru_cache(maxsize=None)
def mFibModQ(n, m, q):
    if n <= 1:
        return n
    return (m * mFib(n - 1, m) + mFib(n - 2, m)) % q


def coprime(a, b):
    return not (gcd(a, b) > 1)


def checkDivProperty(m, N=1000):
    # Sm | Sr iff m | r
    for i in range(1, N):
        for j in range(i + 1, N):
            if ((j % i == 0) and (mFib(j, m) % mFib(i, m) == 0)) or ((j % i != 0) and (mFib(j, m) % mFib(i, m) != 0)):
                continue
            print("Property doesn't hold for m = " + str(m) +
                  ", i = " + str(i) + ", j = " + str(j))
    # print("Property holds for m = " + str(m) + ", up to " + str(N))


"""
m = 1
sols = []
for q in range(3, 100):
    for i in range(1, q*q + q):
        if (seqMod(i - 1, m, q) == seqMod(i + 1, m, q) == q - 1) and (seqMod(i, m, q) == 0):
            sols.append((q, i))
            break
print(sols)
"""

MAX_ITERATIONS = 1000000000


def PisanoPeriod(m, q):
    # Period of the sequence f_m mod q until it repeats
    if q <= 0:
        return 0
    if q == 1:
        return [0]
    sequence = []
    i = 1
    while i < MAX_ITERATIONS:
        sequence.append(mFibModQ(i, m, q))
        if i > 3:
            if (sequence[0] == sequence[-2]) and (sequence[1] == sequence[-1]):
                return sequence[:-2]
        i += 1


def pi(m, q):
    # Length of Pisano Period
    return len(PisanoPeriod(m, q))


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return (n == d)
        d = d + 2
    return True


def plotPisanoPeriods():
    x = []
    periods1 = []
    periods2 = []
    periods3 = []
    periods4 = []
    for j in range(1, 100):
        if not isPrime(j):
            continue
        print(j)
        x.append(j)
        periods1.append(pi(1, j))
        periods2.append(pi(2, j))
        periods3.append(pi(3, j))
        periods4.append(pi(4, j))

        if j % 1000 == 0:
            print(j)

    plt.scatter(x, periods1, s=2, color="#000000")
    plt.scatter(x, periods2, s=2, color="#FF0000")
    plt.scatter(x, periods3, s=2, color="#00FF00")
    plt.scatter(x, periods4, s=2, color="#0000FF")
    plt.show()


plotPisanoPeriods()

# for j in range(1, 10):
#    print(seq(j, 2))
# checkDivProperty(j)
