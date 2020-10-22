
# Hybrid Method 


**Routine Name:** HybridMethod 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher.



**Description/Purpose:** 
This program returns the root of a function up to a tolerance using a bisection-newtons hybrid method.

**Input:** 
f Function Object, This is a function of the function to be approxmiated.
f_p Function object. This is the derivitive of the function to be approximated.
a float: A start value for the bisection method. 
b float: An end value for the bisection method. Note [a,b] must bracket a root.
tol Float: The tolerance to run until. Set at .001 by default.
maxIter int: The maximum number of iterations before deciding if the method will not converge. Set to 1000.
**Output:** 
Returns a float representation of root of the function.

**Example**
Here is an example driver program using the method.
```
if __name__ == '__main__':
    from math import exp

    f = lambda x: x * exp(3 * x ** 2) - 7 * x
    f_p = lambda x: 6 * x ** 2 * exp(3 * x ** 2) + exp(3 * x ** 2) - 7
    a = .5
    b = 10
    print(hybridMethod(a,b,f,f_p))
```
This code outputs

```
0.8053798692388103
```


**Implementation/Code:** 
Here is the implemenation for the routine. Note that this routine relies on calling Newtons method. If moved outside of the library then newtons method must be moved as well, or reimplemented in the class containing the hybrid method. Also note the helper function bisect, which reduces the error by one order of magnitude and returns the new brackts for the root.

```

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

```
**Last Modified:** October/2020
