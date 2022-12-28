import matplotlib.pyplot as plt
from random import randint


def generate_barnsley_fern(iterations: int):
    # initialize lists
    x, y = [0], [0]
    for i in range(iterations):
        selector = randint(1, 100)
        if selector == 1:
            x.append(0)
            y.append(0.16 * (y[i]))
        elif selector >= 2 and selector <= 86:
            x.append(0.85 * (x[i]) + 0.04 * (y[i]))
            y.append(-0.04 * (x[i]) + 0.85 * (y[i]) + 1.6)
        elif selector >= 87 and selector <= 93:
            x.append(0.2 * (x[i]) - 0.26 * (y[i]))
            y.append(0.23 * (x[i]) + 0.22 * (y[i]) + 1.6)
        elif selector >= 94 and selector <= 100:
            x.append(-0.15 * (x[i]) + 0.28 * (y[i]))
            y.append(0.26 * (x[i]) + 0.24 * (y[i]) + 0.44)
    plt.scatter(x, y, s = 0.2, c ='#2ca02c')
    plt.axis("off")
    plt.savefig('barnsley_fern.png', dpi=250, bbox_inches='tight')
