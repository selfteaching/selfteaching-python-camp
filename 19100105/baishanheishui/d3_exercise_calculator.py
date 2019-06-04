argv = input('请输入：X+Y，或X-Y,或X*Y，或X/Y') 
while(argv):
    print(argv,'=:')
    if argv[1] == '+':
        print(int(argv[0]) + int(argv[2]))
    elif argv[1] == '-':
      print(int(argv[0]) - int(argv[2]))
    elif argv[1] == '*':
      print(int(argv[0]) * int(argv[2]))
    elif argv[1] == '/':
      print(int(argv[0]) / int(argv[2]))
    else:
      print("出错")
    argv = input('请继续输入：X+Y，或X-Y,或X*Y，或X/Y') 