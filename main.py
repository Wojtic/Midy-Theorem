import math
from math import floor, sqrt, gcd

class real():
    def __init__(self, a=1, b=1, m=0, c=0, k=1):
        # if m == 0 just fraction
        # n^2 = mn + 1
        # = a/b * (c*n + k)
        self.m = m
        self.k = k
        self.a = a
        self.b = b
        self.c = c

#        if (m == 0) and ((k != 1) or (c != 0)):
#            print(a, b, c, m, k)
#            raise Exception("When m=0 k must =1 and c must =0") 
#            return

        self.reduce()

    def reduce(self):
        divider = gcd(self.c, self.k)
        if divider > 0:
            self.c = int(self.c/divider)
            self.k = int(self.k/divider)
            self.a = int(self.a * divider)

        divider = gcd(self.a, self.b)
        if divider > 0:
            self.a = int(self.a/divider)
            self.b = int(self.b/divider)

    def __str__(self):
        maxLen = max(len(str(self.a)), len(str(self.b)))
        if self.m == 0:
            return str(self.a) + "\n" + "-" * maxLen + "\n" + str(self.b)
        return str(self.a) + "\n" + "-" * maxLen + " * (" + str(self.c) + " * (" + str(self.m) + "+√" + str(self.m**2 + 4) + ")/2 + " + str(self.k) + ")\n" + str(self.b)

    def __add__(self, other):
        if (self.m != other.m) and not ((self.m == 0) or (other.m == 0)):
            raise Exceaption("The two added numbers have different nonzero irrational parts") 
        b = int(self.b * other.b)
        c = int(self.a * other.b * self.c + other.a * self.b * other.c)
        k = int(self.a * other.b * self.k + other.a * self.b * other.k)
        return real(1, b, self.m, c, k)

    def __sub__(self, other):
        if (self.m != other.m) and not ((self.m == 0) or (other.m == 0)):
            raise Exceaption("The two subtracted numbers have different nonzero irrational parts") 
        b = int(self.b * other.b)
        c = int(self.a * other.b * self.c - other.a * self.b * other.c)
        k = int(self.a * other.b * self.k - other.a * self.b * other.k)
        if (c == 0) and (k == 0):
            return real(0, b, self.m, c, 1)
        return real(1, b, self.m, c, k)


    def __mul__(self, other):
        if self.m != other.m:
            if (self.m == 0) or (other.m == 0):
                m = self.m if self.m != 0 else other.m
                k = self.k if self.m != 0 else other.k
                c = self.c if self.m != 0 else other.c
                return real(int(self.a*other.a), int(self.b*other.b), m, c, k)
            raise Exceaption("The two multiplied numbers have different nonzero irrational parts") 
            return

        if self.m == 0:
            return real(int(self.a*other.a), int(self.b*other.b))

        a = int(self.a * other.a)
        b = int(self.b * other.b)
        c = int(self.c * other.c * self.m + self.c * other.k + other.c * self.k)
        k = int(self.c * other.c + self.k * other.k)

        return real(a, b, self.m, c, k)

    def __eq__(self, other):
        if (self.c == other.c == 0):
            if (self.a*self.k == other.a*other.k):
                return self.b == other.b
        return (self.a == other.a) and (self.b == other.b) and (self.c == other.c) and (self.m == other.m) and (self.k == other.k)

    def approx(self):
        return self.a/self.b * (self.c * ( self.m + sqrt(self.m**2 + 4) ) / 2 + self.k)

    def floor(self):
        return real(floor(self.approx()))
        
    __rmul__ = __mul__
    __repr__ = __str__
        
def expansionToReal(beta, expansion):
    # Z
    num = real(0) * beta
    mult = real(1)
    for i in range(len(expansion)):
        num = real(int(expansion[-i - 1])) * mult + num
        mult = mult * beta
    return num

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
        mult = beta*x
        return mult - mult.floor()
    mult = beta*T(beta, n-1, x)
    return mult - mult.floor()

def greedyT(beta, x):
    # [0, 1)
    Ti = []
    xi = []
    i = 0
    while True:
        if i > 100:
            return xi
        Ti.append(T(beta, i, x))
        i += 1
        mult = beta*Ti[-1]
        xi.append(int(mult.floor().approx()))
        for j in range(len(Ti) - 1):
            if Ti[j] == Ti[-1]:
                return xi[0:j] + ["("] + xi[j:-1] + [")"]

GR = real(1, 1, 1, 1, 0)
#print(greedyT(real(10), real(3,7)))
#print(greedyT(real(1, 1, 1, 1, 0), real(1,41)))
#print(greedyT(0.5*(1+sqrt(5)), 3/7))
#print(quasigreedy(10))
#print(quasigreedy(0.5*(1+sqrt(5))))
#a = real(3, 2, 1, 2, 4)
#b = real(3, 5, 0)
#a = real(2, 5, 1, 2, 1)
#b = real(4, 3, 1, 5, 2)
#multiple = a + b
#print(a)
#print(b)
#print(multiple)
#print(multiple.approx())
#print(multiple.floor())
print(expansionToReal(GR, [1, 0, 0, 1]))
#print(expansionToReal(GR, "101001"))
