# Sheet 8 Solutions

Link to the [software manual](../../SoftWare_Manual/Table_of_Contents.md)

### Task 1
See the code for the solving the system in [GaussianSolution.py](GaussianSolution.py). For the code to create a diagonally dominate matrix see the file [MatrixCreator.py](../../lib/MatrixCreator.py) For the software manual entry see [SystemsSolver.md](../../SoftWare_Manual/SystemsSolve.md). 

### Task 2
See the code for this in [LUFactorization.py](LUFactorization.py). Also see the software manual entry for this found [here](../../SoftWare_Manual/LUFactorization.md) and [here](../../SoftWare_Manual/LUFactorization.md).

### Task 3
For the code for this see [Solutions.py](Solutions.py). This did not go very well in any of the cases. As an example here is the solution vector for the hilbert matrix of size 5
```
 [2.122109175659351, 0.30630116952138, 0.023403554016844637, 0.0010714123744737227, 2.2675736961437834e-05]
```
That is not close at all to the all ones vector, so we will need better tools. The results for the larger Hilbert Matrices are similar.

### Task 4
After much reading up on how the method works, lots of debugging, and a few grey hairs the fully functional code for scaled partial pivoting can be found [ScaledPartialPivoting.py](ScaledPartialPivoting.py). The entry for the software manual can be found [here](../../SoftWare_Manual/ScaledPartialPivoting). 


### Task 5
Running the code on the 4x4 Hilbert Matrix we find the solution of

```
The vector for a Hilbert Matrix of size 4 using Scaled Partial Pivoting is 
 [0.9999999999999758, 1.000000000000269, 0.999999999999351, 1.0000000000004226]
```
This is much closer to the all ones vector. Happy day. For Hilbert Matrices of size 5 - 10 run the code in the solutions file mentioned in task 3. The results are similar as the 4x4 case.

### Task 6
Interestingly enough the first site I visited mentioned that a distinguishing charcteristic of the Hilbert Matrix is that it is difficult to invert via numerical techniques. Indeed another site mentioned that the condition number of this matrix grows very quickly with the size of the matrix. Interestly enough there is an explicit formula for element of the inverse of a Hilbert Matrix, but it is a little complicated, and it is probably better just to do scaled partial pivotingto compute the action of the inverse on a vector. 

https://mathworld.wolfram.com/HilbertMatrix.html
https://nhigham.com/2020/06/30/what-is-the-hilbert-matrix/
