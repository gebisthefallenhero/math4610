
# Secant Method

**Routine Name:** secantMethod 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher.



**Description/Purpose:** 
This program returns the root of a function up to a tolerance using the secant method.

**Input:** 
f Function Object, This is a function of the function to be approxmiated.
x_0: Float The first inital point to start the secant iteration.
x_1: Float The second initial point to start the secant iteration
tol Float: The tolerance to run until. Set at .001 by default.
maxIter int: The maximum number of iterations before deciding if the method will not converge. Set to 1000.
errorMessage Boolean: Set to False. If printing and error message is desired then pass in True.
**Output:** 
Returns a float representation of root of the function.

**Example**
Here is an example driver program using the method.
```
if __name__ == "__main__":
    f = lambda x: x * exp(3 * x ** 2) - 7 * x
    guess = 1
    guess2 = 1.1
    print(secantMethod(f,guess,guess2,errorMessage=True))

```
This code outputs
```
0.8053805244336557

```


**Implementation/Code:** 
Here is the implemenation for the routine.

```
def secantMethod(f,x_0,x_1,tol=.001,maxIter=1000,errorMessage=False):
    x_old = x_0
    x_curr = x_1
    error = tol * 10
    iter = 0
    while error > tol and iter < maxIter:
        iter += 1
        f_curr = f(x_curr)
        x_new = x_curr - f_curr * ((x_curr - x_old)/(f(x_curr) - f(x_old)))
        error = abs(x_new - x_curr)
        x_old = x_curr
        x_curr = x_new
        if error < tol:
            return x_new
    if errorMessage == True:
        print("Did not converge")

```
**Last Modified:** October/2020
