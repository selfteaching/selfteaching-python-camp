import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,5))

lebdata = np.genfromtxt('life-expectancy-china-1960-2016.txt',
                     delimiter=',',
                     names=['x', 'y'])

hdidata = np.genfromtxt('hdi-china-1870-2015.txt',
                     delimiter=',',
                     names=['x', 'y'])


plt.plot(hdidata['x'], hdidata['y'])
plt.tick_params(axis='x', rotation=70)
plt.title('China: 1870 - 2015')

# plt.savefig('human-development-index.png', transparent=True)

plt.legend(['Human Development Index'])
plt.plot(lebdata['x'], lebdata['y']*0.005)
plt.plot(secondary_y=True)
# plt.savefig('human-development-index-china-1870-2015.png', transparent=True)

plt.show()
# data from:
# https://ourworldindata.org/957e133e-f3e9-4bf2-9627-dbf30ebc9b4d