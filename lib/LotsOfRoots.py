from NewtonsMethod import newtonsMethod
from SecantMethod import secantMethod
from FixedPoint import fixedPoint
from Bisection import bisection
from HybridMethod import hybridMethod, bisect
from math import sin, exp, cos


def modifiedHybridMethod(a,b,f,f_p,tol=.001,maxIter=1000, increment=.1):
    for i in range(maxIter):
        if f(a) * f(b) < 0:
            return modifiedHybridMethod2(a,b,f,f_p,tol=tol)
        b = b - increment
        a = a + increment
    print("Did not converge :( ")

def modifiedHybridMethod2(a,b,f,f_p,tol=.001,maxIter=1000):
    if a > b:
        a,b = b,a
    if f(a)*f(b) > 0:
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
            a,b = bisect2(a,b,mid,f)
            if abs(b - a) < tol:
                return a


def bisect2(a,b,mid,f):
    # The number of iterations needed to decrease by one order of magnitude using the bisection method.
    ITER_ONE_ORDER_MAG = 4
    for i in range(ITER_ONE_ORDER_MAG):
        f_a = f(a)
        f_mid = f(mid)
        f_b = f(b)
        if (f_mid * f_a < 0) and (f_mid * f_b < 0 ):
             if (mid > 0):
                 b = mid
             else:
                 a = mid
        if f_mid * f_a < 0:
            b = mid
        else:
            a = mid
        mid = (a + b) / 2
    return a,b

#Hybrid method using secand to find the root closest to zero.
def modHybSecMethod(a,b,f,tol=.001,maxIter=1000, increment=.1):
    for i in range(maxIter):
        if f(a) * f(b) < 0:
            return modHybSecMethod2(a,b,f,tol=tol)
        b = b - increment
        a = a + increment
    print("Did not converge :( ")

#Wraped function for the hybrid method to do the actual root finding.
def modHybSecMethod2(a,b,f,tol=.001,maxIter=1000):
    if a > b:
        a,b = b,a
    # if f(a)*f(b) > 0:
    #     print('Error: [a b] does not contain a root')
        # return
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
        secantGuess = secantMethod(f,a,b,tol=tol,maxIter = 10)
        errorS = abs(secantGuess - mid)
        if errorS < tol:
            return secantGuess
        else:
            a,b = bisect2(a,b,mid,f)
            if abs(b - a) < tol:
                return a




def findManyRoots(a,b,f,f_p,numIntervals = 100):
    stepSize = (abs(a) + abs(b)) / numIntervals
    xIntervals = [a]
    # This loop creates the linspace needed to find the intervals.
    for i in range(numIntervals):
        xIntervals.append(xIntervals[i] + stepSize)
    roots = []
    for i in range(len(xIntervals)):
        if i == len(xIntervals) - 1:
            continue
        a = xIntervals[i]
        b = xIntervals[i+1]
        if f(a) * f(b) > 0:
            continue
        root = hybridMethod(a,b,f,f_p,tol=.000001)
        if root != None:
            roots.append(root)
    return roots





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
    print(f"The closet root to zero using the modified secant hybrid method is {modHybSecMethod(-5,6,function,increment=1)}")
    print(f"All the roots possible to find are {findManyRoots(-5,6,function,functionP,numIntervals=500)}")