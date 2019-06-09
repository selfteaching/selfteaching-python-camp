"""
1）导入标准库re和tkinter，创建并简单设置应用主程序，在窗口顶部放置一个只读的文本框用来显示信息。
"""
import re
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
# 设置窗口大小和位置
#root.geometry('30*27+4+1')
root.geometry()
# 不允许改变窗口大小
#root.resizable(False, False)
# 设置窗口标题
root.title('简易计算器')
# 放置用来显示信息的文本框，并设置为只读
contentVar = tkinter.StringVar(root, '')
contentEntry = tkinter.Entry(root, textvariable=contentVar)
contentEntry['state'] = 'readonly'
contentEntry.place(x=10, y=10, width=280, height=20)


"""
2）编写计算器上各种按钮的通用处理代码。
"""
# 按钮通用代码
def buttonClick(btn):
    content = contentVar.get()
    # 如果已有内容是以小数点开头的，前面加0
    if content.startswith('.'):
        content = '0' + content

    # 根据不同按钮做出相应的处理
    if btn in '0123456789':
        content += btn
    elif btn == '.':
        lastPart = re.split(r'\+|-|\*|/]', content)[-1]
        if '.' in lastPart:
            tkinter.messagebox.showerror('错误', '小数点太多了')
            return
        else:
            content += btn
    elif btn == 'C':
            content = ''
    elif btn == '=':
        try:
            # 对输入的表达式求值
            content = str(eval(content))
        except:
            tkinter.messagebox.showerror('错误', '表达式错误')
            return
    elif btn in operators:
        if content.endswith(operators):
            tkinter.messagebox.showerror('错误', '不允许存在连续运算符')
            return
        content += btn
    elif btn == 'Sqrt':
        n = content.split('.')
        if all(map(lambda x: x.isdigit(), n)):
            content = eval(content) ** 0.5
        else:
            tkinter.messagebox.showerror('错误', '表达式错误')
            return
    
    contentVar.set(content)


"""
3）创建计算器上的各种按钮，设置相应的属性和行为，启动消息主循环。
"""
# 放置清除按钮和等号按钮
btnClear = tkinter.Button(root, text='Clear', command=lambda:buttonClick('C'))
btnClear.place(x=40, y=40, width=80, height=20)
btnCompute = tkinter.Button(root, text='=', command=lambda:buttonClick('='))
btnCompute.place(x=170, y=40, width=80, height=20)

# 放置10个数字、小数点和计算平方根的按钮
digits = list('0123456789.') + ['Sqrt']
index = 0
for row in range(4):
    for col in range(3):
        d = digits[index]
        index += 1
        btnDigit = tkinter.Button(root, text=d, command=lambda x=d:buttonClick(x))
        btnDigit.place(x=20+col*70, y=80+row*50, width=50, height=20)
# 放置运算符按钮
operators = ('+', '-', '*', '/', '**', '//')
for index, operator in enumerate(operators):
    btnOperator = tkinter.Button(root, text=operator, command=lambda x=operator:buttonClick(x))
    btnOperator.place(x=230, y=80+index*30, width=50, height=20)

root.mainloop()