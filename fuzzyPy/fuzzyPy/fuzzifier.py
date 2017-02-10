import numpy as np

class FuzzyPy():
    # Defines TRiangular membership finction f:x->y, with 'a' and 'c' the base of triangle and 'b' is peak
    def trimf(self, x, a, b, c):
        X1 = (x - a) / (b - a)
        X2 = (c - x) / (c - b)
        X3 = np.minimum(X1, X2)
        X4 = np.zeros(x.size)
        y = np.maximum(X3, X4)
        return y

    # Defines Trapezoidal membership finction f:x->y, with 'a' and 'd' the base of trpezoid and 'b' and 'c' the shoulder
    def trapmf(self, x, a, b, c, d):
        X1 = (x - a) / (b - a)
        X2 = np.ones(x.size)
        X3 = (d - x) / (d - c)
        X4 = np.minimum(np.minimum(X1, X2), X3)
        X5 = np.zeros(x.size)
        y = np.maximum(X4, X5)
        return y

    def gaussmf(self, x, c, v):
        """Compute Gaussian Membership function. """
        y = np.exp(-np.power((x - c) , 2) / (2 * v ^ 2.0))
        return y
    
    def softmax(x):
       """Compute softmax values for each sets of scores in x."""
       return np.exp(x)/np.sum(np.exp(x), axis=0)
    

class Triangle(FuzzyPy):
    def __init__(self, x, low, middle, high):
        self.low = self.trimf(x, low[0], low[1], low[2])
        self.middle = self.trimf(x, middle[0], middle[1], middle[2])
        self.high = self.trimf(x, high[0], high[1], high[2])

class Triangle5(FuzzyPy):
    def __init__(self, x, low2,low1, middle, high1,high2):
        self.low2 = self.trimf(x, low2[0], low2[1], low2[2])
        self.low1 = self.trimf(x, low1[0], low1[1], low1[2])
        self.middle = self.trimf(x, middle[0], middle[1], middle[2])
        self.high1 = self.trimf(x, high1[0], high1[1], high1[2])
        self.high2 = self.trimf(x, high2[0], high2[1], high2[2])

class Trapezoid(FuzzyPy):
    def __init__(self, x, low, middle, high):
        self.low = self.trapmf(x, low[0], low[1], low[2], low[3])
        self.middle = self.trapmf(x, middle[0], middle[1], middle[2], middle[3])
        self.high = self.trapmf(x, high[0], high[1], high[2], high[3])

class Trapezoid5(FuzzyPy):
    def __init__(self, x, low2,low1, middle, high1,high2):
        self.low2 = self.trapmf(x, low2[0], low2[1], low2[2], low2[3])
        self.low1 = self.trapmf(x, low1[0], low1[1], low1[2], low1[3])
        self.middle = self.trapmf(x, middle[0], middle[1], middle[2], middle[3])
        self.high1 = self.trapmf(x, high1[0], high1[1], high1[2], high1[3])
        self.high2 = self.trapmf(x, high2[0], high2[1], high2[2], high2[3])

class Gauss(FuzzyPy):
    def __init__(self, x, low, middle, high):
        self.low = self.gaussmf(x, low[0], low[1])
        self.middle = self.gaussmf(x, middle[0], middle[1])
        self.high = self.gaussmf(x, high[0], high[1])

class Gauss5(FuzzyPy):
    def __init__(self, x, low2,low1, middle, high1,high2):
        self.low2 = self.gaussmf(x, low2[0], low2[1])
        self.low1 = self.gaussmf(x, low1[0], low1[1])
        self.middle = self.gaussmf(x, middle[0], middle[1])
        self.high1 = self.gaussmf(x, high1[0], high1[1])
        self.high2 = self.gaussmf(x, high2[0], high2[1])
