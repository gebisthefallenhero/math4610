
# Transpose

**Routine Name:** matTranspose.py 

**Author:** Manuel Santana


**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Returns a transposed Matrix

**Input:** 
A: A 2d list as a matrix

**Output:** 
Returns a 2d matrix as the transpose of A

**Example**
Here is an example of running the code

```

testMatrix = [
        [2,2],
        [3,3],
        [4,4]
    ]
    #Testing a symmetric Matrix
    testMatrix2 = [
        [1,1,2],
        [1,2,3],
        [2,3,3]
    ]
    tranposed = matTranspose(testMatrix)
    print("Testing rectangular matrix")
    for row in tranposed:
        print(row)

    tranposed2 = matTranspose(testMatrix2)
    print("Testing Symmetric Matrix")
    for row in tranposed2:
        print(row)
```

This code prints out

```

Testing rectangular matrix
[2, 3, 4]
[2, 3, 4]
Testing Symmetric Matrix
[1, 1, 2]
[1, 2, 3]
[2, 3, 3]

```
**Implementation/Code:** 
Here is the implemenation for the routine.

```

def matTranspose(A):
    '''
    Transposes a 2D list storing a matrix
    :param A: The matrix to be transposed
    :return: A new transposed matrix
    '''
    numRows = len(A)
    numColumns = len(A[0])
    toReturn = [None] * numColumns
    for column in range(numColumns):
        newRow = []
        for row in range(numRows):
            newRow.append(A[row][column])
        toReturn[column] = newRow
    return toReturn
```
**Last Modified:** November/2020
