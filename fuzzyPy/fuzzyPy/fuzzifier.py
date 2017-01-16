#import numpy as np
# Defines TRiangular membership finction f:x->y, with 'a' and 'c' the base of triangle and 'b' is peak
def trimf(x, a, b, c):
    X1 = (x-a)/(b-a)
    X2 = (c-x)/(c-b)
    X3=np.minimum(X1, X2)
    X4=np.zeros(x.size)
    y = np.maximum(X3, X4)
    return y


def trapmf(x, a, b, c, d):
    X1 = (x-a)/(b-a)
    X2=np.ones(x.size)
    X3 = (c-x)/(c-b)
    X4=np.minimum(np.minimum(X1, X2), X3)
    X5=np.zeros(x.size)
    y = np.maximum(X4, X5)
    return y
    y = np.amax([np.amin([(x - a) / (b - a), 1, (d - x) / (d - c)]), 0])
    return y


def gaussmf(x, c, v):
    y = np.exp(-(x - c) ^ 2 / 2 * v ^ 2)
    return y
