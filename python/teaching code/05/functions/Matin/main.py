def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2 if num2 != 0 else "Error: Divided by 0"
    
def main():
    num1 = float(input("num 1: "))
    num2 = float(input("num 2: "))
    operator = input("มึงเลือกมาสิจะทำอะไร (+, -, *, /): ")
    print(f"เท่ากับมึงได้คำตอบล่ะ: {calculate(num1, num2, operator)}")
    print("------------จบโปรแกรม------------")
    print("------------Here what is me-------------")
    print("-------------อยากตายจ้า---------------")
if __name__ == "__main__":
    main()