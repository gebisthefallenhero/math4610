from Transpose import matTranspose

def forwardSolve(A,b):
    '''
    :param A: The lower triangular matrix to be back substituted
    :param b: The b vector in the system of equations
    :return: The solution vector x.
    '''
    numRows, numColumns = len(A), len(A)
    xVec = [0] * numRows
    for row in range(numRows):
        sum = b[row]
        for column in range(row):
            sum -= A[row][column] * xVec[column]
        xVec[row] = sum / A[row][row]
    return xVec

if __name__ == '__main__':
    testMatrix = [
        [1,2,3],
        [0,1,2],
        [0,0,10]
    ]
    testMatrix = matTranspose(testMatrix)
    testB = [6, 4, 30]
    print(forwardSolve(testMatrix,testB))