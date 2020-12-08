def l1Error(v,w):
    '''
    Computes the norm of v - w.
    '''
    sum = 0
    for i in range(len(v)):
        sum += abs(v[i] - w[i])
    return sum

if __name__ == "__main__":
    v = [1,2,3]
    w = [-1, -2, -3]
    print(l1Error(v,w))
