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
* [Jacobi Iteration](Jacobi.md) Solves a system of equations using jacobi iteration.

### Vector Multiplication
* [vector addition](VecAdd.md) Adds two vectors.
* [vector subtraction](VecSub.md) Subtracts two vectors.
* [Scalar Multiplication](ScalMult.md) Multiply a vector by a scalar.
* [Dot Product](DotProd.md) Pefroms the dot product of two vectors.
* [Outer Product](OuterProd.md) Performs the outer product of two vectors.

### Vector and Matrix Norms
* [L1 Norm](L1Norm.md) Calculate the L1 Norm of a vector.
* [L2 Norm](L2Norm.md) Calculate the L2 Norm of a vector.
* [Infinity Norm](Linfty.md) Calulate the infinity norm of a vector.
* [L1 vec difference](L1Error.md) Calculate the L1 Norm of the difference of two vectors.
* [L2 vec difference](L2Error.md) Calculate the L2 Norm of the difference of two vectors.
* [Infinity vec difference](LInftyError.md) Calculat the Infinity Norm of the difference of two vectors.
* [Matrix 1 Norm](L1MatNorm.md) Calculates the 1 norm of a matrix.
* [Matrix Infinity Norm](MatInftyNorm.md) Calculates the maximum norm of a matrix.

### Matrix Operations
* [Matrix Addition](MatAdd.md) Adds two matrices.
* [Matrix Subtraction](MatSub.md) Subtract two matrices.
* [Matrix times a scalar](MatScal.md) Scale a matrix.
* [Transpose.md](Transpose.md) Transpose a matrix
* [MatrixVectorMultiply.md](MatrixVectorMultiply.md) The multiplication of a matrix and a vector from the right.
* [Matrix Matrix Multiplication](MatMatMult.md) Multiply two matricies. 



### EigenValues
* [PowerMethod.md](PowerIter.md) Returns the largest eigenvalue.

### Misc
* [LinearRegression.md](LinearRegression.md) Perform a linear regression.
* [MatrixCreator.md](MatrixCreator.md) A suite of routines to create different types of matricies used for testing code.
