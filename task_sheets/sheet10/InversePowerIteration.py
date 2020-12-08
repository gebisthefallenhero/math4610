from MatVecMult import matVecMult
from L2Norm import l2Norm
from DotProd import dotProd
def inverPowIter(A,x_0,tol,maxIter=100):
    '''
    Returns the smallest eigenvalue of a matrix
    :param A: The input matrix
    :param x_0: The intial guess matrix
    :param tol: The tolerance for the vector norm
    :param maxIter: The santity check iterations
    :return: The smallest eigen value
    '''
    error = 10.0 * tol
    iter = 0
    l_0 = 0 #The lambda approximation

    while (error > tol and iter < maxIter):
        iter += 1
        z = matVecMult(A,y)
        normZ = l2Norm(z)
        w = [z[i] / normZ for i in range(len(z)) ]
        u = matVecMult(A,w)
        l_1 = dotProd(w,u)/dotProd(w,w)
        error = abs(l_1 - l_0)
        l_0 = l_1
        y = w
    return l_0