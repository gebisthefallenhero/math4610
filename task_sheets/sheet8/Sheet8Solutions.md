# Sheet 8 Solutions

Link to the [software manual](../../SoftWare_Manual/Table_of/Contents.md)

### Task 1
See the code for the solving the system in [GaussianSolution.py](GaussianSolution.py). For the code to create a diagonally dominate matrix see the file [MatrixCreator.py](../../lib/MatrixCreator.py) For the software manual entry see [SystemsSolver.md](../../SoftWare_Manual/SystemsSolver.md). 

### Task 2
See the code for this in [LUFactorization.py](LUFactorization.py). Also see the software manual entry for this found [here](../../SoftWare_Manual/LUFactorization.md) and [here](../../SoftWare_Manual/LUFactorization.md).

### Task 3
For the code for this see [Solutions.py](Solutions.py). This did not go very well in any of the cases. As an example here is the solution vector for the hilbert matrix of size 5
```
 [2.122109175659351, 0.30630116952138, 0.023403554016844637, 0.0010714123744737227, 2.2675736961437834e-05]
```
That is not close at all to the all ones vector, so we will need better tools. The results for the larger Hilbert Matrices are similar.

### Task 4
After much reading up on how the method works, lots of debugging, and a few grey hairs the fully functional code for scaled partial pivoting can be found [ScaledPartialPivoting.py](ScaledPartialPivoting.py). The entry for the software manual can be found [here](../../SoftWare_Manual/LUFactorization.md). 


### Task 5
Running the code on the 4x4 Hilbert Matrix we find the solution of

```
The vector for a Hilbert Matrix of size 4 using Scaled Partial Pivoting is 
 [0.9999999999999758, 1.000000000000269, 0.999999999999351, 1.0000000000004226]
```
This is much closer to the all ones vector. Happy day. For Hilbert Matrices of size 5 - 10 run the code in the solutions file mentioned in task 3. The results are similar as the 4x4 case.


