# Filename : 1001S02E03_calculator
# author by : �Ž���

# ���庯��
def add(x, y):
    """���"""
    return x + y

def subtract(x, y):
    """���"""
    return x - y

def multiply(x, y):
    """���"""
    return x * y

def divide(x, y):
    """���"""
    return x / y

########################################################
status = 1

# �û�����
print("ѡ�����㣺")
print("1�����","2�����","3�����","4�����")
print("\n")

choice = input("�������ѡ��(1/2/3/4):")
choice_int = int(choice)


if choice_int > 4:
    status = 0
    print("�Ƿ�����")
    
    

if(status == 1):
    num1 = int(input("�����һ������: "))
    num2 = int(input("����ڶ�������: "))
    
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
    
    

