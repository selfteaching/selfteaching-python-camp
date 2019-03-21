def jisuanqi():
 print("请您依次输入两个数字，你将得到这两个数字的基本的加减乘除运算的结果")
 a=float(input('请输入第一个数字'))
 b=float(input('请输入第二个数字'))
 print('请通过输入1，2，3，4进行您想要的运算：1、加法  2、减法  3、乘法  4、除法')
 x=int(input('请输入第二个数字'))
 c=a+b
 d=a-b
 e=a*b
 f=a/b
 if x==1:
     print("您的运算结果为",c)
 elif x==2:
     print("您的运算结果为",d)
 elif x==3:
     print("您的运算结果为",e)
 elif x==4:
     print("您的运算结果为",f)
 else:
     print("出错")




 print("另外还可以告诉您：第一个数加上第二个数等于:", c )
 print("另外还可以告诉您：第一个数减去第二个数等于:", d ) 
 print("另外还可以告诉您：第一个数乘以第二个数等于:", e )
 print("另外还可以告诉您：第一个数除以第二个数等于:", f )
jisuanqi()

