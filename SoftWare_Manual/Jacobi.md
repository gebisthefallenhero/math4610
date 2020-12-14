
# Jacobi Iteration 

**Routine Name:** jacobiIteration

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Attempts to solve the system of equations using jacobi iteration

**Input:** 
A The matrix to be solved over
x_0 The inital guess vector
b The vector on the right side of the equation
tol The tolerance to be run to
maxIter The max number of iterations.
**Output:** 
A vector with the approximated solution.
**Example**
Here is an example of running the code against a differnt systems of equations solver.

```
if __name__ == '__main__':
    from ScaledPartialPivoting import scaledPartPiv
    A = [
        [10,2,1],
        [3,20,4],
        [4,4,20]
    ]
    b = [5,17,26]
    x_0 = [0, 0, 0]
    tol = .001
    print(jacobiIteration(A,x_0,b,tol))
    print(scaledPartPiv(A,b))
```

This code prints out

```
[0.27036365537, 0.5836108398200001, 1.12921393114]
[0.2703583061889251, 0.5836047774158525, 1.1292073832790444]
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
from MatVecMult import matVecMult
from VecSub import vecSub
from L2Norm import l2Norm
def jacobiIteration(A,x_0,b,tol,maxIter=1000):
    '''
    Performs the Jacobi Iteration using the residual update method.
    A The matrix to be solved over
    x_0 The inital guess vector
    b The vector on the right side of the equation
    tol The tolerance to be run to
    maxIter The max number of iterations.
    '''
    error = tol * 10
    x_old = []
    x_new = []
    for val in x_0: #Intialize the x_old and x_new vectors.
        x_old.append(val)
        x_new.append(val)
    iter = 0
    while (error > tol and iter < maxIter):
        iter += 1
        Ax = matVecMult(A,x_old)
        res = vecSub(b,Ax)
        for i in range(len(x_new)):
            x_new[i] = x_old[i] + res[i] / A[i][i]
        error = l2Norm(res)
        for i in range(len(x_old)):
            x_old[i] = x_new[i]
    return x_new

```
**Last Modified:** December/2020
