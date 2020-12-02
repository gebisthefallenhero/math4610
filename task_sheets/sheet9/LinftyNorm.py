def lInftyNorm(v):
    '''
    v: The vector to have the norm returned.
    '''
    max = 0
    for i in range(len(v)):
        if abs(v[i]) > max:
            max = abs(v[i])
    return max

if __name__ == "__main__":
    v = [1,2,3]
    print(lInftyNorm(v))
