from NewtonsMethod import newtonsMethod

def hybridMethod(a,b,f,f_p,tol=.001,maxIter=1000):
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
    from math import exp

    f = lambda x: x * exp(3 * x ** 2) - 7 * x
    f_p = lambda x: 6 * x ** 2 * exp(3 * x ** 2) + exp(3 * x ** 2) - 7
    a = .5
    b = 10
    print(hybridMethod(a,b,f,f_p))