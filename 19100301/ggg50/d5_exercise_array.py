num_list = [0,1,2,3,4,5,6,7,8,9]
# change into string list 
string_list = [str(x) for x in num_list]

# Reverse
string_list.reverse()   

# Changing list into string, and slicing from 2 to 8(acturlly3 to 9)
text = "".join(string_list)[2:8]
print(text) # 765432

# Text reverse
text_reverse = text[::-1]

# change into bin, oct, hex ...
number_dec = int(float(text_reverse))
number_bin = bin(number_10)
number_oct = oct(number_10)
number_hex = hex(number_10)
