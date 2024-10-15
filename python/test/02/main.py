arr = []
total = 0

for i in range(5):
    inp = int(input("Input Number " + str(i + 1) + " : "))
    total += inp
    arr.append(inp)

print("All Number : " + str(arr))

arr.sort()

print("Min Number : " + str(arr[0]))
print("Max Number : " + str(arr[4]))
print(total)
