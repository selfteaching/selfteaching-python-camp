#<<<<<<< master
def multiplication_table_for():
    for i in range(1,10):
        for j in range(1,10):
            if i >= j:
                print("{}*{}={}".format(i,j,i*j),end="  ")
        print ()
def multiplication_table_while():
    i=1  # i是行
    j=1  # j是列 
    while i < 10 :
        if i % 2 !=0:           #去掉偶数行
            while j<10:         #每一行都从第一列运算到第九列
                if i >= j:
                    print("{}*{}={}".format(i,j,i*j),end="  ")
                j +=1
            print()    
        i +=1 #递增到新的一行
        j=1   #每行运算到第九列后，到新的一行就要从第一列开始
            
multiplication_table_for() 

multiplication_table_while()
#=======
def multiplication_table_for():
    for i in range(1,10):
        for j in range(1,10):
            if i >= j:
                print("{}*{}={}".format(i,j,i*j),end="  ")
        print ()
def multiplication_table_while():
    i=1  # i是行
    j=1  # j是列 
    while i < 10 :
        if i % 2 !=0:           #去掉偶数行
            while j<10:         #每一行都从第一列运算到第九列
                if i >= j:
                    print("{}*{}={}".format(i,j,i*j),end="  ")
                j +=1
            print()    
        i +=1 #递增到新的一行
        j=1   #每行运算到第九列后，到新的一行就要从第一列开始
            
multiplication_table_for() 

multiplication_table_while()
#>>>>>>> master
