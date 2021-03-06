
# Power Iteration 

**Routine Name:** powerIter 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Calculates the largest eigenvalue. 

**Input:** 
A: The input matrix
x_0: The intial guess matrix
tol: The tolerance for the vector norm
maxIter: The santity check iterations


**Output:** 
The largest eigenvalue and eigenvector of a matrix

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
    print(powerIter(A,x_0,tol))
```

This code prints out a tuple of the eigenvalue then the eigen vector

```
(-2.000879593348337, [0.8945582874053755, -1.789772249099101])
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
from MatVecMult import matVecMult
from L2Norm import l2Norm
from DotProd import dotProd
def powerIter(A,x_0,tol,maxIter=1000):
    '''
    Returns the largest eigenvalue and vector of a matrix
    :param A: The input matrix
    :param x_0: The intial guess matrix
    :param tol: The tolerance for the vector norm
    :param maxIter: The santity check iterations
    :return: The largest eigen value and eigen vector as a tuple.
    '''
    error = 10.0 * tol
    iter = 0
    l_0 = 0 #The lambda approximation
    y = x_0
    while (error > tol and iter < maxIter):
        v = matVecMult(A,y)
        normV = l2Norm(v)
        v = [v[i] / normV for i in range(len(v))]
        z = matVecMult(A,v)
        l_1 = dotProd(v,z)
        error = abs(l_1 - l_0)
        l_0 = l_1
        y = v
        iter += 1
    return l_0,v
```
**Last Modified:** December/2020
