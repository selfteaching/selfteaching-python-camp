# Multiplication_table
for x in range(1,10):
  for y in range(1, x + 1):
    print(x, "*", y, "=", x * y, sep="", end="\t" )
  print()

# Multiplication_table_odd
x = 1
while x < 10:
  y = 1
  if x % 2 != 0:
    while y <= x:  
      print(x, "*", y, "=", x * y, sep="", end="\t")
      y = y+1
    print()
  x = x+1
  

