import matplotlib.pyplot as plt
import numpy as np
import wxpy
import mainy 

#导入模块 
from wxpy import * 
#初始化机器人，扫码登录 
bot = Bot() 
#搜索名称含有“王璞”的好友 
# my_friends=bot.friends().search('王璞')[0] 
#给好友发送信息 
# #my_friends.send('你好') 

# Fixing random state for reproducibility
np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()

  #给好友发送信息 

           my_friends.send(text1) 

       #让程序保持运行 

       embed()  


