Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  i=1
>>> while i<=9:
	j=1
	while j<=i:
		mut =j*i
		print("%d*%d=%d"%(j,i,mut), end=" ")
		j +=1
                print("")
                i+=1
                print("\r")
