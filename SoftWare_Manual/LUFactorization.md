
# LU Factorization 

**Routine Name:** LUFact 

**Author:** Manuel Santana


**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Performs an inplace LU factorization of a matrix.

**Input:** 
A: The matrix to be LU factorized. Must be square.

**Output:** 
A: The matrix LU factorized. There diagonal entries come from the matrix U, and all other code should assume the diagonal entries for L should be 1.

**Example**
Here is a example of performing the LU Factorization.

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

```

This code prints out

```
[1, 1, 1]
[2.0, 1.0, 3.0]
[4.0, 2.0, -2.0]
```
Here is the implementation for the routine.

```

def LUFact(A):
    '''
    Performs an LU Factorization on A
    :param A: The Matrix to be LU factorized
    :return: A matrix with L in the lower half and U above the diagonal. The diagonal holds the entries of U
    '''
    numRows = len(A)
    numColumns = len(A[0])
    for k in range(numRows - 1):
        for i in range(k + 1, numColumns):
            factor = A[i][k] / A[k][k]
            A[i][k] = factor
            for j in range(k + 1, numColumns):
                A[i][j] = A[i][j] - factor * A[k][j]
    return A
```
**Last Modified:** November/2020
