import numpy as np
import matplotlib.pyplot as plt


def randomSequence(low_x,high_x,low_y,high_y,N):
    x = np.random.uniform(low_x,high_y,N)
    y = np.random.uniform(low_y,high_y,N)
    return x,y

def circleAreaMC(xvals,yvals):
    n = 0
    N = len(xvals)
    distance = np.zeros(N)
    for i in range(N):
        distance[i] = np.sqrt(xvals[i]**2+yvals[i]**2)
        if distance[i] <= 1:
            n += 1
    A_square = 4
    A_circle = A_square * n/N
    return A_circle

if __name__ == '__main__':
    low_x = -1
    high_x = 1
    low_y = -1
    high_y = 1
    N = 10000
    x,y = randomSequence(low_x,high_x,low_y,high_y,N)
    A_circle = circleAreaMC(x,y)
    print(A_circle)
    p = np.arange(0, 2 * np.pi, 0.01)
    plt.plot(np.sin(p), np.cos(p))
    plt.plot(x,y , 'o')
    plt.show()