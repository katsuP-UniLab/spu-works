class matin:
  def __init__(self, inp):
    self.inp = int(inp)

  def apk(self):
    if ((self.inp % 2) > 0):
      print(str(self.inp) + ' is odd number.')
    else:
      print(str(self.inp) + ' is even number.')
    
# Main Function
inp = ''
arrayBox = []

while (inp != 'x'):
  inp = input('Enter Number (or "x" to exit) : ')
  
  if (inp != 'x'):
    if inp.isnumeric():
      arrayBox.append(int(inp))
    else:
      print('Error: not in choice')

print()

for x in arrayBox:
  classBased = matin(x)
  classBased.apk()