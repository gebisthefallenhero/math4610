
# Find Many Roots


**Routine Name:** findManyRoots 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. Note it does depend on the routine Hybrid Method.


**Description/Purpose:** 
Given an interval this routine uses a hybrid method to attempt to find as many roots as possible of the function in the interval.

**Input:** 
a,b float The left and right endpoint of the interal desired.
f function object: The function you are trying to find roots for.
f_p function object. The deriviate of the function.
numIntervals int. Default set to 100. This will be the number of intervals to look for the root in.

**Output:** 
Returns of list of all the roots found.

**Example**

```
if __name__ == '__main__':
    function = lambda x: exp(- (x * x)) * sin(4 * ( x * x) - 1) + .051
    functionP = lambda x: exp(- (x * x)) * cos(4 * ( x * x) - 1) * 8 * x + sin(4 * ( x * x) - 1) *  exp(- (x * x)) * ( - 2 * x)

print(f"All the roots possible to find are {findManyRoots(-5,6,function,functionP,numIntervals=500)}")

```

This code prints out

```

All the roots possible to find are [-1.7229456481933667, -1.7051042175293047, -1.3215863037109445, -1.035767242431647, -0.48361069854286604, 0.48361069854290567, 1.0357669372558536, 1.3215861833429055, 1.7051042125203324, 1.7229453430175732]
```


**Implementation/Code:** 
Here is the implemenation for the routine.

```
def findManyRoots(a,b,f,f_p,numIntervals = 100, tol=.0001):
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
        root = hybridMethod(a,b,f,f_p,tol=tol)
        if root != None:
            roots.append(root)
    return roots
```
**Last Modified:** November/2020
