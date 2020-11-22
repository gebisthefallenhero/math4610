from LUFactorization import LUForwardSolve,LUFact
from BackSolve import backSolve
from MatrixVectorMultiply import matVecMult
def printMatrix(A):
    for row in A:
        print(row)


def hilbertMatrix(size):
    '''
    Creates a hilbertMatix of size by size
    :param size: The size of the matrix to be created
    :return: A hilbert matrix
    '''
    mat = []
    for i in range(1,size + 1):
        row = []
        for j in range(size):
            row.append(1 / (i + j))
        mat.append(row)
    return mat

if __name__ == '__main__':
    b = [1,1,1]
    for i in range(4,12):
        b.append(1)
        A = hilbertMatrix(i)
        solVec = matVecMult(A,b)
        A = LUFact(A)
        c = LUForwardSolve(A,solVec)
        finalAnswer = backSolve(A,c)
        print(f'The vector for a hilbert matrix of size {i} is \n {finalAnswer}')