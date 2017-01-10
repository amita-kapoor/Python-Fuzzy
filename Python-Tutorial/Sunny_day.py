# Code to find the Crisp Set value and Fuzzy set value for x : The percent of sky covered with clouds
import numpy as np
import matplotlib.pyplot as plt
# Charecteristic function for Crisp Set
def Crisp_Set(x):
    crisp = (x <= 30)
    return crisp
# Membership function for Fuzzy Set
def Fuzzy_Set(x):
    return 1.0-x/100.0

if __name__=='__main__':
    x=np.arange(0,101,10)
    print "The Crisp set is", Crisp_Set(x)
    print "The Fuzzy set is", Fuzzy_Set(x)
    plt.plot(x,Crisp_Set(x), x, Fuzzy_Set(x))
    plt.ylabel('Charactreristic/Membership Function')
    plt.xlabel('Value of x in %')
    plt.axis([0, 100, -0.1, 1.1])
    plt.grid(True)
    plt.show()

