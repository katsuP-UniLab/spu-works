def math(num,a,b):
     if num == " + ":
          return a + b
     elif num == " - ":
          return a - b
     elif num == " * ":
          return a * b
     elif num == " / ":
          if b != 0:
               return a / b
          else:
               return
     else:
         return 

a = int(input("|    |"))
b = int(input("|    |"))

print("|----|: + , - , * , /")
num = input("|----|")
print(math(num, a, b))