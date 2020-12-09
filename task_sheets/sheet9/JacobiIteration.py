from MatVecMult import matVecMult
from L2Norm import l2Norm
def jacobiIteration(A,x_0,b,tol,maxIter=1000):
    '''
    Performs the Jacobi Iteration using the residual update method.
    A The matrix to be solved over
    x_0 The inital guess vector
    b The vector on the right side of the equation
    tol The tolerance to be run to
    maxIter The max number of iterations.
    '''
    error = tol * 10
    length = len(A)
    x_old = [x_0[i] for i in range(len(x_0))]
    x_new = [b[i] for i in range(len(b))]
    res = [0 for i in range(length)]
    iter = 0
    while (error > tol and iter < maxIter):
        iter += 1
        for i in range(length):
            res[i] = b[i]
            for j in range(length):
                res[i] = res[i] - A[i][j] * x_old[j]
        for i in range(length):
            x_new[i] = x_old[i] + res[i] / A[i][i]
        error = l2Norm(res)
        x_old = x_new
    return x_new

if __name__ == '__main__':
    A = [
        [4,-2,1],
        [1,-3,2],
        [-1,2,6]
    ]
    b = [1,2,3]
    x_0 = [0, 0, 0]
    tol = .001
    print(jacobiIteration(A,x_0,b,tol))



