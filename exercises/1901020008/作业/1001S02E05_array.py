example_list = [0,1,2,3,4,5,6,7,8,9]
war_list = sorted(example_list, key=lambda x: x*-1)
print(war_list)
str=''.join(str(i)for i in war_list)
print(str)

war=str[2:8]
print(war)

war2 =war[::-1]
print(war2)

int(war2)
print(war2)

x=int(war2)
bin(x)
print(bin(x))
oct(x)
print(oct(x))
hex(x)
print(hex(x))