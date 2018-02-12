"""
  Name     : c15_12_ARCH.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import scipy as sp 
import matplotlib.pyplot as plt
#
sp.random.seed(12345)
n=1000        # n is the number of observations
n1=100        # we need to drop the first several observations 
n2=n+n1       # sum of two numbers
#
a=(0.1,0.3)   # ARCH (1) coefficients alpha0 and alpha1, see Equation (3)
errors=sp.random.normal(0,1,n2) 
t=sp.zeros(n2)
t[0]=sp.random.normal(0,sp.sqrt(a[0]/(1-a[1])),1) 
for i in range(1,n2-1):
    t[i]=errors[i]*sp.sqrt(a[0]+a[1]*t[i-1]**2) 
    y=t[n1-1:-1] # drop the first n1 observations 
#
plt.title('ARCH (1) process')
x=range(n) 
plt.plot(x,y)
plt.show()
