
# Matrix Scaling

**Routine Name:** matAdd

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Scales a matrix

**Input:** 
A The matrix
c The scalar to scal the matrix by.

**Output:** 
The matrix from the scaling

**Example**
Here is an example of running the code

```
if __name__ == "__main__":
    A = [
            [1, 2, 3,4],
            [4,5,6,7],
            [7,8,9,10]
            ]
    c = 2
    print(matScal(A,c))
```

This code prints out

```
[[2, 4, 6, 8], [8, 10, 12, 14], [14, 16, 18, 20]]
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
def matScal(A,c):
    '''
    A The matrix to the multiplied
    c The scalar to mulitply it by
    '''
    for i in range(len(A)):
        for j in range(len(A[0])): #In the case that A is a rectangular matrix
            A[i][j]= A[i][j] * c 
    return A
```
**Last Modified:** December/2020