
# BackSolve 


**Routine Name:** BackSolve

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Perfroms back substitution on an upper triangular matrix

**Input:** 
A: A 2d list as a matrix
b: The vector on the solution side of the matrix equation

**Output:** 
Returns the solution vector x

**Example**
Here is an example of running the code

```
if __name__ == '__main__':
    testMatrix = [
        [1,2,3],
        [0,1,2],
        [0,0,10]
    ]
    testB = [6,4,30]
    solution = backSolve(testMatrix,testB)
    print(solution)
```

This code prints out

```
[1.0, -2.0, 3.0]
```
**Implementation/Code:** 
Here is the implemenation for the routine.

```
def backSolve(A,b):
    '''
    :param A: The upper triangular matrix to be back substituted
    :param b: The b vector in the system of equations
    :return: The solution vector x.
    '''
    numRows, numColumns = len(A), len(A)
    xVec = [0] * numRows
    for row in range(numRows - 1, -1, -1):
        sum = b[row]
        for column in range(row +1, numColumns):
            sum -= A[row][column] * xVec[column]
        xVec[row] = sum / A[row][row]
    return xVec
```
**Last Modified:** November/2020
