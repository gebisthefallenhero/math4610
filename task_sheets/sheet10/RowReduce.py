def rowReduce(A,b):
    '''
    Row reduce a matrix that is assumed to be in good form, aka no pivoting strategies.
    :param A: The Matrix to be reduced
    :param b: The b vector in Ax = b
    :return: A tuple containing both A and b.
    '''
    numRows = len(A)
    numColumns = len(A[0])
    for  k in range(numRows - 1):
        for i in range(k + 1, numColumns):
            factor = A[i][k] / A[k][k]
            for j in range(k, numColumns):
                A[i][j] = A[i][j] - factor * A[k][j]
            b[i] = b[i] - factor * b[k]
    return A,b


if __name__ == '__main__':
    testMatrix = [
        [1, -3, 1],
        [2, -8,  8],
        [-6, 3, -15]
    ]
    testB = [4,-2,9]

    A,b = rowReduce(testMatrix,testB)
    for row in A:
        print(row)
    print(b)
