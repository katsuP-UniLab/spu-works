exit = ""
total = 0

for i in range(2):
    exit = ""
    customer_total = 0

    print("1. asd -- 20thb")
    print("2. water -- 10thb")
    print("0. End")

    while exit != "exit":
        inp = int(input("Enter the Menu : "))

        if inp != 0:
            if inp == 1:
                customer_total += 20
            elif inp == 2:
                customer_total += 10
            else:
                print("Error: There's no menu.")

        elif inp == 0:
            print("customer total = " + str(customer_total))
            total += customer_total
            exit = "exit"

        else:
            print("Error: There's no menu.")

        print("")

    print("----------")
    print("")

print("Daily total = " + str(total))
