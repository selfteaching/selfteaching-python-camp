a = [0,1,2,3,4,5,6,7,8,9]
a.reverse()
#print(a)
b = ''.join(str(i) for i in a)#��Ҫ��������������
#print (b)
c = b[2:8]#�ַ�����Ƭȡ3��8�ַ�
#print(c)
d=c[::-1]#�ַ�����Ƭ��ʽ��ת
#print(d)
e = int(d)#�ַ���ת��ֵ
#print(e)
print("ת��Ϊ������Ϊ��", bin(e))
print("ת��Ϊ�˽���Ϊ��", oct(e))
print("ת��Ϊʮ������Ϊ��", hex(e))