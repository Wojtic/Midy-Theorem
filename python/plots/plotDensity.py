import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def read_txt(filename="midy_denominators.txt"):
    midy_dict = {}

    with open(filename, 'r') as file:
        current_m = None
        for line in file:
            line = line.strip()
            if line.startswith("Midy numbers for m ="):
                current_m = int(line.split("=")[1].strip()[:-1])
                midy_dict[current_m] = []
            elif line and current_m is not None and line[0].isdigit():
                midy_dict[current_m] = list(map(int, line.split()))
    print("Data loaded")
    return midy_dict


def plotMidyDensity(data, max_m=100):
    """
    pointsX = []
    total = 0
    pointsY = []
    for i in range(1, 100001):
        if i in data[1]:
            total += 1
        pointsX.append(i)
        pointsY.append(total / i)
    plt.plot(pointsX, pointsY)
    plt.show()
    """
    N = 100

    totals = [0] * N
    # have = []
    pointsX = []
    pointsY = [[] for _ in range(N)]
    for i in range(1, 100000):
        if i % 100 == 0:
            print(i)
        for m in range(1, N + 1):
            if i in data[m]:
                totals[m - 1] += 1
            pointsY[m - 1].append(totals[m - 1] / i)
        pointsX.append(i)

    colours = cm.viridis(np.linspace(0, 1, N))
    for m in range(1, N + 1):
        # if (m - 1) % 7 != 0:
        #    continue
        plt.plot(pointsX, pointsY[m - 1], color=colours[m - 1])
        # plt.text(pointsX[-1], pointsY[m - 1][-1], f'{m}')
        print(m, pointsY[m-1][-1])

    plt.grid(axis="y")
    plt.xlabel("N")
    plt.ylabel("Hustota")
    plt.show()


if __name__ == "__main__":
    data = read_txt()
    plotMidyDensity(data, max_m=1)
