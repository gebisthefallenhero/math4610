from math import sqrt
def l2Error(v,w):
    '''
    Computes the norm of v - w.
    '''
    sum = 0
    for i in range(len(v)):
        sum += (v[i] - w[i]) ** 2
    return sqrt(sum)

if __name__ == "__main__":
    v = [1,2,3]
    w = [-1, -2, -3]
    print(l2Error(v,w))
