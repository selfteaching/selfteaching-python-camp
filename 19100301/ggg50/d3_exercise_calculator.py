operator = input("""\
What you want? I can do these things: 
1.+
2.-
3.*
4./
""")

number_f = int(input("Enter a number"))
number_s = int(input("Enter another number"))

if operator == "1":
  print(number_f + number_s)
elif operator == "2":
  print(number_f - number_s)
elif operator == "3":
  print(number_f * number_s)
elif operator == "4":
  print(number_f / number_s)


