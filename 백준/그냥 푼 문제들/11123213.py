import numpy as np
#port sys, os
#sys.path.append(os.pardir)
#from dataset.mnist import load_mnist
import matplotlib.pylab as plt
def sum_squares_error(y, t):
    return  0.5*np.sum((y-t)**2)

def numnerical_diff(f ,x):
    h =1e-4
    return (f(x + h)-f(x - h)) / (2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

x = np.arange(0.0 , 20.0 , 0.1)
y =function_1(x)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

print(numnerical_diff(function_1,5))