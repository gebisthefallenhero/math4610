
def LUFact(A):
    '''
    Performs an LU Factorization on A
    :param A: The Matrix to be LU factorized
    :return: A matrix with L in the lower half and U above the diagonal. The diagonal holds the entries of U
    '''
    numRows = len(A)
    numColumns = len(A[0])
    for k in range(numRows - 1):
        for i in range(k + 1, numColumns):
            factor = A[i][k] / A[k][k]
            A[i][k] = factor
            for j in range(k + 1, numColumns):
                A[i][j] = A[i][j] - factor * A[k][j]
    return A

def LUForwardSolve(A,b):
    '''
    A forward substitution after an LU Factorization has been performed
    :param A: A matrix has has been LU factorized
    :param b: the vector on the right side of the equation
    :return: A solution vector
    '''
    #Change the entries of the passed in matrix to match the forward substitution.
    for i in range(len(A)):
        A[i][i] = 1
    numRows, numColumns = len(A), len(A)
    xVec = [0] * numRows
    for row in range(numRows):
        sum = b[row]
        for column in range(row):
            sum -= A[row][column] * xVec[column]
        xVec[row] = sum / A[row][row]
    return xVec



if __name__ == '__main__':
    from MatrixCreator import printMatrix
    test = [
        [1,1,1],
        [2,3,5],
        [4,6,8]
    ]
    A = LUFact(test)
    printMatrix(A)
    b = [1,1,1]
    print('Solving Lc = b with b = [1,1,1]')
    c = LUForwardSolve(A,b)
    print(c)


