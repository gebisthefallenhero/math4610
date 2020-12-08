from MatVecMult import matVecMult
from L2Norm import l2Norm
from DotProd import dotProd
def powerIter(A,x_0,tol,maxIter=1000):
    '''
    Returns the largest eigenvalue and vector of a matrix
    :param A: The input matrix
    :param x_0: The intial guess matrix
    :param tol: The tolerance for the vector norm
    :param maxIter: The santity check iterations
    :return: The largest eigen value and eigen vector as a tuple.
    '''
    error = 10.0 * tol
    iter = 0
    l_0 = 0 #The lambda approximation
    y = x_0
    while (error > tol and iter < maxIter):
        iter += 1
        z = matVecMult(A,y)
        normZ = l2Norm(z)
        w = [z[i] / normZ for i in range(len(z)) ]
        u = matVecMult(A,w)
        l_1 = dotProd(w,u)
        error = abs(l_1 - l_0)
        l_0 = l_1
        y = w
    return l_0,w

if __name__ == '__main__':
    A = [
        [0,1],
        [-2,-3]
    ]
    x_0 = [1,1]
    tol = .001
    print(powerIter(A,x_0,tol))