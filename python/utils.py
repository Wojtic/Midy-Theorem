import math
from functools import lru_cache
from math import floor, sqrt, gcd
from real import real


def coprime(a, b):
    return not (gcd(a, b) > 1)


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


def expansionToReal(beta, expansion):
    # Z
    num = real(0) * beta
    mult = real(1)
    for i in range(len(expansion)):
        num = real(int(expansion[-i - 1])) * mult + num
        mult = mult * beta
    return num


def addExpansions(m, expansion1, expansion2):
    # Z -> R
    digits = max(len(expansion1), len(expansion2))
    total = [[0] for _ in range(digits)]
    extraDigits = 0
    for i in range(len(expansion1)):
        total[-i - 1].append(expansion1[-i-1])
    for i in range(len(expansion2)):
        total[-i - 1].append(expansion2[-i-1])
    while True:
        lastTotal = total.copy()
        while True:
            # 1. Sum according to the rules
            sumTotal = total.copy()
            for i in range(len(total)):
                total[i] = [sum(total[i])]
            for i in range(len(total)):
                if total[i][0] > m:
                    if i == 0:
                        total = [[0]] + total
                        i += 1
                        digits += 1
                    total[i - 1].append(1)
                    total[i] = [total[i][0] - m - 1]
                    if i > digits - 3 + extraDigits:
                        for _ in range(i - (digits - 3 + extraDigits)):
                            extraDigits += 1
                            total.append([])
                    total[i + 1].append(m - 1)
                    total[i + 2].append(1)
            if sumTotal == total:
                break

        while True:
            # 2. Get rid of illegal expansions
            changed = False
            for i in range(len(total) - 1):
                if (total[i][0] == m) and (total[i + 1][0] != 0):
                    changed = True
                    total[i - 1][0] += 1
                    total[i][0] = 0
                    total[i + 1][0] -= 1
            if not changed:
                break

        if lastTotal == total:
            break

    for i in range(len(total)):
        total[i] = total[i][0]

    for i in range(extraDigits):
        if total[digits + i] != 0:
            return total[0:digits] + ["."] + total[digits:]

    return total[0:digits]

# def quasigreedy(beta):
#    return greedyT(beta, 0.999999999)


@lru_cache(maxsize=None)
def greedy(beta, x):
    k = floor(math.log(x.approx(), beta.approx()))
    exponent = beta**k
    x_i = [real(floor(x.approx()/exponent.approx()))]
    r = x
    while k > 0:
        r -= (beta**k) * x_i[-1]
        k -= 1
        exponent = beta**k
        x_i.append(real(floor(r.approx()/exponent.approx())))
    r -= x_i[-1]
    x_i = list(map(lambda num: num.int(), x_i))
    if r != real(0):
        x_i.append(".")
        x_i += greedyT(beta, r)
    return x_i


@lru_cache(maxsize=None)
def T(beta, n, x):
    # [0, 1] -> [0, 1)
    if n == 0:
        return x
    if n == 1:
        mult = beta*x
        return mult - mult.floor()
    mult = beta*T(beta, n-1, x)
    return mult - mult.floor()


@lru_cache(maxsize=None)
def greedyT(beta, x):
    # [0, 1)
    Ti = []
    xi = []
    i = 0
    while True:
        if i > 1000:
            return xi
        Ti.append(T(beta, i, x))
        i += 1
        mult = beta*Ti[-1]
        xi.append(int(mult.floor().approx()))
        for j in range(len(Ti) - 1):
            if Ti[j] == Ti[-1]:
                return xi[0:j] + ["("] + xi[j:-1] + [")"]
