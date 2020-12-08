def matScal(A,c):
    '''
    A The matrix to the multiplied
    c The scalar to mulitply it by
    '''
    for i in range(len(A)):
        for j in range(len(A[0])): #In the case that A is a rectangular matrix
            A[i][j]= A[i][j] * c 
    return A

if __name__ == "__main__":
    A = [
            [1, 2, 3,4],
            [4,5,6,7],
            [7,8,9,10]
            ]
    c = 2
    print(matScal(A,c))
