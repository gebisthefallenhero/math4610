def matTranspose(A):
    '''
    Transposes a 2D list storing a matrix
    :param A: The matrix to be transposed
    :return: A new transposed matrix
    '''
    numRows = len(A)
    numColumns = len(A[0])
    toReturn = [None] * numColumns
    for column in range(numColumns):
        newRow = []
        for row in range(numRows):
            newRow.append(A[row][column])
        toReturn[column] = newRow
    return toReturn


if __name__ == "__main__":
    testMatrix = [
        [2,2],
        [3,3],
        [4,4]
    ]
    #Testing a symmetric Matrix
    testMatrix2 = [
        [1,1,2],
        [1,2,3],
        [2,3,3]
    ]
    tranposed = matTranspose(testMatrix)
    print("Testing rectangular matrix")
    for row in tranposed:
        print(row)

    tranposed2 = matTranspose(testMatrix2)
    print("Testing Symmetric Matrix")
    for row in tranposed2:
        print(row)
