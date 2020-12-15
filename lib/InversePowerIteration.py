from L2Norm import l2Norm
from DotProd import dotProd
from ScaledPartialPivoting import scaledPartPiv
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
    y = x_0
    while (error > tol and iter < maxIter):
        v = scaledPartPiv(A,y)
        normV = l2Norm(v)
        v = [v[i] / normV for i in range(len(v))]
        z = scaledPartPiv(A,v)
        l_1 = dotProd(v,z)
        error = abs(l_1 - l_0)
        l_0 = l_1
        y = v
        iter += 1
    return 1/l_0,z

if __name__ == '__main__':
    A = [
        [0,1],
        [-2,-3]
    ]
    x_0 = [1,1]
    tol = .001
    print(inverPowIter(A,x_0,tol))
