from PowerIteration import powerIter
from random import randint
def diagDomSymmetric(size):
    '''
    Creates a diagonal domiant random matrix symmetric
    :param size The size of the matrix.
    :return: The random matrix
    '''
    START_VALUE = 0
    END_VALUE = 20
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
    A = diagDomSymmetric(100)
    ones = [1 for i in range(100)]
    tol = .001
    print(powerIter(A,ones,tol))