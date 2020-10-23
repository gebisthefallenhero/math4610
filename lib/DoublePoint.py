from numpy import float64

def doublePoint():
    one = float64(1.0)
    seps = float64(1.0)
    appone = float64(1.0)
    for ipow in range(1, 1000):
        seps = seps / 2
        seps = float64(seps)
        appone = one + seps
        if (abs(appone) == 1):
            return ipow
    print("Didn't make it after 1000 Iterations")


if __name__ == "__main__":
    print(f"The number of binary digits that can be printed is {doublePoint()}")
    print(f"The smallest number this corresponds to is {2 ** -doublePoint()}")