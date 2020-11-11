
# RowReduce 


**Routine Name:** RowReduce 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Performs Gaussian elimination on a matrix. No pivoting strageties are implemented yet.

**Input:** 
A: The maxtrix to be row reduced. 
b: The vector on the solution side of the matrix equation

**Output:** 
Returns the solution vector x

**Example**
Here is an example of running the code

```
if __name__ == '__main__':
    testMatrix = [
        [1, -3, 1],
        [2, -8,  8],
        [-6, 3, -15]
    ]
    testB = [4,-2,9]
    
    A,b = rowReduce(testMatrix,testB)
    for row in A:
    	print(A)
    print(b)
```
This code prints out

```
[1, -3, 1]
[0.0, -2.0, 6.0]
[0.0, 0.0, -54.0]
[4, -10.0, 108.0]

```
**Implementation/Code:** 
Here is the implemenation for the routine.

```
def rowReduce(A,b):
    '''
    Row reduce a matrix that is assumed to be in good form, aka no pivoting strategies.
    :param A: The Matrix to be reduced
    :param b: The b vector in Ax = b
    :return: A tuple containing both A and b.
    '''
    numRows = len(A)
    numColumns = len(A[0])
    for  k in range(numRows - 1):
        for i in range(k + 1, numColumns):
            factor = A[i][k] / A[k][k]
            for j in range(k, numColumns):
                A[i][j] = A[i][j] - factor * A[k][j]
            b[i] = b[i] - factor * b[k]
    return A,b
```
**Last Modified:** November/2020
