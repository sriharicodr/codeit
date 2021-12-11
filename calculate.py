while True:
    print("Welcome to Simply calculate!")
    print()
    num1 = float(input("Please enter your first value: "))
    print()
    num2 = float(input("Please enter your second value: "))
    print()
    print("+,-,*&/")
    print()
    opretor = input("Please give opretor here: ")

    if opretor == "+":
        print("Your result: ",num1+num2)
    elif opretor == "-":
        print("Your result: ",num1-num2)
    elif opretor == "*":
        print("Your result: ",num1*num2)
    elif opretor == "/":
        print("Your result: ",num1/num2)
    else:
        print("Please try again!")
    print()
    print("Do you want to calculate again? (yes/no): ")
    yn = input("Please type here: ")
    if yn == "yes":
        print()
    elif yn == "no":
        print("Thank You for using SimplyCalculate! ")
        quit()

