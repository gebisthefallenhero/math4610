import matplotlib.pyplot as plt
from sys import argv

def plotFunction(f):
    figure = plt.figure()
    figure.xlabel = "x Axis"
    figure.ylabel = "y Axis"
    figure.plot(f)




if __name__ == "__main__":
    if len(argv) == 0:
        print("No functions passed in")

    else:
        figure = plt.figure()
        for arg in argv:
            print(arg)
            figure.plot(eval(arg))
