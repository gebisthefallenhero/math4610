
# Matrix Vector Multiplication 

**Routine Name:** matVectMult 

**Author:** Manuel Santana


**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Multiplies a matrix and a vector using the dot product of the rows of the matrix with the vector.

**Input:** 
A: The matrix to be multiplied.
v: The vector to be multiplied.

**Output:** 
Returns the vector from the mulitplication.

**Example**
Here is an example of running the code

```
    matrix = [
        [1,2],
        [3,4]
    ]
    vec = [3,4]
    print(matVecMult(matrix,vec))
```

This code prints out

```
[11, 25]
```
**Implementation/Code:** 
Here is the implemenation for the routine.

```
def matVecMult(A,v):
    '''
    Multiplies a matrix and a vector from the right
    :param A: the matrix to be multiplied
    :param v: the vector to be multiplied
    :return: the new vector
    '''
    numRows = len(A)
    vecLength = len(v)
    newVec = []
    for row in range(numRows):
        sum = 0
        for entry in range(vecLength):
            sum += vec[entry] * A[row][entry]
        newVec.append(sum)
    return newVec
```
**Last Modified:** November/2020
