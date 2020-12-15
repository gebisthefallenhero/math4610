def matInftyNorm(A):
    '''
    Computes the Infinity Norm of a matrix
    :param A:
    :return: the maximum row sum
    '''
    lenRows = len(A[0])
    numRows = len(A)
    max = 0
    for i in range(numRows):
        sum = 0
        for j in range(lenRows):
            sum += abs(A[i][j])
        if sum > max:
            max = sum
    return max


if __name__ == '__main__':
    A = [
        [1,1,1,1,1,1,1],
        [2,2,2,2,2,2,2],
        [3,3,3,3,3,3,3]
    ]
    print(matInftyNorm(A))