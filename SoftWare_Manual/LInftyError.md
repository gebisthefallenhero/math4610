
# L Infinity Error Norm

**Routine Name:** lInftyError

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Computes the L Infinity Norm of the difference of two vectors

**Input:** 
v,w The vectors to have the norm taken

**Output:** 
The scalar value from taking the norm

**Example**
Here is an example of running the code

```
if __name__ == "__main__":
    v = [1,2,3]
    w = [-1, -2, -3]
    print(lInftyError(v,w))

```

This code prints out

```
6
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
def lInftyError(v,w):
    '''
    Computes the infinity norm of v - w.
    '''
    max = 0
    for i in range(len(v)):
        val = abs(v[i] - w[i])
        if val > max:
            max = val
    return max
```
**Last Modified:** December/2020