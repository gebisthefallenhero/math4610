
# FixedPoint 

**Routine Name:** FixedPoint 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher.

**Description/Purpose:** 
This program finds a single root of a given function using fixed point iteration. There is a test function that can be ran from the command line using
```
python FixedPoint.py
```

**Input:** 
f: A function object for the function that you want to approximate.
initialGuess: Float. An initial guess to start the iteration.
maxIter int. Default 1000. How many iterations to go before deciding it doesn't convervge. 
tol: float This is set default to .001, but can be passed in.
epsilo: float. This value is set to .01 normally, but can be passed in to make to help the root to converge.
**Output:** 
Returns an approximation to tolerance of a root found by the function.

**Implementation/Code:** 
```


def fixedPoint(f, initialGuess, tol=.001, maxIter=1000,epsilon = .01):
    x_0 = initialGuess
    x = x_0 -  epsilon * f(x_0)
    for i in range(maxIter):
        x_new = x -  epsilon * f(x)
        error = abs(f(x_new))
        if (error < tol):
            return x_new
        x = x_new
    print("Did not converge")

if __name__ == "__main__":
    f = lambda x: x * exp(3 * x ** 2) - 7 * x
    guess = -.1
    root = fixedPoint(f,guess, epsilon = .001)
    print(f'The root is {root}')
```
**Last Modified:** October/2020
