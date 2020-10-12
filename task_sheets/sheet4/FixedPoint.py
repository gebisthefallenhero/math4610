from math import exp

def fixedPoint(f, initialGuess, tol=.001, maxIter=1000):
    x_0 = initialGuess
    x = x_0 - f(x_0)
    for i in range(maxIter):
        x_new = x - .000000001 * f(x)
        error = abs(f(x_new))
        if (error < tol):
            return x_new
        x = x_new
    print("Did not converge")


if __name__ == "__main__":
    f = lambda x: x * exp(3 * x ** 2) - 7 * x
    guess = .9
    root = fixedPoint(f,guess)
    print(f'The root is {root}')