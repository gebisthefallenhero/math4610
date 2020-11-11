from BackSolve import backSolve
from Transpose import matTranspose

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
    print(matrix)
    for row in range(numRows):
        for column in range(numColumns):
            if column >= row:
                matrix[row][column] = row + column - 1
            else:
                matrix[row][column] = 0
    return matrix


if __name__ == '__main__':
    NUM_ROWS = 3
    U = createUpperTriangular(3)
    b = [1 for i in range(NUM_ROWS)]
    print(backSolve(U,b))
