
# Linear Regression 


**Routine Name:** linearRegression 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 or higher.


**Description/Purpose:** 
This program returns the slope and itercept of data points using a linear regression.

**Input:** 
x,y numeric type array. These are arrays containing the data ponits. Both arrays must be the same size.

**Output:** 
Returns a tuple (a,b) where a is the intercept and b is the slope.

**Example**
The following is code used to text the function.

```
if __name__ == "__main__":
    #Driver program with test vectors.
    x = [2,3,5,7,9]
    y = [4,5,7,10,15]
    print(linearRegression(x,y))
```
This code prints out

```
(0.3048780487804878, 1.5182926829268293)
```


**Implementation/Code:** 
Here is the implemenation for the routine.

```
def linearRegression(x,y):
    if len(x) != len(y):
        print("The length of the vectors do not match for regression")
        return
    #initialize the values in A^TA
    a11 = len(x)
    a12 = 0
    a22 = 0
    #Now the values in A^T y
    b1 = 0
    b2 = 0
    for i in range(len(x)):
        a12 += x[i]
        a22 += x[i] * x[i]
        b1 += y[i]
        b2 += y[i] * x[i]
    #Solve the 2x2 system.
    det = a11 * a22 - a12 * a12
    c1 = (a22 * b1 - a12 * b2) / det
    c2 = (a11 * b2 - a12 * b1) / det
    return c1,c2

```
**Last Modified:** October/2020
