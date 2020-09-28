# Single Point

**Routine Name:** DoublePoint 

**Author:** Manuel Santana

**Language** Java. This can be compiled and ran using JDK 13.01 or higher.

For example,

    java DoublePoint.java 


**Description/Purpose:** This routine will compute the double precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

**Input:** 
There are no inputs needed here.

**Output:** This routine returns a double precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

By using the function calcDoublePoint() you will print out the number of binary digits that can be represented on the computer using single point precision. 
Here is an example main class

```
    public static void main(String[] args){
        double numBinaryDigits = calcDoublePoint();
        System.out.println("The number of binary digits that can be printed is " + calcDoublePoint());
        System.out.println("The smallest number this corresponds to is " + Math.pow(2,-numBinaryDigits));
    }

```


Output from the lines above:

The number of binary digits that can be printed is 53.0
The smallest number this corresponds to is 1.1102230246251565E-16

The first value (53) is the number of binary digits that define the machine epsilon and the second is related to the
decimal version of the same value. The number of decimal digits that can be represented is roughly eight (E-16 on the
end of the second value).

**Implementation/Code:** The following is the code for calcDoublePoint()

public class DoublePoint {
    /*
    Returns the number of binary digits that can be printed from single point percision.
     */
    public static float calcDoublePoint(){
        double one = 1;
        double seps = 1;
        double appone = one + seps;
        for( int ipow = 1; ipow <= 1000; ipow++){

            seps = seps / 2;
            appone = 1 + seps;
            if (Math.abs(appone) == 1){
                return ipow;
            }
        }
        System.out.print("Did not make it after 1000 iterations");
        return 0;
    }

**Last Modified:** September/2020

