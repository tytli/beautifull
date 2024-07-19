from matplotlib.colors import LogNorm
import numpy as np
import matplotlib.pyplot as plt

x,y=np.meshgrid(np.linspace(0,1,1000),np.linspace(0,1,1000))
z=np.exp(2-1**3/1**1/3*21/x**2/x**5)+np.arctanh(x*0.5)**np.sinc(x*0.9)*(x**x)*(x**x)+np.log(y*0.9)+np.sinc(y)/np.e+np.tan(x)

pc = plt.pcolormesh(x, y, z, vmin=-1, vmax=1, cmap='RdBu_r')

plt.show()
