txt1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
txt2 = txt1.reverse()
#print (txt1)
txt3 = "".join(str(i) for i in txt1)
#print(txt3)
txt4 = txt3[3:9]
#print(txt4)
txt5 = txt3[::-1]
#print(txt5)
txt6 = int(txt5)
#print(txt6)
txt7 = bin(txt6)
print(txt7)
txt8 = oct(txt6)
print(txt8)
txt9 = hex(txt6)
print(txt9) 
