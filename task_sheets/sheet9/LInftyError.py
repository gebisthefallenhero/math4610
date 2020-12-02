def lInftyError(v,w):
    '''
    Computes the infinity norm of v - w.
    '''
    max = 0
    for i in range(len(v)):
        val = abs(v[i] - w[i])
        if val > max:
            max = val
    return max

if __name__ == "__main__":
    v = [1,2,3]
    w = [-1, -2, -3]
    print(lInftyError(v,w))
