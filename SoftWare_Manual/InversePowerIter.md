
# Inverse Power Iteration 

**Routine Name:** inverPowerIter 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Calculates the smallest eigenvalue. 

**Input:** 
A: The input matrix
x_0: The intial guess matrix
tol: The tolerance for the vector norm
maxIter: The santity check iterations


**Output:** 
The smallest eigenvalue and eigenvector of a matrix

**Example**
Here is an example of running the code

```
if __name__ == '__main__':
    A = [
        [0,1],
        [-2,-3]
    ]
    x_0 = [1,1]
    tol = .001
    print(inverPowerIter(A,x_0,tol))
```

This code prints out

```
(-1.0009782604070478, [-0.7075678875155642, 0.7066453739725193])
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
from MatVecMult import matVecMult
from L2Norm import l2Norm
from DotProd import dotProd
from ScaledPartialPivoting import scaledPartPiv
def inverPowIter(A,x_0,tol,maxIter=100):
    '''
    Returns the smallest eigenvalue of a matrix
    :param A: The input matrix
    :param x_0: The intial guess matrix
    :param tol: The tolerance for the vector norm
    :param maxIter: The santity check iterations
    :return: The smallest eigen value
    '''
    error = 10.0 * tol
    iter = 0
    l_0 = 0 #The lambda approximation
    y = x_0
    while (error > tol and iter < maxIter):
        v = scaledPartPiv(A,y)
        normV = l2Norm(v)
        v = [v[i] / normV for i in range(len(v))]
        z = scaledPartPiv(A,v)
        l_1 = dotProd(v,z)
        error = abs(l_1 - l_0)
        l_0 = l_1
        y = v
        iter += 1
    return l_0,v
```
**Last Modified:** December/2020
