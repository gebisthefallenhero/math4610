def matVecMult(A,v):
    '''
    Multiplies a matrix and a vector from the right
    :param A: the matrix to be multiplied
    :param v: the vector to be multiplied
    :return: the new vector
    '''
    numRows = len(A)
    vecLength = len(v)
    newVec = []
    for row in range(numRows):
        sum = 0
        for entry in range(vecLength):
            sum += vec[entry] * A[row][entry]
        newVec.append(sum)
    return newVec

if __name__ == '__main__':
    matrix = [
        [1,2],
        [3,4]
    ]
    vec = [3,4]
    print(matVecMult(matrix,vec))