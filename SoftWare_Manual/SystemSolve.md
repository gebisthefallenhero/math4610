
# Gaussian Solution 

**Routine Name:** systemSolve 

**Author:** Manuel Santana


**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Solves a system of equations by row reduction and then a back substitution. No pivoting used.

**Input:** 
A: The matrix represeting the system of equations.
b: The vector on the right side of the equations.

**Output:** 
xVec: A 1-D vector containg the solutions to the system.

**Example**
Here is an example using the diagonally dominate routine from the MatrixCreator suite.
```
if __name__ == '__main__':
    from MatrixCreator import diagDom,printMatrix,diagAsArray
    A = diagDom(3)
    print('The matrix A')
    printMatrix(A)
    print('B vector')
    b = diagAsArray(3)
    print(b)
    x = systemSolve(A,b)
    print('Solution x')
    print(x)

```

This code prints out

```
The matrix A
[23, 13, 9]
[4, 22, 17]
[4, 3, 8]
B vector
[44, 29, 67]
Solution x
[1.8081985708913129, -6.735238811583301, 9.996615268898081]

```
Here is the implementation for the routine.

```
def systemSolve(A,b):
    '''
    Solve a system of linear equations. No pivoting strategies used.
    :param A: The Matrix with the equations.
    :param b: The solution vector
    :return: A vector containing the solution to the equation.
    '''
    #The code for the row reducing.
    numRows = len(A)
    numColumns = len(A[0])
    for k in range(numRows - 1):
        for i in range(k + 1, numColumns):
            factor = A[i][k] / A[k][k]
            for j in range(k, numColumns):
                A[i][j] = A[i][j] - factor * A[k][j]
            b[i] = b[i] - factor * b[k]
    #The code for the back substitution
    xVec = [0] * numRows
    for row in range(numRows - 1, -1, -1):
        sum = b[row]
        for column in range(row + 1, numColumns):
            sum -= A[row][column] * xVec[column]
        xVec[row] = sum / A[row][row]
    return xVec
```
**Last Modified:** November/2020
