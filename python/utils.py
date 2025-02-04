import math
from functools import lru_cache
from math import floor, sqrt, gcd
from real import real


def expansionToReal(beta, expansion):
    # Z
    num = real(0) * beta
    mult = real(1)
    for i in range(len(expansion)):
        num = real(int(expansion[-i - 1])) * mult + num
        mult = mult * beta
    return num

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
