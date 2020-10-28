from SecantMethod import secantMethod
from NewtonsMethod import newtonsMethod
from math import exp, log
from LinearRegression import linearRegression

if __name__ == '__main__':
    f = lambda x: x * exp(3 * x ** 2) - 7 * x
    f_p = lambda x: 6 * x ** 2 * exp(3 * x ** 2) + exp(3 * x ** 2) - 7
    guess = 1
    guess2 = 1.1
    errors= []
    actualVal = newtonsMethod(f,f_p,guess,tol=.00000001)
    #Changes a lot depending on if you go to 4 or 6
    for i in range(0,4):
        tol = 1 / (10 ** i)
        # error = abs(actualVal - secantMethod(f,guess,guess2,tol=tol,errorMessage=True))
        error = abs(actualVal - newtonsMethod(f,f_p,guess,tol=tol))
        errors.append(error)
    #make the list of errors and take the log of them.
    x = [log(i) for i in errors]
    y = [log(i) for i in errors]
    print(x)
    print(y)
    #Make sure x and y have the right values for the error.
    x.pop()
    y.pop(0)
    print(x)
    print(y)
    print(linearRegression(x,y))