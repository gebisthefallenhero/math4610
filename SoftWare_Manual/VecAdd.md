
# Vector Addition 

**Routine Name:** vecAdd

**Author:** Manuel Santana


**Language:** Python. This can be used with Python 3.8 or higher. 

**Description/Purpose:** 
Adds two vectors

**Input:** 
v,w the two vectors to be added

**Output:** 
Returns the vector from the addition

**Example**
Here is an example of running the code

```
if __name__ == "__main__":
    v = [1,2,3]
    w = [2,3,1]
    print(vecAdd(v,w))
```

This code prints out

```
[3, 5, 4]
```
**Implementation/Code:** 
Here is the implemenation for the routine.

```
def vecAdd(v,w):
    '''
    v,w the two vectors to be added
    '''
    return [v[i] + w[i] for i in range(len(v))]

```
**Last Modified:** December/2020
