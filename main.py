import math
from math import floor, sqrt, gcd

class real():
    def __init__(self, m=0, a=1, b=1, k=0):
        # if m == 0 just fraction
        # n^2 = mn + 1
        # = a/b * (n + k)
        self.m = m
        self.k = k
        self.a = a
        self.b = b

    def reduce(self):
        divider = gcd(self.a, self.b)
        self.a /= divider
        slef.b /= divider

    def __str__(self):
        maxLen = max(len(str(self.a)), len(str(self.b)))
        if self.m == 0:
            return str(self.a) + "\n" + "-" * maxLen + "\n" + str(self.b)
        return str(self.a) + "\n" + "-" * maxLen + " * ((" + str(self.m) + "+-√" + str(self.m**2 + 4) + ")/2 + " + str(self.k) + ")\n" + str(self.b)

    def __mul__(self, other):
        return new real()
        
    __rmul__ = __mul__
    __repr__ = __str__
        

def quasigreedy(beta):
    return greedyT(beta, 0.999999999)

def greedy(beta, x):
    k = floor(math.log(x, beta))
    x_i = [floor(x/beta**k)]
    r = x
    while k > 0:
        r = r - (beta**k) * x_i[-1]
        k -= 1
        x_i.append(floor(r/beta**k))
    return x_i

def T(beta, n, x):
    # [0, 1] -> [0, 1)
    if n == 0:
        return x
    if n == 1:
        return beta*x - floor(beta*x)
    return beta*T(beta, n-1, x) - floor(beta*T(beta, n-1, x))

def greedyT(beta, x):
    # [0, 1)
    Ti = []
    xi = []
    i = 0
    while i < 20:
        Ti.append(T(beta, i, x))
        i += 1
        xi.append(floor(beta*Ti[-1]))
        if Ti[-1] in Ti[:-1]:
            break
    print(Ti)
    return xi

#print(greedy(2, 25))
#print(greedyT(0.5*(1+sqrt(5)), 3/7))
#print(quasigreedy(10))
#print(quasigreedy(0.5*(1+sqrt(5))))
number = real(1, 25, 3)
print(number)
