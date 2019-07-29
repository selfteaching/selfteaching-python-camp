# import matplotlib
# print(matplotlib.matplotlib_fname())

# # # from matplotlib.font_manager import FontProperties

# def getChineseFont():  
#     return FontProperties(fname='/anaconda3/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf',size=15) 

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager

plt.rcdefaults()
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif']= 'SimHei'

x= [1,2,3,4,5,6]
y = x
plt.plot(x,color='red',linewidth=2.0,linestyle='-.',label=u'崔')
plt.legend(loc='best')
plt.show()