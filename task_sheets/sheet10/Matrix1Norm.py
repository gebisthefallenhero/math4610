def mat1Norm(A):
    '''
    Computes the 1 Norm of a matrix
    :param A:
    :return: the maximum column sum
    '''
    numCols = len(A[0])
    lenCols = len(A)
    max = 0
    for i in range(numCols):
        sum = 0
        for j in range(lenCols):
            sum += abs(A[j][i])
        if sum > max:
            max = sum
    return max


if __name__ == '__main__':
    A = [
        [1,2,3],
        [1,2,3],
        [1,2,3],
        [1,2,3],
        [1,2,3]
    ]
    print(mat1Norm(A))