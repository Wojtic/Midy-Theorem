from sequences import *
from utils import addExpansions


def checkDivProperty(m, N=1000):
    # Fm | Fr iff m | r
    for i in range(1, N):
        for j in range(i + 1, N):
            if ((j % i == 0) and (mFib(j, m) % mFib(i, m) == 0)) or ((j % i != 0) and (mFib(j, m) % mFib(i, m) != 0)):
                continue
            print("Property doesn't hold for m = " + str(m) +
                  ", i = " + str(i) + ", j = " + str(j))
    print("Property holds for m = " + str(m) + ", up to " + str(N))


def checkMidyExpansionReal(expansion, beta):
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


def checkMidyExpansion(expansion, beta):
    if (expansion[0] != "(") or (expansion[-1] != ")"):
        return False
    n = len(expansion) - 2
    if n % 2 != 0:
        return False

    expanded = addExpansions(beta.m, expansion[1:int(
        n/2) + 1], expansion[int(n/2) + 1:-1])
    if "," in expanded:
        return False
    if len(expanded) != n / 2:
        return False
    for i in range(len(expanded)):
        # Check quasigreedy !!TODO!!
        if (i % 2 == 0) and (expanded[i] != beta.m):
            return False
        if (i % 2 != 0) and (expanded[i] != 0):
            return False
    return True


def checkRoundingPrecision(beta, n):
    for i in range(1, n):
        expansion = greedyT(beta, real(1, i))
        if "(" in expansion:
            continue
        if real(1, i) != expansionToReal(beta, expansion):
            print(i)
            return


def checkMidyProperty(beta, n, maximum=0):
    # In base beta checks fractions from 1/n up to n/n for the Midy property
    if maximum == 0:
        maximum = n
    for a in range(1, maximum):
        if gcd(n, a) > 1:
            continue
        expansion = greedyT(beta, real(a, n))
        if checkMidyExpansion(expansion, beta):
            return [True, a, expansion]
    return False


def checkMidyPropertyMatrix(m, n):
    period = PisanoPeriod(m, n)
    for i in range(1, len(period)):
        if period[i] == 0 and period[i - 1] == n - 1:
            return True
    return False


def checkMidyPropertyReal(beta, n, maximum=0):
    if maximum == 0:
        maximum = n
    for a in range(1, maximum):
        if gcd(n, a) > 1:
            continue
        expansion = greedyT(beta, real(a, n))
        if checkMidyExpansionReal(expansion, beta):
            return [True, a, expansion]
    return False


def getMidyNumbers(m, N):
    numbers = []
    for n in range(3, N + 1):
        if checkMidyProperty(real(1, 1, m, 1, 0), n):
            numbers.append(n)
    return numbers


def getMidyNumbersMatrix(m, N):
    numbers = []
    for n in range(3, N + 1):
        if checkMidyPropertyMatrix(m, n):
            numbers.append(n)
    return numbers


def getMidyNumbersReal(m, N):
    # Fails for N > around 50
    # print("Use getMidyNumbers or getMidiyNumbersMatrix instead of this!")
    numbers = []
    for n in range(3, N + 1):
        if checkMidyProperty(real(1, 1, m, 1, 0), n):
            numbers.append(n)
    return numbers


def plotMidyDensity(N=50):
    totals = [0] * N
    # have = []
    pointsX = []
    pointsY = [[] for _ in range(N)]
    for i in range(1, 1000):
        if i % 1000 == 0:
            print(i)
        for m in range(1, N + 1):
            if checkMidyPropertyMatrix(m, i):
                totals[m - 1] += 1
            pointsY[m - 1].append(totals[m - 1] / i)
        pointsX.append(i)

    for m in range(1, N + 1):
        plt.plot(pointsX, pointsY[m - 1])
    plt.show()
