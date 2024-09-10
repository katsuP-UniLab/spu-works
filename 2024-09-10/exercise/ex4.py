arr = []
calc = 0

for i in range(5):
    inp = input('Enter Number : ')
    arr.append(int(inp))
    
print('')
    
for i in range(len(arr)):
    print("In Location " + str(i) + " is " + str(arr[i]))
    calc += arr[i]
    
arr.sort()

print('')
print('The lowest number is ' + str(arr[0]))
print('The highest number is ' + str(arr[len(arr) -1]))
print('The summation of the above number is ' + str(calc))