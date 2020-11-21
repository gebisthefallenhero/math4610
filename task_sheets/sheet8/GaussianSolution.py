def systemSolve(A,b):
    '''
    Solve a system of linear equations. No pivoting strategies used.
    :param A: The Matrix with the equations.
    :param b: The solution vector
    :return: A vector containing the solution to the equation.
    '''
    #The code for the row reducing.
    numRows = len(A)
    numColumns = len(A[0])
    for k in range(numRows - 1):
        for i in range(k + 1, numColumns):
            factor = A[i][k] / A[k][k]
            for j in range(k, numColumns):
                A[i][j] = A[i][j] - factor * A[k][j]
            b[i] = b[i] - factor * b[k]
    #The code for the back substitution
    xVec = [0] * numRows
    for row in range(numRows - 1, -1, -1):
        sum = b[row]
        for column in range(row + 1, numColumns):
            sum -= A[row][column] * xVec[column]
        xVec[row] = sum / A[row][row]
    return xVec


if __name__ == '__main__':
    from MatrixCreator import diagDom,printMatrix,diagAsArray
    A = diagDom(3)
    print('The matrix A')
    printMatrix(A)
    print('B vector')
    b = diagAsArray(3)
    print(b)
    x = systemSolve(A,b)
    print('Solution x')
    print(x)

