def scalMult(v,c):
    '''
    v the vector
    c the scalar
    '''
    return [v[i] * c for i in range(len(v))]

if __name__ == "__main__":
    v = [1,2,3]
    c = 3
    print(scalMult(v,c))
