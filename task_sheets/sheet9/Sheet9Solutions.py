from random import randint
from MatVecMult import matVecMult
from JacobiIteration import jacobiIteration
from ScaledPartialPivoting import scaledPartPiv
from L2Error import l2Error
def diagDomSymmetric(size):
    '''
    Creates a diagonal domiant random matrix symmetric
    :param size The size of the matrix.
    :return: The random matrix
    '''
    START_VALUE = 1
    END_VALUE = 5
    matrix = []
    #initialize a random matrix
    for i in range(size):
        row = []
        for j in range(size):
            row.append(randint(START_VALUE,END_VALUE))
        matrix.append(row)
    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = matrix[j][i]
    #Force diagonal dominance upon that matrix
    for i in range(size):
        sum = 0
        for j in range(size):
            if (j != i):
                sum += matrix[i][j]
        matrix[i][i] = sum + 1
    return matrix

if __name__ == '__main__':
    size = 100
    ones = [1 for i in range(100)]
    A = diagDomSymmetric(100)
    b = matVecMult(A,ones)
    x_0 = [0 for i in range(100)]
    jacobiGuess = jacobiIteration(A,x_0,b,.00001)
    scaledGuess = scaledPartPiv(A,b)
    jacobiError = l2Error(ones,jacobiGuess)
    scaledError = l2Error(ones,scaledGuess)
    print(f"The Jacobi error is {jacobiError} and the backSub error is {scaledError}")