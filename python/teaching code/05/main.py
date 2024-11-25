out = 0
exitPrompt = ""


def cal(no1, no2, op):
    if op == 1:
        return int(no1) + int(no2)
    elif op == 2:
        return int(no1) - int(no2)
    elif op == 3:
        return int(no1) * int(no2)
    elif op == 4:
        try:
            return int(no1) / int(no2)
        except ZeroDivisionError:
            return "Error: Divided by 0"

    else:
        return "nothing"


while out != 1:
    in1 = 0
    in2 = 0
    op = 0

    while True:
        try:
            in1 = int(input("Enter number #1 : "))
        except ValueError:
            print("Enter a valid value!!")
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            break

    while True:
        try:
            in2 = int(input("Enter number #2 : "))
        except ValueError:
            print("Enter a valid value!!")
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            break

    while True:
        try:
            print("1. +")
            print("2. -")
            print("3. *")
            print("4. /")
            op = int(input("Enter operator : "))
        except ValueError:
            print("Enter a valid value!!")
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            if op < 5 & op > 0:
                break
            else:
                print("Enter the valid Number on the choice!")
                print("")

    print(cal(in1, in2, op))

    print("")
    while True:
        try:
            exitPrompt = input("Do you want to end Program? (Y/n) : ")
        except ValueError:
            print("Enter a valid value!!")
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            if op == "Y" | op == "y" | op == "n" | op == "N":
                out = 1
                break
            else:
                print("Enter the valid choice!")
