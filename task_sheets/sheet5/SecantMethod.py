from math import exp

def secantMethod(f,x_0,x_1,tol=.001,maxIter=1000,errorMessage=False):
    x_old = x_0
    x_curr = x_1
    error = tol * 10
    iter = 0
    while error > tol and iter < maxIter:
        iter += 1
        f_curr = f(x_curr)
        x_new = x_curr - f_curr * ((x_curr - x_old)/(f(x_curr) - f(x_old)))
        error = abs(x_new - x_curr)
        x_old = x_curr
        x_curr = x_new
        if error < tol:
            return x_new
    if errorMessage == True:
        print("Did not converge")



if __name__ == "__main__":
    f = lambda x: x * exp(3 * x ** 2) - 7 * x
    guess = 1
    guess2 = 1.1
    print(secantMethod(f,guess,guess2,errorMessage=True))


