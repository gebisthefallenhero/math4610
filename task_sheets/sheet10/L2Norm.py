from math import sqrt
def l2Norm(v):
    '''
    v: The vector to have the norm returned.
    '''
    sum = 0
    for i in range(len(v)):
        sum += v[i] * v[i]
    return sqrt(sum)

if __name__ == "__main__":
    v = [1,2,3]
    print(l2Norm(v))
