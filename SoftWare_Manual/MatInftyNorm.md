

# Matrix Infinity Norm 

**Routine Name:** matInftyNorm 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Computes the Infinity Norm of a matrix 

**Input:** 
A The Matrix to have the norm taken

**Output:** 
The scalar value from taking the norm

**Example**
Here is an example of running the code

```
if __name__ == '__main__':
    A = [
        [1,1,1,1,1,1,1],
        [2,2,2,2,2,2,2],
        [3,3,3,3,3,3,3]
    ]
    print(matInftyNorm(A))
```

This code prints out

```
21
```
**Implementation/Code:** 
Here is the implemenation for the routine.

```
def matInftyNorm(A):
    '''
    Computes the Infinity Norm of a matrix
    :param A:
    :return: the maximum row sum
    '''
    lenRows = len(A[0])
    numRows = len(A)
    max = 0
    for i in range(numRows):
        sum = 0
        for j in range(lenRows):
            sum += abs(A[i][j])
        if sum > max:
            max = sum
    return max
```
**Last Modified:** December/2020
