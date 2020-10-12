# Single Point

**Routine Name:** DoublePoint 

**Author:** Manuel Santana

**Language** Python. This can be ran with python 3.8 or higher with a numpy dependance

For example,

	python DoublePoint.py

**Description/Purpose:** This routine will compute the double precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

**Input:** 
There are no inputs needed here.

**Output:** This routine returns a double precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

By using the function DoublePoint() you will print out the number of binary digits that can be represented on the computer using single point precision. 
Here is an example main class

```

if __name__ == "__main__":
    print(f"The number of binary digits that can be printed is {doublePoint()}")
    print(f"The smallest number this corresponds to is {2 ** -doublePoint()}")

```


Output from the lines above:

The number of binary digits that can be printed is 53.0
The smallest number this corresponds to is 1.1102230246251565E-16

The first value (53) is the number of binary digits that define the machine epsilon and the second is related to the
decimal version of the same value. The number of decimal digits that can be represented is roughly eight (E-16 on the
end of the second value).

**Implementation/Code:** The following is the code for calcDoublePoint()

```
def singlePoint():
    one = float32(1.0)
    seps = float32(1.0)
    appone = float32(1.0)
    for ipow in range(1, 1000):
        seps = seps / 2
        seps = float32(seps)
        appone = one + seps
        if (abs(appone) == 1):
            return ipow
    print("Didn't make it after 1000 Iterations")

```
**Last Modified:** September/2020

