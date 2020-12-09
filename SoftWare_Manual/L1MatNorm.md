
# Matirx Norm

**Routine Name:** mat1Norm

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Computes the 1 Norm of a matrix 

**Input:** 
A The matrix to have the norm taken

**Output:** 
The scalar value from taking the norm

**Example**
Here is an example of running the code

```
if __name__ == '__main__':
    A = [
        [1,2,3],
        [1,2,3],
        [1,2,3],
        [1,2,3],
        [1,2,3]
    ]
    print(mat1Norm(A))
```

This code prints out

```
15
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
def mat1Norm(A):
    '''
    Computes the 1 Norm of a matrix
    :param A:
    :return: the maximum column sum
    '''
    numCols = len(A[0])
    lenCols = len(A)
    max = 0
    for i in range(numCols):
        sum = 0
        for j in range(lenCols):
            sum += abs(A[j][i])
        if sum > max:
            max = sum
    return max
```
**Last Modified:** December/2020
