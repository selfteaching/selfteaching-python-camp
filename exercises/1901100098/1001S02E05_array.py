#�������������ת��
#������ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ��ת
sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
reversed_list = sample_list[::-1]
print('�б�ת==>',sample_list)

#��ת�������ƴ�ӳ��ַ���
#����''�����ַ�����str ���͵� join �������������б����Ԫ�أ���''�����ַ�������ʾ���ӵ�ʱ��Ԫ�ؼ䲻���κ��ַ�����
#��Ϊrebersed_list ��߶���int ����Ԫ�أ�����ƴ��֮ǰҪ��rebersed_list ���һ������str����Ԫ�ص��б�
joined_str =''.join([str(i) for i in reversed_list])
print('��ת����ַ�ƴ�ӳ��ַ���',joined_str)

# 3 ���ַ�����Ƭ�ķ�ʽȡ����3����8���ַ���������3����8���ַ���
# ��Ƭʱ�������ʼ��������������β���� 
sliced_str = joined_str[2:8]
print('���ַ�����Ƭ�ķ�ʽȡ����3����8���ַ�==>',sliced_str)

#4 ��õ��ַ������з�ת
reversed_str = sliced_str[::-1]
print('�ַ������з�ת==>',reversed_str)

# 5 ת���� int ����
int_value = int(reversed_str)

print('ת����int����==��',int_value)

print('ת���ɶ�����==>',bin(int_value))
print('ת���ɰ˽���==>',oct(int_value))
print('ת����ʮ������==>',hex(int_value))