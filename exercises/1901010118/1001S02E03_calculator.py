var = 1
while var == 1:
  num = float(input("please input a number:"))
  nums = float(input("please input a number:"))
  numf = float(input("please input a command:"))
  if numf == 1:
      print(num*nums)
  elif numf == 2:
      print(num/nums)
  elif numf == 3:
      print(num+nums)
  else :
      print(num-nums)