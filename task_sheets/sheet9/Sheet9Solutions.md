# Sheet9 Solutions

For all tasks see the [table of contents](../../SoftWare_Manual/Table_of_Contents.md) of the software manual for the software manual entries.

### Task 1
* [vector addition](VecAdd.py)
* [vector subtraction](VecSub.py)
* [Scalar Multiplication](ScalMult.py)
* [Dot Product](DotProd.py)
* [Outer Product](OuterProd.py)

### Task 2
* [L1 Norm](L1Norm.py)
* [L2 Norm](L2Norm.py)
* [Infinity Norm](LinftyNorm.py)
* [L1 vec difference](L1Error.py)
* [L2 vec difference](L2Error.py)
* [Infinity vec difference](LInftyError.py)

### Task 3
* [Matrix Addition](MatAdd.py)
* [Matrix Subtraction](MatSub.py)
* [Matrix times a scalar](MatScal.py)
* [Matrix Transpose](../sheet7/Transpose.py)
* [Matrix Vector left multiplication](MatVecMult.py)
* [Matrix Matrix Multiplication](MatMatMult.py)

### Task 4
For the code see [JacobiIteration.py](JacobiIteration.py). For the software manual entry look [here](../../SoftWare_Manual/Jacobi.md)

### Task 5
For the code see [here](Sheet9Solutions.py). This is what the code printed out
```
The Jacobi error is 0.34243385020750805 and the backSub error is 8.150882121683646e-15

```
Clearly the back subsitution does a much better job, but the Jacobi error isn't bad either.


### Task 6
First I looked at Gauss-Seidel iteration which looks just like Jacobi only it seperates A into L and U with U a stricly upper triangular matrix. According to one research article I read the biggest difference between the two methods is that the in the Gauss-Seidel iteration instead of always using the previous iteration 'whenever an updated value become avaliable it is immediately used'. (see the second source). This seems to be useful when using approximating 2D PDE's using iterative finite difference methods.

https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method
https://www.sciencedirect.com/topics/engineering/gauss-seidel-method#:~:text=The%20difference%20between%20the%20Gauss,as%20demonstrated%20in%20Table%207.2.

