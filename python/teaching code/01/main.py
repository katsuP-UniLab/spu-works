arr = []

for i in range(1):
    name = input("Enter your name : ")
    sName = input("Enter your surname : ")
    sID = str(input("Enter Student ID : "))
    age = int(input("Enter Age : "))
    height = int(input("Enter height (in cm.) : "))
    weight = int(input("Enter weight (in kg.) : "))

    BMI = weight / ((height / 100) * (height / 100))

    store = {
        "name": name,
        "sName": sName,
        "sID": sID,
        "age": age,
        "height": height,
        "weight": weight,
        "BMI": BMI,
    }

    arr.append(store)

    print()
    print("------------------------")
    print()

for i in arr:
    print(i["sID"] + " " + i["name"] + " " + i["sName"])
    print(str(i["age"]) + " " + str(i["height"]) + "cm " + str(i["weight"]) + "kg")
    print(f"%.2f", i["BMI"])
