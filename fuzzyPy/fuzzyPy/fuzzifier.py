#import numpy as np

import numpy as np


## import the file fuzzifier.py
## Argument to the class are of type numpy array
class Triangle():
    def __init__(self,x,low, middle,high):
       self.low = self.trimf(x,low[0],low[1],low[2])
       self.middle = self.trimf(x, middle[0],middle[1], middle[2])
       self.high = self.trimf(x, high[0], high[1], high[2])
    
# Defines TRiangular membership finction f:x->y, with 'a' and 'c' the base of triangle and 'b' is peak
    def trimf(x, a, b, c):
        X1 = (x-a)/(b-a)
        X2 = (c-x)/(c-b)
        X3=np.minimum(X1, X2)
        X4=np.zeros(x.size)
        y = np.maximum(X3, X4)
        return y

class Trapezoid():
    def __init__(self,x,low, middle,high):
        self.low = self.trapmf(x, low[0], low[1], low[2], low[3])
        self.middle = self.trapmf(x, middle[0], middle[1], middle[2],middle[3])
        self.high = self.trapmf(x, high[0], high[1], high[2],high[3])
        
        
    def trapmf(x, a, b, c, d):
        X1 = (x - a) / (b - a)
        X2 = np.ones(x.size)
        X3 = (c - x) / (c - b)
        X4 = np.minimum(np.minimum(X1, X2), X3)
        X5 = np.zeros(x.size)
        y = np.maximum(X4, X5)
        return y
        

class Gauss():
    def __init__(self,x,low, middle,high):
        self.low = self.gaussmf(x, low[0], low[1])
        self.middle = self.gaussmf(x, middle[0], middle[1])
        self.high = self.gaussmf(x, high[0], high[1])


    def gaussmf(x, c, v):
        y = np.exp(-(x - c) ^ 2 / 2 * v ^ 2)
        return y
