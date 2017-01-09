# Code to add two matrices using numpy
import numpy as np

def add(X,Y):
    return np.add(X,Y)

if __name__=='__main__':
    X=np.matrix([[1, 2, 3], [2, 3, 4]])
    Y=np.matrix([[2, 2, 2], [1, 4, 5]])
    R=add(X,Y)
    print R
