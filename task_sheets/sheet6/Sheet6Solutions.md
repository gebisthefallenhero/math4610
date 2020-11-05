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
The first step was to deal with the fact that the interval [-5,6] was not guaranteed to bracked a root by the intermedite value theorem. In order to deal with this the modified method added this block of code
```
if f(a)*f(b) > 0:
    if numIter < maxIter:
      #Try the method again but moving b closer to the origin
       return modifiedHybridMethod(a,b - .1,f,f_p,numIter=numIter + 1)
```
What this code does is recursively try to find the root again this time moving b slightly closer to the origin. Then each time a root was found if that root was closer to zero than the last one it was saved as the best answer, and passed into the next recusive call. The recurssion ends if a negative b is passed into the code. This works since on that last iteration the best root between a and b at that point will be found, and compared with the current best root. The code output

```
The closest root to zero using the modified hybrid method is -0.48361071309741366
```
This compares is consistent with the answers in task 1 sincethe code has a root at + or - .4836 and therefor this is the best root.
