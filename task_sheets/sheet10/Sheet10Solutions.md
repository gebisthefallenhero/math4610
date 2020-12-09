# Sheet 10 Solutions

### Task 1
See the file [PowerIteration.py](PowerIteration.py). Also see the sofware entry [here](../../SoftWare_Manual/PowerIter.py). I will post the code used below to test on the 100 x 100 matrix, which seemed to work fine. Also see the code [Sheet10Solutions.py](Sheet10Solutions.py)

```
if __name__ == '__main__':
    A = diagDomSymmetric(100)
    ones = [1 for i in range(100)]
    tol = .001
    print(powerIter(A,ones,tol))
```

### Task 2

### Task 3
See the code [Matrix1Norm.py](Matrix1Norm.py) as well as the entry under vector and matrix norms in the [software manual](../../SoftWare_Manual/Table_of_Contents.md)

### Task 4
See the code [matInftyNorm.py](matInftyNorm.py) as well as the entry under vector and matrix norms in the [software manual](../../SoftWare_Manual/Table_of_Contents.md)

### Task 5

### Task 6 
One website defined a condition number as measuring the sensativity of a solution to small pertubations on input data. The bigger the condition number the more senitive it is. It also often came up that the condition number is not defined in terms of the eigenvalue of the matrix, but in terms of the singular values. Thi gives an alternative way to compute it.

https://nhigham.com/2020/03/19/what-is-a-condition-number/
https://www.cmpe.boun.edu.tr/~cemgil/Courses/cmpe482/slides/Lecture12.pdf
http://www.ams.sunysb.edu/~jiao/teaching/ams526_fall12/lectures/lecture07.pdf
