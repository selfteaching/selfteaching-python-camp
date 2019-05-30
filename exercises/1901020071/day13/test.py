import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
# np.random.seed(19680801)

# from pylab import mpl
# mpl.rcParams['font.sans-serif']=['simkai'] #用来正常显示中文标签
# mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号

#matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei'] 

ll=[(u'杜杜', 19), ('命令行', 13), ('soft', 11), ('able', 10), ('developer', 9), ('launch', 7), ('quantum', 7), ('ability', 7), ('support', 7), ('use', 7)]
dic=dict(ll)
keyList=list(dic.keys())
print(keyList)
#plt.rcdefaults()

fig, ax = plt.subplots()

y_pos=np.arange(len(keyList))


values=list(dic.values())
print(values)
values=np.asarray(values,dtype=int)



ax.barh(y_pos,values,align='center')

# ax.set_yticks(y_pos)
# ax.set_yticklabels(people)
# ax.invert_yaxis()  # labels read top-to-bottom

ax.set_yticks(y_pos)
ax.set_yticklabels(keyList)
ax.invert_yaxis()
ax.set_xlabel('底部')
ax.set_title('How fast do you want to go today?')
plt.show()