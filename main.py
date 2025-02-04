import math
from functools import lru_cache
from math import floor, sqrt, gcd
from real import real
from utils import *


def checkMidy(expansion, beta):
    if (expansion[0] != "(") or (expansion[-1] != ")"):
        return False
    n = len(expansion) - 2
    if n % 2 != 0:
        return False

    added = expansionToReal(beta, expansion[1:int(
        n/2) + 1]) + expansionToReal(beta, expansion[int(n/2) + 1:-1])
    expanded = greedy(beta, added)
    if len(expanded) != n / 2:
        return False
    for i in range(len(expanded)):
        # Check quasigreedy !!TODO!!
        if (i % 2 == 0) and (expanded[i] != beta.m):
            return False
        if (i % 2 != 0) and (expanded[i] != 0):
            return False
    return True


def checkMidyProperty(beta, n, maximum=0):
    if maximum == 0:
        maximum = n
    for a in range(1, maximum):
        if gcd(n, a) > 1:
            continue
        expansion = greedyT(beta, real(a, n))
        if checkMidy(expansion, beta):
            return [True, a, expansion]
    return False


"""
GR = real(1, 1, 1, 1, 0)

beta = real(1, 1, 3, 1, 0)

print(greedy(beta, real(1, 5)))
print(greedy(beta, expansionToReal(beta, "20130") + expansionToReal(beta, "220110")))
"""
"""
for i in range(1, 100):
    print(i, greedy(real(1, 1, i, 1, 0), real(i) + real(1)))
"""
"""beta = real(1, 1, 3, 1, 0)
print(greedy(beta, expansionToReal(beta, "201302") + expansionToReal(beta, "103022")))
"""
"""
bases = []
if __name__ == "__main__":
    a = real(1, 1, 2, 1, 0)
    print(greedy(a, real(1, 4)))
    for m in range(1, 2):
        beta = real(1, 1, m, 1, 0)
        print(m)
        base = []
        for i in range(1, 100):
            result = checkMidyProperty(beta, i, 2)
            if (result):
                base.append(i)
        bases.append(base)
    print(bases[0])
"""
print(greedy(real(1, 1, 1, 1, 0), real(1, 50)))
"""
    for i in range(1, 100):
        print(i, checkMidyProperty(GR, i))
    """
