import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('life-expectancy-china-1960-2016.txt',
                     delimiter=',',
                     names=['x', 'y'])
da1960  = data[0][1]
da2016  = data[-1][1]
increase = (da2016 - da1960) / da1960
note = 'from {:.2f} in 1960 to {:.2f} in 2016, increased  {:.2%}'\
    .format(da1960, da2016, increase)

plt.figure(figsize=(10, 5))
plt.plot(data['x'], data['y'])
plt.ylabel('Life Expectancy from Birth')
plt.tick_params(axis='x', rotation=70)
plt.title('CHINA\n' + note)

# plt.savefig('life-expectancy-china-1960-2016.png', transparent=True)
plt.show()

# data from:
# https://databank.worldbank.org/data/reports.aspx?source=2&series=SP.DYN.LE00.IN