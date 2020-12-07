
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
[[8, 10, 12], [4, 5, 6], [0, 0, 0]]
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
def matMatMult(A,B):
    '''
    A,B The matricies to be multiplied as A * B 
    Checking dimensions is left to user.
    '''
    toReturn = []
    for k in range(len(A)):
        newRow = []
        for i in range(len(A)): #
            sum = 0
            for j in range(len(B)): # For the number of entries in a column of B
                sum += A[k][j] * B[j][i]
            newRow.append(sum)
        toReturn.append(newRow)
    return toReturn
```
**Last Modified:** December/2020