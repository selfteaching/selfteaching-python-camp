# 调用stats_word中的stats_text_cn函数以统计中文汉字词频
from mymodule.stats_word import stats_text_cn     # 从 模块中(mymodule是包，stats_word是模块) 导入 函数stats_text

import json                                    # 导入json模块
# unicode是一个内置函数，第二个参数指示源字符串的编码格式，从unicode转str，要用encode方法，即转换为utf-8编码的字符串str
with open('F:/编程入门/selfteaching-python-camp/exercises/1901090023/d09/tang300.json',encoding='UTF-8') as f:    # tang文件和main文件是同级目录，这是用相对路径；还有一种是绝对路径：with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tang300.json')) as f :
    text = f.read()                            # f.read()读取并返回文件的整个内容，会读取一些数据并将其作为字符串返回
    
try:
    print(stats_text_cn(text,100))                # 输出中文词频最高的前100个词
except NameError as err:                          # 假设调用者忘了输入text，由于text没有被定义，则由except来捕获NameError异常
    print('Oops, cannot find text! Please input text!')
else:                                          # 如果调用者正确定义了text,即无错误发生，则执行else语句
    print('no error')
finally:                                       # 不管有无异常，最后都要执行finally语句，让程序按流程执行完。
    print('The end')



# 笔记
# 1.如何用Python读取中文文件？
# 在open函数末端加一个encoding声明就好了，encoding声明里用的编码是文本自己本身所用的编码，代码见上图
# 如果文件是用gbk方式编码的话，那么把上述的utf-8改为gbk就好

# 2. 如何用Python(复制)写入中文txt文件？
# 首先你要做的，是在打开写入文件时，声明encoding编码
# put_in = open(becopyed_file,"w+",encoding= 'utf-8')
# 之后，在写入文件的时候设置好编码方式，先用encode编码，再用decode解码文件
# put_in.write(str(data.encode('utf-8').decode('utf-8')))

# 3. 相对路径和绝对路径的概念
# 绝对路径就是文件的真正存在的路径，是指从硬盘的根目录(盘符)开始，进行一级级目录指向文件。 
# 相对路径就是以当前文件为基准进行一级级目录指向被引用的资源文件。 
# 以下是常用的表示当前目录和当前目录的父级目录的标识符 
# ../ 表示当前文件所在的目录的上一级目录 
# ./ 表示当前文件所在的目录(可以省略) 
# / 表示当前站点的根目录(域名映射的硬盘目录) 

