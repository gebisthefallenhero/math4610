# Sheet 4 Solutions

# Software Manual Link
Here is the link for the [software manual](../../SoftWare_Manual/Table_of_Contents.md)

### Task 1:
See the files [AbsError.py](AbsError.py) and [RelError.py](RelError.py)

### Task 2:
See the file [Graphing.py](Graphing.py)

### Task 3 - 4: 
See the file [FixedPoint.py](FixedPoint.py). Inorder to get this to converge to a root a took the derivative of the function and choose a point where the derivative stayed positive for the initial guess. This led to needing an epsilon of at least .01 in order to get convergence near 0. After some experiementing if we use an inital gues of .01 and and epsilon of -.01 we were able to find that the root is zero. This led also to updating the function to be able to pass in different values of epsilon.

### Task 5:
See the file [Bisection.py](Bisection.py)

### Task 6:
One interesting use for root finding methods is to compute quantiles of CDFs in statistics, as many CDFs do not have an analytical way to find a root. To do so you take a CDF, F(x) and set it equal to what percentage of your function you want to have the data below. For example F(x) = .7 for the 70th percentile. Then you just subtract to F(x) - .7 = 0. And there you go, a root finding problem.


[https://blogs.sas.com/content/iml/2018/02/19/compute-quantiles-distribution.html](https://blogs.sas.com/content/iml/2018/02/19/compute-quantiles-distribution.html)
