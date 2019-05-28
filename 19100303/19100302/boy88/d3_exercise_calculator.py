from tkinter import *
reset=True
def buttonCallBack(event):
    global label
    global reset
    num=event.widget['text']
    if num=='C':
        label['text']="0"
        return
    if num in "=":
        label['text']=str(eval(label['text']))
        reset=True
        return 
    s=label['text']
    if s=='0' or reset==True:
        s=""
        reset=False
    label['text']=s+num
#主窗口
root=Tk()
root.wm_title("计算器")
#显示栏1
label=Label(root,text="0",background="white",anchor="e")
label['width']=35
label['height']=2
label.grid(row=1,columnspan=4,sticky=W)
#按钮
showText="789/456*123-0.C+"
for i in range(4):
    for j in range(4):
        b=Button(root,text=showText[i*4+j],width=7)
        b.grid(row=i+2,column=j)
        b.bind("<Button-1>",buttonCallBack)
showText="()"
for i in range(2):
    b=Button(root,text=showText[i],width=7)
    b.grid(row=6,column=2+i)
    b.bind("<Button-1>",buttonCallBack)
b=Button(root,text="=")
b.grid(row=6,columnspan=2,sticky="we")
b.bind("<Button-1>",buttonCallBack)
root.mainloop()
