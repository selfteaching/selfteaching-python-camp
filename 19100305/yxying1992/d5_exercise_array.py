shuzu=[0,1,2,3,4,5,6,7,8,9]
shuzu.reverse() #�����鷭ת
print(shuzu)

s = ''      #��ת�������ƴ�ӳ��ַ�������һ
for i in range(0,10):  
    shuzu[i]=str(shuzu[i])
zifucuan=s.join(shuzu)
print(zifucuan)

#zifucuan=str(shuzu[0]) #��ת�������ƴ�ӳ��ַ���������
#for i in range(1,10):   
#    zifucuan =zifucuan+str(shuzu[i])
#print(zifucuan)

r1=zifucuan[2:8]  #����Ƭ��ʽȡ���������ڰ˸��ַ�
print(r1)
zhengshu=int(r1[::-1])  #���ַ������з�ת����ת��Ϊint����
print(zhengshu)
print(bin(zhengshu),oct(zhengshu),hex(zhengshu))    #ת���ɶ����ơ��˽��ơ�ʮ������