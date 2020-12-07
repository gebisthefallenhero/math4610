

# L Infinity Norm Norm

**Routine Name:** lInftyNorm

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Computes the L Infinity Norm of a vector

**Input:** 
v The vector to have the norm taken

**Output:** 
The scalar value from taking the norm

**Example**
Here is an example of running the code

```
if __name__ == "__main__":
    v = [1,2,3]
    print(lInftyNorm(v))
```

This code prints out

```
3
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
def lInftyNorm(v):
    '''
    v: The vector to have the norm returned.
    '''
    max = 0
    for i in range(len(v)):
        if abs(v[i]) > max:
            max = abs(v[i])
    return max

```
**Last Modified:** December/2020