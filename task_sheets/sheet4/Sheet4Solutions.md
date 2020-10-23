# Sheet 4 Solutions

### Task 1:
See the files [AbsError.py](AbsError.py) and [RelError.py](RelError.py)

### Task 2:
See the file [Graphing.py](Graphing.py)

### Task 3 - 4: 
See the file [FixedPoint.py](FixedPoint.py). Inorder to get this to converge to a root a took the derivative of the function and choose a point where the derivative stayed positive for the initial guess, and then experimented with differentvalues of epsilon. Eventually the one that ended up working is epslion = .001 converged to the root -.805 using the inital guess of .001.

### Task 5:
See the file [Bisection.py](Bisection.py)

### Task 6:
One interesting use for root finding methods is to compute quantiles of CDFs in statistics, as many CDFs do not have an analytical way to find a root. To do so you take a CDF, F(x) and set it equal to what percentage of your function you want to have the data below. For example F(x) = .7 for the 70th percentile. Then you just subtract to F(x) - .7 = 0. And there you go, a root finding problem.


[https://blogs.sas.com/content/iml/2018/02/19/compute-quantiles-distribution.html](https://blogs.sas.com/content/iml/2018/02/19/compute-quantiles-distribution.html)
