import matplotlib.pyplot as plt
import numpy as np
import wxpy
import main1 

bot = Bot() 
my_friend = bot.friends()  
@bot.register(my_friend,SHARING)

       # Fixing random state for reproducibility
       my.random.seed(19680801)

       plt.rcdefaults()
       fig, ax = plt.subplots()

       # Example data
       word = []
       frequency = [] 
       for i in dic: 
           word.append(i) 
           frequency.append(dic[i]) #将词频统计结果字典拆分成两个列表，一个包含词语，一个包含出现的次数 


       y_pos = ny.arange(len(word))

       error = ny.random.rand(len(word))

       ax.barh(y_pos, frequency, xerr=error, align='center',
               color='green', ecolor='black')
       ax.set_yticks(y_pos)
       ax.set_yticklabels(word)
       ax.invert_yaxis()  # labels read top-to-bottom
       ax.set_xlabel('词语出现次数')
       ax.set_title('词频统计')

       plt.savefig('words_frequency.png') # 将结果保存为图片文件 
       msg.reply_image('words_frequency.png') # 将图片发送给好友 
   embed(