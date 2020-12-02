def outerProd(v,w):
    '''
    v,w the two vectors to be multiplied 
    Returns a matrix from the outer product.
    '''
    matrix = []
    for i in range(len(v)):
        matrix.append([w[j] * v[i] for j in range(len(v))])
    return matrix


if __name__ == "__main__":
    v = [1,2,3]
    w = [2,3,1]
    print(outerProd(v,w))
