from math import exp

def newtonsMethod(f,f_p,x_start,tol=.001,maxIter=1000,errorMessage=False):
    x_old = x_start
    error = tol * 10
    iter = 0
    while error > tol and iter < maxIter:
        iter += 1
        x_new = x_old - (f(x_old)/ f_p(x_old))
        error = abs(x_new - x_old)
        x_old = x_new
        if error < tol:
            return x_new
    if errorMessage == True:
        print("Did not converge")


if __name__ == "__main__":
    f = lambda x: x * exp(3 * x ** 2) - 7 * x
    f_p = lambda x: 6 * x ** 2 * exp(3 * x ** 2) + exp(3 * x ** 2) - 7
    guess = 1
    print(newtonsMethod(f,f_p,guess,errorMessage=True))

