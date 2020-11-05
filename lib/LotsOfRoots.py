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








# #This modified hybrid method recursively moves the left endpoint towards the orirgin.
# def modifiedHybridMethod(a,b,f,f_p,tol=.001,maxIter=1000,numIter=0, bestGuess =0):
#     if (b < 0):
#         return bestGuess
#     if a > b:
#         a,b = b,a
#     if f(a)*f(b) > 0:
#         if numIter < maxIter:
#             #Try the method again but moving b closer to the origin
#             return modifiedHybridMethod(a,b - .1,f,f_p,numIter=numIter + 1)
#         print('Error: No Root found in maximum iterations')
#         return
#     if f(0) == 0:
#         return 0
#     #Error B is the bisection error
#     errorB = tol * 10
#     iter = 0
#     while errorB > tol and iter < maxIter:
#         iter += 1
#         mid = (a + b) * .5
#         newtonsGuess = newtonsMethod(f,f_p,mid,tol=tol)
#         errorN = abs(newtonsGuess - mid)
#         if errorN < tol:
#             #The case where the root actually zero is taken care of above
#             if bestGuess == 0:
#                 bestGuess =  newtonsGuess
#                 break
#             else:
#                 if abs(newtonsGuess) < abs(bestGuess):
#                     bestGuess = newtonsGuess
#         else:
#             a,b = bisect2(a,b,mid,f)
#             mid = (a + b) * .5
#             newtonsGuess = newtonsMethod(f, f_p, mid, tol=tol)
#             errorN = abs(newtonsGuess - mid)
#             if errorN < tol:
#                 # The case where the root actually zero is taken care of above
#                 if bestGuess == 0:
#                     bestGuess = newtonsGuess
#                     break
#                 else:
#                     if abs(newtonsGuess) < abs(bestGuess):
#                         bestGuess = newtonsGuess
#             if abs(b - a) < tol:
#                 if bestGuess == 0:
#                     bestGuess = a
#                 else:
#                     if abs(a) < abs(bestGuess):
#                         bestGuess = a
#                 break
#     return modifiedHybridMethod(a,b -.1,f,f_p,numIter=numIter + 1, bestGuess=bestGuess)
#
# def bisect2(a,b,mid,f):
#     # The number of iterations needed to decrease by one order of magnitude using the bisection method.
#     ITER_ONE_ORDER_MAG = 4
#     for i in range(ITER_ONE_ORDER_MAG):
#         mid = (a + b) / 2
#         if mid > 0:
#             b = mid
#         if mid < 0:
#             a = mid
#         # f_a = f(a)
#         # f_mid = f(mid)
#         # if f_mid * f_a < 0:
#         #     b = mid
#         # else:
#         #     a = mid
#     return a,b




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
    # print(f"The closet root to zero using the modified secant hybrid method is {modSecHybMethod(-5,6)}")