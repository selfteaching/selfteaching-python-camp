# Filename : multiplication_table.py
# Author by : Evans

#Task1 : Use for in list the multiplication_table
print("Multiplication_table:")
for i in range(1,10):
    for j in range (1,i+1):
        print ('{}x{}={}\t'.format(i,j,i*j),end='')
    print ('')
print('\n')



#Task2 : Only show the odd line of the multiplication_table
print('Odd line of the Multiplication_table:')
for i in range(1,10):
    if i % 2 == 0 :
        i += 1 
        continue
    for j in range(1,i+1):
            print('{}x{}={}\t'.format(i,j,i*j),end='')
    print('')



