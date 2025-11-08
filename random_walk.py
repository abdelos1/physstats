#
#Libraries
import random #
import matplotlib.pyplot as plt #
import numpy as np #for linear regression
from scipy.stats import linregress

ndim=1000000
npas=1000000
nsim=100
x=np.zeros(npas)
y=np.zeros(npas)
for i in range(nsim):
    position=0
    a=1
    for ipas in range(npas):
        r=random.random() 
        if r<0.5: #equiprobable
            istep=+a
        else:
            istep=-a
        position+=istep
        
        x[ipas]+=position
        y[ipas]+=position**2 
        
x=x/nsim
y=y/nsim
deltaxy=np.sqrt(y-x**2)
# steps rank array
step=np.arange(1,ndim+1)
#a,b=np.polyfit(x,1)
#a,b,coef,pval,std=linregress(np.log(step),np.log(x))
plt.plot(step,x)
#plt.loglog(step,deltaxy,label='échelle logarithmique')
plt.show()
