import os
from mymodule import stats_word

#这个函数中open括号中的部分是在issue中看到的，目前不是特别明白它的意思
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json')) as f:
    text=f.read()
    f.closed
    stats_word.stats_text_cn(text,100)


#try:
    #stats_word.stats_text(text,100)#这一行代码会影响结果的输出，所以先屏蔽
#except ValueError as err:
    #print('具体原因为:{0}'.format(err))#将错误的信息显示出来


