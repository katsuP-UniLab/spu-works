def q( a , b ):
    return a + b

def w( a , b ):
    return a - b

def e( a , b):
    return a * b

def r( a , b):
    if b != 0:
        return a / b
    else:
        return "ค ว ย"

Num1 = int(input("ควย1"))
Num2 = int(input("ควย2"))

print("1. +")
print("2. -")
print("3. *")
print("4. /")

cco = input("เลือกซะไอควาย")

if cco == "1":
    m = q(Num1 , Num2)
    print (m)
elif cco == "2":
    m = w(Num1 , Num2)
    print(m)
elif cco == "3":
    m = e(Num1 , Num2)
    print (m)
elif cco == "4":
    m = r(Num1 , Num2)
    print (m)
else:
    print ("เอ๋อเหี้ยไร")