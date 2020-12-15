# Sheet 10 Solutions

### Task 1
See the file [PowerIteration.py](PowerIteration.py). Also see the software manual entry [here](../../SoftWare_Manual/PowerIter.md). I will post the code used below to test on the 100 x 100 matrix, which seemed to work fine. Also see the code [Sheet10Solutions.py](Sheet10Solutions.py)

```
if __name__ == '__main__':
    A = diagDomSymmetric(100)
    ones = [1 for i in range(100)]
    tol = .001
    print(powerIter(A,ones,tol))
```
This prints out the eigenvalue as 9984.309689714208

### Task 2
See the file[InversePowerIteration.py](InversePowerIteration.py). Also see the software manual entry [here](../../SoftWare_Manual/InversePowerIter.md). Again the code below is what was used to test and it seemed to work find. Also see the file referenced in Task 1.
```
if __name__ == '__main__':
    A = diagDomSymmetric(100)
    ones = [1 for i in range(100)]
    tol = .001
    print(inversePowerIter(A,ones,tol))
```
This prints out the smallest eigenvalue as 6978.534177924543

### Task 3
See the code [Matrix1Norm.py](Matrix1Norm.py) as well as the entry under vector and matrix norms in the [software manual](../../SoftWare_Manual/Table_of_Contents.md). Again see the file in task 1 for the testing of the code, but it seems to work fine.
Running the code give us
```buildoutcfg
The matrix one norm 9107.501940396867
```

### Task 4
See the code [matInftyNorm.py](matInftyNorm.py) as well as the entry under vector and matrix norms in the [software manual](../../SoftWare_Manual/Table_of_Contents.md) Again see the file in task 1 for the testing of the code, but it seems to work fine.
Running the code gives us
```buildoutcfg
The matrix infinty norm 10584.071266115827
```

### Task 5
See the code [ConditionNumber.py](CondtionNumber.py) as well as the sofware manual entry [here](../../SoftWare_Manual/ConditionNumber.md). Testing on the 100 x 100 matrix gives
```
The condition number is 1.2369546761056278
```

### Task 6 
One website defined a condition number as measuring the sensativity of a solution to small pertubations on input data. The bigger the condition number the more senitive it is. It also often came up that the condition number is not defined in terms of the eigenvalue of the matrix, but in terms of the singular values. The gives an alternative way to compute it. Addtionally I learned that the condition number is not an idea unique to numerical linear algebra, but it is also something used in most areas of numerical analysis. 

https://nhigham.com/2020/03/19/what-is-a-condition-number/
https://www.cmpe.boun.edu.tr/~cemgil/Courses/cmpe482/slides/Lecture12.pdf
http://www.ams.sunysb.edu/~jiao/teaching/ams526_fall12/lectures/lecture07.pdf
