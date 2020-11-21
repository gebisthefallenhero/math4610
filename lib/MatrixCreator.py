from random import randint

def printMatrix(matrix):
    for row in matrix:
        print(row)

def squareMatrix(size):
    '''
    Returns a random matrix of size n X n with random intergers between 1 and 100
    :param size: The number of rows and columns of your matrix
    :return: An nxn matrix
    '''
    matrix = []
    for j in range(size):
        matrix.append([])
        for i in range(size):
            matrix[j].append(randint(0,100))
    return matrix

def upTriMat(size):
    '''
    Returns a random upper triangular matrix of size n X n with random intergers between 1 and 100
    :param size: The number of rows and columns of your matrix
    :return: An nxn upper triangular matrix
    '''
    matrix = []
    for j in range(size):
        matrix.append([0] * size)
        for i in range(size):
            if j <= i:
                matrix[j][i] = randint(0,100)
    return matrix

def lowTriMat(size):
    '''
    Returns a lower upper triangular matrix of size n X n with random intergers between 1 and 100
    :param size: The number of rows and columns of your matrix
    :return: An nxn lower triangular matrix
    '''
    matrix = []
    for j in range(size):
        matrix.append([0]*size)
        for i in range(size):
            if j >= i:
                matrix[j][i] = randint(0,100)
    return matrix

def diagMat(size):
    '''
    Returns a diagonal matrix of size n X n with random intergers between 1 and 100
    :param size: The number of rows and columns of your matrix
    :return: An nxn diagonal triangular matrix
    '''
    matrix = []
    for j in range(size):
        matrix.append([0]*size)
        for i in range(size):
            if j == i:
                matrix[j][i] = randint(0,100)
    return matrix

def diagAsArray(size):
    '''
    Return a diagonal matrix of random values from 0 to 100 stored as an array
    :param size: Size of the diagonal matrix
    :return: An array of size n.
    '''
    return [randint(0,100) for i in range(size)]

def diagDom(size):
    '''
    Creates a diagonal domiant random matrix
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
    #Force diagonal dominance upon that matrix
    for i in range(size):
        sum = 0
        for j in range(size):
            if (j != i):
                sum += matrix[i][j]
        matrix[i][i] = sum + 1
    return matrix



if __name__ == '__main__':
    print("Square")
    printMatrix(squareMatrix(3))
    print("Lower Triangular")
    printMatrix(lowTriMat(3))
    print("Upper Triangular")
    printMatrix(upTriMat(3))
    print("Diagonal")
    printMatrix(diagMat(3))
    print("Diagonal As an Array")
    print(diagAsArray(3))
    print('Diagonally Dominate Matrix')
    printMatrix(diagDom(3))
