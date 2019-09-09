def add(x,y):
       return x+y
    

def decline(x,y):
    return x-y
   

def multiply(x,y):   
    return x*y
   
def divide(x,y):
       return x/y
   
num1=int(input("输入第一个数字："))
 
mothod=raw_input（"请输入运算符："）


num2=int(input("输入第二个数字："))


   if mothod=="+":
      print(num1,mothod,add(num1,num2))
     elif mothod=="-":
          print(num1,mothod, decline(num1,num2))
     elif mothod=="*"：
        print(num1,mothod, multiply(num1,num2))
    elif mothod=="/":
        print(num1,mothod, divide(num1,num2))
    else:
        print("输入有误")
        

   

           
