def l1Norm(v):
    '''
    v: The vector to have the norm returned.
    '''
    sum = 0
    for i in range(len(v)):
        sum += v[i]
    return sum

if __name__ == "__main__":
    v = [1,2,3]
    print(l1Norm(v))
