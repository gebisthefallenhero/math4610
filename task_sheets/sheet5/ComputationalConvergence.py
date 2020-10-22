from SecantMethod import secantMethod
from NewtonsMethod import newtonsMethod
from math import exp
import matplotlib.pyplot as plt

if __name__ == '__main__':
    f = lambda x: x * exp(3 * x ** 2) - 7 * x
    f_p = lambda x: 6 * x ** 2 * exp(3 * x ** 2) + exp(3 * x ** 2) - 7
    guess = 1
    guess2 = 1.1
    tols = []
    errors= []
    actualVal = newtonsMethod(f,f_p,guess,tol=.000000000001)
    #This does 10 iterations of the loop from 1 to 10
    for i in range(1,11):
        tol = 1 / (10 ** i)
        tols.append(tol)
        # error = abs(actualVal - secantMethod(f,guess,guess2,tol=tol,errorMessage=True))
        error = abs(actualVal - newtonsMethod(f,f_p,guess,tol=tol))
        errors.append(error)

    figure = plt.figure()
    plt.loglog(tols,errors)
    plt.title("Newtons Method Convergence")
    plt.xlabel('Tolerance')
    plt.ylabel('Errors')
    plt.show()