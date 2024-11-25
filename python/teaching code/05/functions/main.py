def cal(no1, no2, op):
  if (op == 1):
    return(int(no1) + int(no2))
  elif (op == 2):
    return(int(no1) - int(no2))
  elif (op == 3):
    return(int(no1) * int(no2))
  elif (op == 4):
    if (no2 != 0):
      return(int(no1) / int(no2))
    else:
      return 'Unexpected Error: Divided by 0'
  else:
    return('nothing')

in1 = input("Enter number #1 : ")
in2 = input("Enter number #2 : ")

print('1. +')
print('2. -')
print('3. *')
print('4. /')
op = input("Enter operator : ")

print(cal(in1, in2, op))