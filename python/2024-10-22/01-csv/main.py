import pandas as pd

data = {
  "Date": [],
  "Name": [],
  "Amount": []
}

total = 0

# data['amount'].append(100)

times = int(input('How many times do you want to add money usages? : '))
dates = input('Enter date : ')

for i in range(times):
  print()
  name = input('Item name : ')
  amount = int(input('Amount : '))
  
  total += amount
  
  data['date'].append(dates)
  data['name'].append(name)
  data['amount'].append(amount)
  
  print('====================================')
  
df = pd.DataFrame(data)
df.to_csv('../expense.csv')

print()
print('Total Amount is ', total)
print('End Program')

# print(data)