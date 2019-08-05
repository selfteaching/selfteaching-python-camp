
from mymodule import stats_word as s   #从模块中导入自定义函数
from os import path                    #从os中导入路径

print(__file__, __name__)
fp =path.join(path.dirname(path.abspath(__file__)), 'tang300.json')  #找到唐诗三百首的路径
with open(fp, 'rb') as f:                                            #读取本地文件，以以 binary（二进制） mode 打开文件
    read_data =f.read()
    
    b = read_data.decode('utf8')                                     #将utf8解码为Unicode
    c3 =s.stats_text_cn(b,100) 
    print(c3.most_common(100))

    f.close(fp, 'rb')
    



try:                                 #try except  捕获异常
    print(c3.most_common(100))
except ValueError as err:
    print("err:not string ,try again")

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()

