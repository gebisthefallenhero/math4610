# Sheet 4 Solutions

### Task 1:
See the files [AbsError.py](AbsError.py) and [RelError.py](RelError.py)

### Task 2:
See the file [Graphing.py](Graphing.py)

### Task 3 - 4: 
See the file [FixedPoint.py](FixedPoint.py)

## Task 5:
See the file [Bisection.py](FixedPoint.py)

### Task 6:
One interesting use for root finding methods is to compute quantiles of CDFs in statistics, as many CDFs do not have an analytical way to find a root. To do so you take a CDF, F(x) and set it equal to what percentage of your function you want to have the data below. For example F(x) = .7 for the 70th percentile. Then you just subtract to F(x) - .7 = 0. And there you go, a root finding problem.


[https://blogs.sas.com/content/iml/2018/02/19/compute-quantiles-distribution.html](https://blogs.sas.com/content/iml/2018/02/19/compute-quantiles-distribution.html)
