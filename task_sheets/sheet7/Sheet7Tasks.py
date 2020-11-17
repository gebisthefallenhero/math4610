from BackSolve import backSolve
from Transpose import matTranspose
from MatrixCreator import printMatrix
from ForwardSolve import forwardSolve
from MatrixCreator import squareMatrix, diagAsArray
from RowReduce import rowReduce

def createUpperTriangular(numRows, numColumns = None):
    '''
    Creates an upper triangular matrix based on given rules
    :param numRows: The number of rows, and columns if n x n
    :param numColumns: The number of columns
    :return: The upper triangular matrix
    '''
    if numColumns == None:
        numColumns = numRows
    matrix = [[0] * numColumns for i in range(numRows)]
    for row in range(numRows):
        for column in range(numColumns):
            if column >= row:
                matrix[row][column] = row + column - 1
            else:
                matrix[row][column] = 0
    return matrix


if __name__ == '__main__':
    #Task 1
    NUM_ROWS = 3
    U = createUpperTriangular(3)
    print("Printing U")
    printMatrix(U)
    b = [1 for i in range(NUM_ROWS)]
    print("Solution with b as 1's vector")
    print(backSolve(U,b))
    print("Printing U^T")
    L = matTranspose(U)
    printMatrix(L)
    print("Solution with b as 1's vector.")
    print(forwardSolve(L,b))
    A = squareMatrix(3)
    print("Random Square Matrix")
    printMatrix(A)
    print("Random b vector")
    b = diagAsArray(3)
    print(b)
    print("Matix Reduced")
    A, b = rowReduce(A,b)
    printMatrix(A)
    print("Reduced b vector")
    print(b)

