import matplotlib.pyplot as plt
import numpy as np
from mymodule.Think_Python_modules import make_wordlist
import collections
import math
word_list = make_wordlist('Skin in the Game.txt')
fequency = collections.Counter(word_list).most_common(5000)
x = []
y = []
for i in range(1,len(fequency)+1):
    x.append(i)
    y.append(fequency[i-1][1])
plt.clf()
plt.xscale('log')
plt.yscale('log')
plt.title('Zipf plot')
plt.xlabel('rank')
plt.ylabel('frequency')
plt.plot(y, x, 'r-', linewidth=1)
plt.show()

'''
plt.scatter(x,y,s=1)
#plt.legend(loc = 'best')    # 设置 图例所在的位置 使用推荐位置

plt.show()  
'''

