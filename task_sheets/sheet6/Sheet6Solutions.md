# Sheet 6 Solutions.

For all tasks involving code see the file [LotsOfRoots](../../lib/LotsOfRoots.py)

### Task 1
Running each method on the code, though using different guesses printed out the following.

```
The root using the bisection method is 0.48370361328125
Good, we've found the root, now to test the rest of the methods.
The root using Newtons method is 0.4836108116478235 
The root using Secant method is 0.4836105999005513 
The root using Hybrid method is 0.4836108103158168 
The root using FixedPoint method is 0.48393241039733603 

```
One interesting thing while running this code what that a bad guess lead to a division by zero error really quickly in most of the methods.

### Task 2
I was duped. The newton's method crashed with both guesses. This is because the derivative at -5 and 6 is very close to zero, and therefore led to a division byzero error.

### Task 3
For this task the first thing I did was write a wrapper function to find a bracketed root. It looks like this

```
def modifiedHybridMethod(a,b,f,f_p,tol=.001,maxIter=1000, increment=.1):
    for i in range(maxIter):
        if f(a) * f(b) < 0:
            return modifiedHybridMethod2(a,b,f,f_p,tol=tol)
        b = b - increment
        a = a + increment
    print("Did not converge :( ")

```
This function moves a and b both towards zero and tries to find a bracketed root. Next the logic needed to be changed in the bisection method. It looks like this now.

```
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
```
Essentially what this does is it says if given the choice between intervals choose the one that still has zero in it. I will say this is not a fool proof method but it seems to work in this situation. It should be noted that this returned the same root as in task 2.

### Task 4
For this task all that was needed to be done was to switch the line in the hybrid method using newtons method to a line using the secant method and it gave the same root as in tasks 3 and 2.
