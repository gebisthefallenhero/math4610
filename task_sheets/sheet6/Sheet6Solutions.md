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

