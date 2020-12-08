def dotProd(v,w):
    '''
    v,w the two vectors to be multiplied 
    '''
    sum = 0
    for i in range(len(v)):
        sum += v[i] * w[i]
    return sum

if __name__ == "__main__":
    v = [1,2,3]
    w = [2,3,1]
    print(dotProd(v,w))
