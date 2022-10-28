from random import randint
import numpy as np
import matplotlib.pyplot as plt

m1 = [[0],
      [25]]
m2 = [[0],
      [0]]
m3 = [[25],
      [0]]

b1 = [[15, 0],
      [0, 2]]
b2 = [[7, 0],
      [1, 7]]
b3 = [[2, 0],
      [0, 18]]


def get_y():
    summ = 0
    for j in range(12):
        summ += randint(0, 100) / 100 - 0.5

    return summ


def get_xy(m, b):
    N = 200
    n = 2
    a00 = np.sqrt(b[0][0])
    a01 = 0
    a10 = b[0][1] / np.sqrt(b[0][0])
    a11 = np.sqrt(b[1][1] - (b[0][1] * b[0][1] / b[0][0]))
    a = [[a00, a01],
         [a10, a11]]
    x = [[0 for _ in range(2)] for _ in range(200)]

    for i in range(N):
        for k in range(n):
            A = 0
            for l in range(n):
                y = get_y()
                A += a[l][k] * y

            x[i][k] = A + m[k]

    ox = [item[0] for item in x]
    oy = [item[1] for item in x]

    return ox, oy


def main():
    x1, y1 = get_xy(m1, b1)
    x2, y2 = get_xy(m2, b2)
    x3, y3 = get_xy(m3, b3)

    plt.rcParams["figure.autolayout"] = True
    plt.plot(x1, y1, color='red', marker='+', linestyle='')
    plt.plot(x2, y2, color='green', marker='*', linestyle='')
    plt.plot(x3, y3, color='blue', marker='x', linestyle='')
    plt.show()


if __name__ == '__main__':
    main()
