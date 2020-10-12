
# Graphing 


**Routine Name:** plotFunction 

**Author:** Manuel Santana

**Language:** Python. This can be used with Python 3.8 with libraries matplot lib and numpy 



**Description/Purpose:** 
This program will plot a function or a list of functions on a single axis.


**Input:** 
fList : A list of functions to be passed in. A single function must be in list form

low, high. Upper and lower limits for values of the function. They default to -10, and 10.

This program can be run from the command line to plot multiple functions. For example

```

python x**2 (x+3x)/(x-2)

```
Functions passed in this way must follow python syntax. It uses the evil eval function and that is why.
Note: Currently will crash is a division by zero is tried. Do not let the interval low to high contain a part were the fuction is not defined.


**Output:** 
This will produce a png file of the graph you create that can be viewed and saved.


**Implementation/Code:** 

import matplotlib.pyplot as plt
import numpy as np

def plotFunction(fList, low = -10, high = 10):
    linspace = np.linspace(low, high)

    for f in fList:
        functVal = []
        for val in linspace:
            x = val
            functVal.append(eval(f))
        plt.plot(linspace, functVal)
    plt.legend(argv)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()
**Last Modified:** October/2020
