
# Newtons Method 


**Routine Name:** NewtonsMethod 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher.



**Description/Purpose:** 
This program returns the root of a function up to a tolerance using newtons method.

**Input:** 
f Function Object, This is a function of the function to be approxmiated.
f_p Function object. This is the derivitive of the function to be approximated.
x_start The initial point to start the newton iteration
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
    f_p = lambda x: 6 * x ** 2 * exp(3 * x ** 2) + exp(3 * x ** 2) - 7
    guess = 1
    print(newtonsMethod(f,f_p,guess,errorMessage=True))
```
This code outputs
```
0.8053798692388103
```


**Implementation/Code:** 
Here is the implemenation for the routine.

```

def newtonsMethod(f,f_p,x_start,tol=.001,maxIter=1000,errorMessage=False):
    x_old = x_start
    error = tol * 10
    iter = 0
    while error > tol and iter < maxIter:
        iter += 1
        x_new = x_old - (f(x_old)/ f_p(x_old))
        error = abs(x_new - x_old)
        x_old = x_new
        if error < tol:
            return x_new
    if errorMessage == True:
        print("Did not converge")

```
**Last Modified:** October/2020
