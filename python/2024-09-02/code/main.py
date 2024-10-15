name = input("Type your name : ")
age = input("Age : ")
height = input("height (In cm.) : ")

print("")
print("==============================")
print("")

age = int(age) + 10
height = int(int(height) + (int(height) * 5 / 100))

print("Next 10 Years. Your age gonna be %d" % age)
print("and your height gonna be %d" % height)
