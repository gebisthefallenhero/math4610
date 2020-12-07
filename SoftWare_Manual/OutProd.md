
# Outer Product

**Routine Name:** outerProd

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Computes the out product of two vectors

**Input:** 
v,w the two vectors to have the dot product taken v w^T

**Output:** 
The matrix from the outer product.

**Example**
Here is an example of running the code

```
if __name__ == "__main__":
    v = [1,2,3]
    w = [2,3,1]
    print(outerProd(v,w))
```

This code prints out

```
[[2, 3, 1], [4, 6, 2], [6, 9, 3]]
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
def outerProd(v,w):
    '''
    v,w the two vectors to be multiplied 
    Returns a matrix from the outer product.
    '''
    matrix = []
    for i in range(len(v)):
        matrix.append([w[j] * v[i] for j in range(len(v))])
    return matrix
```
**Last Modified:** December/2020