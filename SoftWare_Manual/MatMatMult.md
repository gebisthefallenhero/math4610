
# Matrix Matrix Mulitplication

**Routine Name:** matMatMult

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Mutliplies two matricies, it is up to the user to check the dimension.

**Input:** 
A,B the matrices to be multiplied

**Output:** 
The matrix from the multiplication

**Example**
Here is an example of running the code

```
if __name__ == "__main__":
    A = [
            [0,2],
            [0,1],
            [0,0]
        ]

    B = [
            [1,2,3],
            [4,5,6],
        ]
            
    print(matMatMult(A,B))


```

This code prints out

```
[[0, 1, 2], [2, 3, 4], [4, 5, 6]]
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
def matSub(A,B):
    '''
    A,B the matricies to be subtracted in the order A - B 
    '''
    for i in range(len(A)):
        for j in range(len(B)):
            A[i][j]= A[i][j] - B[i][j]
    return A
```
**Last Modified:** December/2020