"""Jumping Jack"""


def  maxStep( N,  K):
    y = 0 # current step
    x = 1
    while x <= N:
        # if moving would land jack on the broken step, pass
        if K == y + x:
            pass
        else:
            y += x
        x += 1
    return y

N = 2
K = 2

print maxStep(N, K)

N = 2
K = 1

print maxStep(N, K)