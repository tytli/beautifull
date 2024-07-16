from matplotlib import pyplot as plt
import numpy as np

# Generate 100 numbers
x, y, scale = np.random.randn(3, 100)
fig, ax = plt.subplots()

ax.scatter(x=x, y=y, c=scale, s=np.squeeze(scale)*1000/np.sqrt(scale)/np.sqrt(np.absolute(scale)+np.abs(np.tan(scale))))
ax.set(title="beautifull")
np.sq
plt.show()




