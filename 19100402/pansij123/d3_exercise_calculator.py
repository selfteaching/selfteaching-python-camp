import sys

ans = 1
if len(sys.argv)!=4:
        print("use like this\npython3 d2_xxx.py 1 jia 1\njia can be jia, jian, cheng, chuyi")

if sys.argv[2] == 'jia':
        print(sys.argv[1], '+', sys.argv[3],end='')
        ans=float(sys.argv[1])+float(sys.argv[3])
        if ans%1 == 0:
                ans=int(ans)
        print(' =', ans)
elif sys.argv[2] == 'jian':
        print(sys.argv[1], '-', sys.argv[3],end='')
        ans=float(sys.argv[1])-float(sys.argv[3])
        if ans%1 == 0:
                ans=int(ans)
        print(' =', ans)
elif sys.argv[2] == 'cheng':
        print(sys.argv[1], '*', sys.argv[3],end='')
        ans=float(sys.argv[1])*float(sys.argv[3])
        if ans%1 == 0:
                ans=int(ans)
        print(' =', ans)
elif sys.argv[2] == 'chuyi':
        if float(sys.argv[3]) == 0.0:
                print("Cannot divide a number by zero (even your PE teacher taught you maths)")
        else:
                print(sys.argv[1], '/', sys.argv[3],end='')
                ans=float(sys.argv[1])/float(sys.argv[3])
                if ans%1 == 0:
                        ans=int(ans)
                print(' =', ans)
else:
        print("Only jia jian cheng chuyi. Thank you.")
