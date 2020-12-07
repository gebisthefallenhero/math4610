
# Vector Dot Product

**Routine Name:** dotProd 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Computes the dot product of two vectors

**Input:** 
v,w the two vectors to have the dot product taken v^t w

**Output:** 
Returns the scalar from the dot product

**Example**
Here is an example of running the code

```
if __name__ == "__main__":
    v = [1,2,3]
    w = [2,3,1]
    print(dotProd(v,w))
```

This code prints out

```
11
```
**Implementation/Code:** 
Here is the implemenation for the routine.
```
def dotProd(v,w):
    '''
    v,w the two vectors to be multiplied 
    '''
    sum = 0
    for i in range(len(v)):
        sum += v[i] * w[i]
    return sum
```
**Last Modified:** December/2020