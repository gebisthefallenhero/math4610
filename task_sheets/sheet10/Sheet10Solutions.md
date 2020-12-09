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
See the code [matInftyNorm.py](matInfty1Norm.py) as well as the entry under vector and matrix norms in the [software manual](../../SoftWare_Manual/Table_of_Contents.md)
