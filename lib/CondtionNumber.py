from Transpose import matTranspose
from MatMatMult import matMatMult
from math import sqrt
from PowerIteration import powerIter
from InversePowerIteration import inverPowIter
import math
def condNum(A):
    tol = .0001
    x_0 = [1 for i in range(len(A))]
    AtA = matMatMult(matTranspose(A),A)
    sigma1 = sqrt(powerIter(AtA,x_0,tol)[0])
    sigma2 = sqrt(inverPowIter(AtA,x_0,tol)[0])
    if sigma2 == 0:
        return math.inf
    return sigma1 / sigma2

if __name__ == '__main__':
    A = [
        [1,2,2],
        [4,-1,1],
        [-1,1,-1]
    ]
    print(condNum(A))

    