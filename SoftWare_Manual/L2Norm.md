
# L2 Norm

**Routine Name:** l2Norm

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Computes the L2 Norm of a vector

**Input:** 
v The vector to have the norm taken

**Output:** 
The scalar value from taking the norm

**Example**
Here is an example of running the code

```
if __name__ == "__main__":
    v = [1,2,3]
    print(l2Norm(v))
```

This code prints out

```
3.7416573867739413
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
from math import sqrt
def l2Norm(v):
    '''
    v: The vector to have the norm returned.
    '''
    sum = 0
    for i in range(len(v)):
        sum += v[i] * v[i]
    return sqrt(sum)

```
**Last Modified:** December/2020