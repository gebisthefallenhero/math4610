
# Matrix Addition

**Routine Name:** matAdd

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Adds two matricies

**Input:** 
A,B the matrices to be added

**Output:** 
The matrix from the addition

**Example**
Here is an example of running the code

```
if __name__ == "__main__":
    A = [
            [1, 2, 3],
            [4,5,6],
            [7,8,9]
            ]
    B = [
            [1,1,1],
            [2,2,2],
            [3,3,3]
            ]
    print(matAdd(A,B))
```

This code prints out

```
[[2, 3, 4], [6, 7, 8], [10, 11, 12]]
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
def matAdd(A,B):
    '''
    A,B the matricies to be added
    '''
    for i in range(len(A)):
        for j in range(len(B)):
            A[i][j]= A[i][j] + B[i][j]
    return A
```
**Last Modified:** December/2020