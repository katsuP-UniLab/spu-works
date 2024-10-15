arr = []

while True:
    print("=================== BMI Calculator ===================")
    print("1. Calculation")
    print("2. Show Data")
    print("3. Exit Program")

    inp = int(input("Please choose 1-3 : "))

    if inp == 1:
        name = str(input("Please input your name : "))
        height = int(input("Please input your height (in cm.) : "))
        weight = int(input("Please input your weight (in kg.) : "))
        detail = ""

        BMI = round(weight / ((height / 100) * (height / 100)), 2)

        if BMI < 18.5:
            detail = "ต่ำกว่าเกณฑ์"
        elif BMI >= 18.5 and BMI < 23.0:
            detail = "สมส่วน"
        elif BMI >= 23.0 and BMI < 25:
            detail = "น้ำหนักเกิน"
        elif BMI >= 25.0 and BMI < 30.0:
            detail = "โรคอ้วน"
        else:
            detail = "โรคอ้วนอันตราย"

        print("Your BMI is " + str(BMI) + " " + detail)

        store = {
            "name": name,
            "height": height,
            "weight": weight,
            "BMI": BMI,
            "detail": detail,
        }

        arr.append(store)

    elif inp == 2:
        for i in range(len(arr)):
            print(
                str(i + 1)
                + "\t"
                + str(arr[i]["name"])
                + "\t"
                + str(arr[i]["height"])
                + "\t"
                + str(arr[i]["weight"])
                + "\t"
                + str(arr[i]["BMI"])
                + "\t"
                + str(arr[i]["detail"])
            )
    elif inp == 3:
        exit = str(input("Do you want to exit BMI Calculator (Y/N)?"))

        if exit == "Y" or exit == "y":
            print("Thank You")
            break
    else:
        print("There is no option that you selected.")
