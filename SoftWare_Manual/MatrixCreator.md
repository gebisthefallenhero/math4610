
# Matrix Creator 

**Routine Name:** squareMatrix, upTriMatrix, lowTriMat, diagMat, diagAsArray, diagDom

**Author:** Manuel Santana


**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
All these routines return a matrix of size nxn, except diagAsArray, which returns a nx1 array. These are generated using random numbers from (0,100) inclusive, and are used for testing. upTriMatrix returns an upper triangular matrix, lowTriMat a lower triangular matrix, diagMat a diagonalMatrix, diagAsArray a diagonal matrix just represented a 1-D array, and diagDom returns a diagonally dominate matrix.

**Input:** 
size: The size of the desired matrix.

**Output:** 
Returns an nxn matrix.

**Example**
Here is an example of all the routine being run
```
if __name__ == '__main__':
    print("Square")
    printMatrix(squareMatrix(3))
    print("Lower Triangular")
    printMatrix(lowTriMat(3))
    print("Upper Triangular")
    printMatrix(upTriMat(3))
    print("Diagonal")
    printMatrix(diagMat(3))
    print("Diagonal As an Array")
    print(diagAsArray(3))
    print('Diagonally Dominate Matrix')
    printMatrix(diagDom(3))
```

This code prints out

```
Square
[93, 96, 55]
[68, 99, 71]
[84, 90, 61]
Lower Triangular
[10, 0, 0]
[50, 98, 0]
[27, 86, 64]
Upper Triangular
[7, 5, 57]
[0, 72, 35]
[0, 0, 96]
Diagonal
[40, 0, 0]
[0, 61, 0]
[0, 0, 43]
Diagonal As an Array
[25, 11, 47]
Diagonally Dominate Matrix
[9, 8, 0]
[16, 20, 3]
[8, 4, 23]
```

**Implementation/Code:** 
Here is the implemenation for the routine shown above. The implementation for other routines is similar. 

```
def squareMatrix(size):
    '''
    Returns a random matrix of size n X n with random intergers between 1 and 100
    :param size: The number of rows and columns of your matrix
    :return: An nxn matrix
    '''
    matrix = []
    for j in range(size):
        matrix.append([])
        for i in range(size):
            matrix[j].append(randint(0,100))
    return matrix
```
**Last Modified:** November/2020
