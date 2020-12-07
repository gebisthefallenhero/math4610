def matMatMult(A,B):
    '''
    A,B The matricies to be multiplied as A * B 
    Checking dimensions is left to user.
    '''
    toReturn = []
    for i in range(len(A)): #For every row of A
        sum = 0
        for j in range(len(B)): # For the number of entries in a column of B
            sum += A[i][j] * B[j][i]
        toReturn.append(sum)
    return toReturn

    

if __name__ == "__main__":
    A = [
            [0,2],
            [0,1],
            [0,0]
        ]

    B = [
            [1,2,3],
            [4,5,6],
        ]

    
            
    print(matMatMult(A,B))
