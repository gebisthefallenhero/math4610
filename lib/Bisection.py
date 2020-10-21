from math import log, exp

def bisection(f,a,b,tol=.001,):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if f(a) * f(b) > 0:
        print("Bisection Error: f(a) * f(b) > 0")
        return
    if a > b:
        a,b = b,a
    if tol < 0:
        print("Bisection Error: Invalid tolerance passed in")
        return
    # This calculates the iteration from the tolerance. The +1 is just for good measure
    iterations = int((log(tol / (b - a))) / log(.5)) + 2
    error = tol * 10
    iterCount = 0
    #Here the plus one is due to not inclusive nature of the range function.
    for i in range(iterations +1):
        c = (a + b) / 2
        f_c = f(c);
        if f_c == 0:
            return c
        if f(a) * f_c < 0:
            b = c
        else:
            a = c
    return c

if __name__ == "__main__":
    f = lambda x: x * exp(3 * x ** 2) - 7 * x
    estimate = bisection(f,-2,1)
    print(estimate)