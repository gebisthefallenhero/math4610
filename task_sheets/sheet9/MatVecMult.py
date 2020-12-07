from DotProd import dotProd
def matVecMult(A,v):
    '''
    A The matrix to the multiplied
    v The vector to be multiplied, on the left.
    '''
    newVect = []
    for row in A:
        newVect.append(dotProd(row,v))
    return newVect
    

if __name__ == "__main__":
    A = [
            [1, 2, 3,4],
            [4,5,6,7],
            [7,8,9,10]
            ]
    v = [2,2,2,2]
    print(matVecMult(A,v))
