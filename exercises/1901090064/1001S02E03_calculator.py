import random
count = 0
right = 0
op = ['+','-','*','/']

while True:
    a= random.randint(0,9)
    b= random.randint(0,9)
    s = random.choice(op)
    print('%d %s %d = ' %(a,s,b))
    question = input('请输入您的答案:(q退出)')
    if s == '+':
        result = a + b
    if s == '-':
        result = a - b
    if s == '*':
        result = a * b
    if s == '/':
        result = a // b
    if question == str(result):
        print('回答正确')
        right += 1
        count += 1
    elif question == 'q':
        break
    else:
        print('回答错误')
        count += 1

percent = right / count
print('测试结束,共回答%d道题,正确个数为%d,正确率为%.2f%%' %(count,right,percent * 100))