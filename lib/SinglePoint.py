from numpy import float32

def singlePoint():
    one = float32(1.0)
    seps = float32(1.0)
    appone = float32(1.0)
    for ipow in range(1, 1000):
        seps = seps / 2
        seps = float32(seps)
        appone = one + seps
        if (abs(appone) == 1):
            return ipow
    print("Didn't make it after 1000 Iterations")


if __name__ == "__main__":
    print(f"The number of binary digits that can be printed is {singlePoint()}")
    print(f"The smallest number this corresponds to is {2 ** -singlePoint()}")