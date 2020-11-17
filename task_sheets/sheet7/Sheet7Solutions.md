# Task Sheet 7 Solutions

Here is a link to the software manual for the back substitution, forward substitution, matrix creation, and row reduction. [software manual](../../Software_Manual/Table_Of_Contents.md)

### Task 1
The code for the back substitution can be found in [BackSolve.py](BackSolve.py) The upper triangluar matrix routine was performed in [Sheet7Tasks.py](Sheet7Tasks.py). Note that this version of creating an upper triangular matrix is different than the one described in task 3. Testing the code on a 3x3 matrix outputs

```
Printing U
[-1, 0, 1]
[0, 1, 2]
[0, 0, 3]
Solution with b as 1's vector
[-0.6666666666666667, 0.33333333333333337, 0.3333333333333333]
```

### Task 2
The code for the forward substitution can be found in [ForwardSolve.py](ForwardSolve.py). The code for the transpose can be found in [Transpose.py](Transpose.py). Running this test output

```
Printing U^T
[-1, 0, 0]
[0, 1, 0]
[1, 2, 3]
Solution with b as 1's vector.
[-1.0, 1.0, 0.0]
```


### Tasks 3 -4
The code for these task is in the file [MatrixCreator.py](MatrixCreator.py) and the software manual entry for this suite can be found from the [table of contents](../../SoftWare_Manual/Table_Of_Contents.md) under the linear algebra section.


### Task 5
For the code for row reducting see [RowReduce.py](RowReduce.py). Using the driver program in [Sheet7Tasks.py](Sheet7Tasks.py) the code output the following with a random matrix

```
Random Square Matrix
[60, 74, 13]
[10, 94, 53]
[94, 27, 35]
Random b vector
[87, 83, 76]
Matix Reduced
[60, 74, 13]
[0.0, 81.66666666666667, 50.833333333333336]
[0.0, 0.0, 69.98979591836735]
Reduced b vector
[87, 68.5, 14.295102040816317]
```




