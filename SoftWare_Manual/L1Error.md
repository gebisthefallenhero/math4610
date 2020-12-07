
# L1 Error Norm

**Routine Name:** l1Error

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Computes the L1 Norm of the difference of two vectors

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
    print(l1Error(v,w))
```

This code prints out

```
12
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
def l1Error(v,w):
    '''
    Computes the norm of v - w.
    '''
    sum = 0
    for i in range(len(v)):
        sum += abs(v[i] - w[i])
    return sum
```
**Last Modified:** December/2020