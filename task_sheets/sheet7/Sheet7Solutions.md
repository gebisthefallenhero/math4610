# Task Sheet 7 Solutions

Here is a link to the software manual for the back substitution, forward substitution, matrix creation, and row reduction. [software manual](../../SoftWare_Manual/Table_of_Contents.md)

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
The code for these task is in the file [MatrixCreator.py](MatrixCreator.py) and the software manual entry for this suite can be found from the [table of contents](../../SoftWare_Manual/Table_of_Contents.md) under the linear algebra section.


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
### Task 6
The first thing I looked up is stuff about the condition number. Essentially the condition number helps to know how a small pertubation affects the entire matrix. If the condition number is large, then the matrix is close to singular, and could cause trouble. The other main thing discussed was that even when a matrix is non-singular if it has small pivots then the matrix can appear singular. As talked about in class it is often metioned that a pivoting strategy is needed in this case.

[https://blogs.mathworks.com/cleve/2017/07/17/what-is-the-condition-number-of-a-matrix/](https://blogs.mathworks.com/cleve/2017/07/17/what-is-the-condition-number-of-a-matrix/)

[http://ranger.uta.edu/~huber/cse4345/Notes/Linear_Equations.pdf](http://ranger.uta.edu/~huber/cse4345/Notes/Linear_Equations.pdf)

