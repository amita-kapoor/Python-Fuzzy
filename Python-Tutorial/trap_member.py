import fuzzifier
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0, 10.1, 0.5)
low=np.array([0,2,3,4])
middle=np.array([3,4,5,6])
high=np.array([5,8,9,10])

service=fuzzifier.Trapezoid(x,low,middle,high)
plt.plot(x, service.Low, x, service.middle,x,service.high)
plt.ylabel('Service')
plt.xlabel(' x ')
plt.axis([0, 10, -0.1, 1.1])
plt.grid(True)
plt.show()

print x[0]
