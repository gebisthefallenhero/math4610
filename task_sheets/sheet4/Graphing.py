import matplotlib.pyplot as plt
import numpy as np
from sys import argv

def plotFunction(fList, low = -10, high = 10):
    linspace = np.linspace(low, high)

    for f in fList:
        functVal = []
        for val in linspace:
            x = val
            functVal.append(eval(f))
        plt.plot(linspace, functVal)
    plt.legend(argv)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()

if __name__ == "__main__":
    if len(argv) == 0:
        print("No functions passed in")
    else:
        argv = argv[1:]
        plotFunction(argv)


