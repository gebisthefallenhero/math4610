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
For this task all that was needed to be done was to switch the line in the hybrid method using newtons method to a line using the secant method and it gave the same root as in tasks 3 and 2. Well I shouldn't say all because it also required playing with how a and b were incremented towards the origin. The secant method for what ever reason required a different increment than newtons method to avoid division by zero. For what ever reason some increments caused the function to fail.

### Task 5
For this task a wrote a new functoin which I will put in here for convenience. The entry for this function can be found in the [software manual](../../SoftWare_Manual/Table_of_Contents.md)

```
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
 ```
 This function creates a linspace off of a specified number of intervals. It then checks those intervals to see if they have a root by the intermediate value theorem, and then if so they use a hybrid method to caclulate the root. Using this function with 500 subintervals intervals of [-5,6] we get the following.

 ```

All the roots possible to find are [-1.7229456481933667, -1.7051042175293047, -1.3215863037109445, -1.035767242431647, -0.48361069854286604, 0.48361069854290567, 1.0357669372558536, 1.3215861833429055, 1.7051042125203324, 1.7229453430175732
]

```
There are 10 roots in total. The first and last two were the most confusing to find since they are so close together.

### Task 6
The first website I looked at suggested the same of idea of dividing it into many sub intervals. The con of this approach though is that there really isn't a way to know if you got all the roots of your function, but you can have a good guess by making the intervals small enough. Interestingly though there is a lot of research that has gone on even in recent years to find multiple roots, and skimming though on article it seems that some methods have good ways to show just how large the number of subintervals that you need is to be fairly confident that you have found all the roots. The downside to this is that it is much more complecated to understand and implement, and so depending on your need it may be better to just keep making your interval size smaller until you have the roots that you desire.

[https://www.mathworks.com/matlabcentral/answers/391474-bisection-method-multiple-roots](https://www.mathworks.com/matlabcentral/answers/391474-bisection-method-multiple-roots)

[https://www.sciencedirect.com/science/article/pii/S0377042712001045](https://www.sciencedirect.com/science/article/pii/S0377042712001045)

