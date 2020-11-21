
# LU Factorization 

**Routine Name:** LUForwardSolve 

**Author:** Manuel Santana


**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Does the forward substitution on an inplace LU factorized matrix.

**Input:** 
A: A matrix that has had LU factorization performed on it.
b: The vector on the right side of the matrix equation.

**Output:** 
xVec: The solution vector to the system of equations.

**Example**
Here is an example of solving the lower part of the system of equations.
```

if __name__ == '__main__':
    from MatrixCreator import printMatrix
    test = [
        [1,1,1],
        [2,3,5],
        [4,6,8]
    ]
    A = LUFact(test)
    printMatrix(A)
    b = [1,1,1]
    print('Solving Lc = b with b = [1,1,1]')
    c = LUForwardSolve(A,b)
    print(c)
```

This code prints out

```
[1, 1, 1]
[2.0, 1.0, 3.0]
[4.0, 2.0, -2.0]
Solving Lc = b with b = [1,1,1]
[1.0, -1.0, -1.0]
```
Here is the implementation for the routine.

```
def LUForwardSolve(A,b):
    '''
    A forward substitution after an LU Factorization has been performed
    :param A: A matrix has has been LU factorized
    :param b: the vector on the right side of the equation
    :return: A solution vector
    '''
    #Change the entries of the passed in matrix to match the forward substitution.
    for i in range(len(A)):
        A[i][i] = 1
    numRows, numColumns = len(A), len(A)
    xVec = [0] * numRows
    for row in range(numRows):
        sum = b[row]
        for column in range(row):
            sum -= A[row][column] * xVec[column]
        xVec[row] = sum / A[row][row]
    return xVec
```
**Last Modified:** November/2020
