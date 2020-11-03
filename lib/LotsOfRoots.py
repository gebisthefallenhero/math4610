from NewtonsMethod import newtonsMethod
from SecantMethod import secantMethod
from FixedPoint import fixedPoint
from Bisection import bisection
from HybridMethod import hybridMethod
from math import sin, exp, cos

def hybridMethod(a,b,f,f_p,tol=.001,maxIter=1000):
    if a > b:
        a,b = b,a
    if f(a)*f(b) > 0:
        mid = (a + b) / 2
        print('Error: [a b] does not contain a root')
        return
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    #Error B is the bisection error
    errorB = tol * 10
    iter = 0

    while errorB > tol and iter < maxIter:
        iter += 1
        mid = (a + b) * .5
        newtonsGuess = newtonsMethod(f,f_p,mid,tol=tol)
        errorN = abs(newtonsGuess - mid)
        if errorN < tol:
            return newtonsGuess
        else:
            a,b = bisect(a,b,mid,f)
            if abs(b - a) < tol:
                return a


def bisect(a,b,mid,f):
    # The number of iterations needed to decrease by one order of magnitude using the bisection method.
    ITER_ONE_ORDER_MAG = 4
    for i in range(ITER_ONE_ORDER_MAG):
        f_a = f(a)
        f_mid = f(mid)
        if f_mid * f_a < 0:
            b = mid
        else:
            a = mid
    return a,b


if __name__ == '__main__':
    function = lambda x: exp(- (x * x)) * sin(4 * ( x * x) - 1) + .051
    functionP = lambda x: exp(- (x * x)) * cos(4 * ( x * x) - 1) * 8 * x + sin(4 * ( x * x) - 1) *  exp(- (x * x)) * ( - 2 * x)
    print("The root using the bisection method is " + str(bisection(function,-.1,1)))
    print("Good, we've found the root, now to test the rest of the methods.")
    print(f"The root using Newtons method is {newtonsMethod(function,functionP,.3)} ")
    print(f"The root using Secant method is {secantMethod(function,.25,.3)} ")
    print(f"The root using Hybrid method is {hybridMethod(-.2, 1,function,functionP)} ")
    print(f"The root using FixedPoint method is {fixedPoint(function, .3)} ")

    try:
        print(f"\n Now testing the newtons Method with guess - 5.0. This gives { newtonsMethod(function,functionP,-5)}")
        print(f"Now testing newtons Method with guess 6. This gives {newtonsMethod(function,functionP,6)}")
    except:
        print("Newton's method failed")

    print(f"The closest root to zero using the modified hybrid method is {modifiedHybridMethod(-5,6,function,functionP)}")