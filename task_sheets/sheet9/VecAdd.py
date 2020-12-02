def vecAdd(v,w):
    '''
    v,w the two vectors to be added
    '''
    return [v[i] + w[i] for i in range(len(v))]

if __name__ == "__main__":
    v = [1,2,3]
    w = [2,3,1]
    print(vecAdd(v,w))
