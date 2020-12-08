def matAdd(A,B):
    '''
    A,B the matricies to be added
    '''
    for i in range(len(A)):
        for j in range(len(B)):
            A[i][j]= A[i][j] + B[i][j]
    return A

if __name__ == "__main__":
    A = [
            [1, 2, 3],
            [4,5,6],
            [7,8,9]
            ]
    B = [
            [1,1,1],
            [2,2,2],
            [3,3,3]
            ]
    print(matAdd(A,B))
