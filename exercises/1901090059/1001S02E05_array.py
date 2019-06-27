
Arry =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Arry.reverse()
print(Arry)

Arry = str(Arry)
print(Arry)

Carry = []
for i in Arry:
    if i >= '2' and i <= '7' :
        Carry.append(i)
print(Carry)

Carry.reverse()
print(Carry)

ICarry = (''.join(Carry))
int(ICarry)
print(ICarry)

HexICarry = hex(int(ICarry))
OctICarry = oct(int(ICarry))
BinICarry = bin(int(ICarry))

print('HEX, OCT, BIN equals', HexICarry, OctICarry, BinICarry)
