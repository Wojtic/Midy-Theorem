import matplotlib.pyplot as plt
import numpy as np
from functools import lru_cache
from math import gcd
from utils import *

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


def PisanoPeriod(m, q, MAX_ITERATIONS=1000000000):
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


def plotPisanoPeriods():
    x = []
    periods1 = []
    periods2 = []
    periods3 = []
    periods4 = []
    for j in range(1, 2000):
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
