from Transpose import matTranspose
from MatMatMult import matMatMult
from math import sqrt
from PowerIteration import powerIter

def condNum(A):
    x_0 = [1 for i in range(len(A))]
    AtA = matMatMult(matTranspose(A),A)
    r1 = sqrt(powerIter(AtA,x_0))
    