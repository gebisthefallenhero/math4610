# Software Manual Table of Contents

## Error and Graphing

* [SinglePoint.md](SinglePoint.md) Calculates the single point precision of your computer.
* [DoublePoint.md](DoublePoint.md) Calculates the double point percision of your computer.
* [Graphing.md](Graphing.md) Takes in string representation of functions in python syntax to graph a function.
* [RelError.md](RelError.md) Returns the relative error of x - y.
* [AbsError.md](AbsError.md) Returns the absolute error of x-y.

## Root Finding Methods
* [FixedPoint.md](FixedPoint.md) Uses fixed point iteration to find the root of a function.
* [Bisection.md](Bisection.md) Uses the bisection method to find the root of a function.
* [NewtonsMethod.md](NewtonsMethod.md) Uses newtons method to find the root of a function.
* [SecantMethod.md](SecantMethod.md) Uses the secant method to find the root of a function.
* [HybridMethod.md](HybridMethod.md) Uses the a bisection-newton method to find the root of a function.
* [FindManyRoots.md](FindManyRoots.md) Uses a hybrid method to find as many roots as possible on an interval.

## Linear Algebra


### Solving Systems of Equations
* [BackSolve.md](BackSolve.md) Backsolve an upper triangular system of equations.
* [ForwardSolve.md](ForwardSolve.md) Forward Solve a lower triangular system of equations.
* [RowReduce.md](RowReduce.md) Perform Gaussian elimination on a matrix. No Pivoting Strategies implemented yet.
* [SystemSolve.md](SystemSolve.md) Solves a system of equations my doing a Gaussian elmination and then a back substitution. No pivoting strategies or dependencies on other routines.
* [LUFactorization.md](LUFactorization.md) Performs an inplace LU factorization on a matrix.
* [LUForwardSolve.md](LUForwardSolve.md) Does the forward solve of the lower part of an LU factorized matrix.
* [ScaledPartialPivoting.md](ScaledPartialPivoting.md) Solves a system of equations using scaled partial pivoting. If a solution exists, this will find it.


* [MatrixVectorMultiply.md](MatrixVectorMultiply.md) The multiplication of a matrix and a vector from the right.

### Vector Multiplication
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

### Misc
* [LinearRegression.md](LinearRegression.md) Perform a linear regression.
* [MatrixCreator.md](MatrixCreator.md) A suite of routines to create different types of matricies used for testing code.
* [Transpose.md](Transpose.md) Transpose a matrix
