
# Vector Scalar Multiplication

**Routine Name:** scalMult

**Author:** Manuel Santana


**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Multiplies a Vector and a Scalar

**Input:** 
v The vector
c the Scalar

**Output:** 
Returns the vector after the scalar multiplication

**Example**
Here is an example of running the code

```
if __name__ == "__main__":
    v = [1,2,3]
    c = 3
    print(scalMult(v,c))
```

This code prints out

```
[3, 6, 9]
```
**Implementation/Code:** 
Here is the implemenation for the routine.

```
def scalMult(v,c):
    '''
    v the vector
    c the scalar
    '''
    return [v[i] * c for i in range(len(v))]
```
**Last Modified:** December/2020