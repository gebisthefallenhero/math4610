
# Condition Number 

**Routine Name:** condNum

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Calculates the condition number of a matrix.

**Input:** 
A: The input matrix

**Output:** 
The condition number of the matrix A

**Example**
Here is an example of running the code

```
if __name__ == '__main__':
	A = diagDomSymmetric(100) #Creates a diagonally dominate symetric Matrix
	print(f'The condition number is {condNum(A)}')

```

This code prints a small condition number for the diagonally dominate symmetric matrix.

```
The condition number is 1.2369546761056278
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
from Transpose import matTranspose
from MatMatMult import matMatMult
from math import sqrt
from PowerIteration import powerIter
from InversePowerIteration import inverPowIter
import math
def condNum(A):
    tol = .0001
    x_0 = [1 for i in range(len(A))]
    AtA = matMatMult(matTranspose(A),A)
    sigma1 = sqrt(powerIter(AtA,x_0,tol)[0])
    sigma2 = sqrt(inverPowIter(AtA,x_0,tol)[0])
    if sigma2 == 0:
        return math.inf
    return sigma1 / sigma2
```
**Last Modified:** December/2020
