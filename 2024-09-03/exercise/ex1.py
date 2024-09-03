s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
v = ["A", "E", "I", "O", "U"]

alphabet =list(s)

for i in range(len(alphabet)):
  for j in range(len(v)):
    if alphabet[i] == v[j]:
      print('Location of ' + v[j] + ' is at ' + str(i))
      break