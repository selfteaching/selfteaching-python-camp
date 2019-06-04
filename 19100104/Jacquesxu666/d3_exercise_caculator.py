def jia(x,y):  #function for plus
    return x + y

def jian(x,y): # function for minus
    return x - y

def chen(x,y): #function for multiplus
    return x*y

def chu(x,y): #function for divide
    return x/y

print("Please choose your operation: 1 for plus,2 for minus, 3 for multiplus, 4 for divide")

selection = input("Your choice is ：")

data1 = float(input("Your first number is:"))
data2 = float(input("Your second number is :"))
if selection == '1' :

    print("the result is :",jia(data1,data2))

elif selection == '2' :
    print("the result is :",jian(data1,data2))

elif selection == '3' :
    print("the result is :",chen(data1,data2))

elif selection == '4' and data2 != 0:
    print ("the result is :",chu(data1,data2))

elif selection =='4' and data2 == 0:
    print("Your input is wrong! 0 cannot be used as divisor!")

else :
    print("Your input is wrong! please choose correct operation!")
