def linearRegression(x,y):
    if len(x) != len(y):
        print("The length of the vectors do not match for regression")
        return
    #initialize the values in A^TA
    a11 = len(x)
    a12 = 0
    a22 = 0
    #Now the values in A^T y
    b1 = 0
    b2 = 0
    for i in range(len(x)):
        a12 += x[i]
        a22 += x[i] * x[i]
        b1 += y[i]
        b2 += y[i] * x[i]
    #Solve the 2x2 system.
    det = a11 * a22 - a12 * a12
    c1 = (a22 * b1 - a12 * b2) / det
    c2 = (a11 * b2 - a12 * b1) / det
    return c1,c2


if __name__ == "__main__":
    #Driver program with test vectors.
    x = [2,3,5,7,9]
    y = [4,5,7,10,15]
    print(linearRegression(x,y))