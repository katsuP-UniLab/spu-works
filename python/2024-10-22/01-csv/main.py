import pandas as pd

data = {"Date": [], "Name": [], "Amount": []}

total = 0

times = int(input("How many times do you want to add money usages? : "))
dates = input("Enter date : ")

for i in range(times):
    print()
    name = input("Item name : ")
    amount = int(input("Amount : "))

    total += amount

    data["Date"].append(dates)
    data["Name"].append(name)
    data["Amount"].append(amount)

    print("====================================")

df = pd.DataFrame(data) # <-- PD
df.to_csv("../expense.csv", index=False) # <-- PD

print()
print("Total Amount is ", total)
print("End Program")

# print(data)
