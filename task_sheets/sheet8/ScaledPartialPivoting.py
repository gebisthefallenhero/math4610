def scaledPartPiv(A,b):
    '''
    Solves a linear system using scaled partial pivoting.
    :param A: The matrix repsenting the left hand side of the equations.
    :param b: The matrix representing the right hand side of the equations
    :return: A solution vector.
    '''
    rowLen = len(b) #We are assuming a square system so rowLen = colLen
    map = [i for i in range(rowLen)]
    maxVec = maxVector(A)
    #The Row Reduction
    for k in range(rowLen - 1):
        pivotRow = bestPivot(A,k,maxVec,map)
        map[k],map[pivotRow] = map[pivotRow], map[k]
        for i in range(k + 1, rowLen):
            factor = A[map[i]][k]/ A[map[k]][k]
            for j in range(k, rowLen):
                A[map[i]][j] = A[map[i]][j] - factor * A[map[k]][j]
            b[map[i]] = b[map[i]] - factor * b[map[k]]
    #The back substitution
    xVec = [0] * rowLen
    for row in range(rowLen - 1, -1, -1):
        sum = b[map[row]]
        for column in range(row +1, rowLen):
            sum -= A[map[row]][column] * xVec[column]
        xVec[row] = sum / A[map[row]][row]
    return xVec


def bestPivot(A, column,maxVec,map):
    '''
    Returns the best pivot in a given column of A
    :param A: The matrix in question
    :param column: The column in question
    :return:
    '''
    maxPivotRow = 0
    maxPivot = 0
    for row in range(column,len(map)):
        pivot = abs(A[map[row]][column] / maxVec[map[row]])
        if pivot > maxPivot:
            maxPivot = pivot
            maxPivotRow = row
    return maxPivotRow



def maxVector(A):
    '''
    Finds the absolute maximum value in each row of a matrix A
    :param A: The matrix in question
    :return: A vector with each maximum value in the row
    '''
    maxVector = []
    for row in A:
        maxValue = 0
        for value in row:
            absVal = abs(value)
            if absVal > maxValue:
                maxValue = absVal
        maxVector.append(maxValue)
    return maxVector

if __name__ == '__main__':
    from MatrixCreator import printMatrix
    test = [
     [30,591400],
     [5.291,-6.130]
    ]
    b = [591700,46.78]
    x = scaledPartPiv(test,b)
    printMatrix(x)

    test2 = [
        [1,2,-2],
        [2,1,-5],
        [1,-4,1]
    ]
    b = [-15,-21,18]
    print(scaledPartPiv(test2,b))