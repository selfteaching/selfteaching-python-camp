# Filename : 1001S02E05_array.py
# author by : �Ž���

#���鷭ת
list = [0,1,2,3,4,5,6,7,8,9]
list_rev = list[::-1]
print(list_rev)

#ת�����ַ���
str1 = "".join(map(str,list_rev))
print(str1)


#ȡ��2-8��Ԫ��
str2 = str1[2:8]
print(str2)


#��ת��һ�Σ�2-8���Ľ��
str3 = str2[::-1]
print(str3)


#ת����������
str4 = int(str3)
print(str4)


#ת���ɶ����ơ��˽��ơ�ʮ������
str5 = bin(str4)
str6 = oct(str4)
str7 = hex(str4)


print(str5)
print(str6)
print(str7)