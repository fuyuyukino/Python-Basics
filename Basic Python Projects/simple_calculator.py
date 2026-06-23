#Simple calculator with addition, subtraction, multiplication, division, and exponential

#Input for calculator
try:
    while True:
        try:
            calculator = input("Please choose between +, -, *, /, **! ")

            if calculator not in ["+","-","*","/","**"]:
                raise ValueError("Invalid operator")
            break

        except ValueError as e:
            print(e)
            print("Please enter +, -, *, /, or **!")

    a = int(input("Please enter number: "))
    b = int(input("Please enter number: "))

#Conditional for program
    if calculator == "+":
        print("Result is :", a+b)
    elif calculator == "-":
        print("Result is :", a-b)
    elif calculator == "*":
        print("Result is :", a*b)
    elif calculator == "/":
        print("Result is :", a/b)
    elif calculator == "**":
        print("Result is :", a**b)
    else:
        print("Error")

#Exception for error value and zero division
except ValueError:
    print("Please, input number")
except ZeroDivisionError:
    print("Please don't enter 0")