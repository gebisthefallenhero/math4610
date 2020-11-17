
# Matrix Creator 

**Routine Name:** squareMatrix, upTriMatrix, lowTriMat, diagMat, diagAsArray 

**Author:** Manuel Santana


**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
All these routines return a matrix of size nxn, except diagAsArray, which returns a nx1 array. These are generated using random numbers from (0,100) inclusive, and are used for testing

**Input:** 
size: The size of the desired matrix.

**Output:** 
Returns an nxn matrix.

**Example**
Here is an example of running the code demonstraded only with the square matrix generated. Other routines are used similarly.

```
print("Square")
    printMatrix(squareMatrix(3))
```

This code prints out

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
