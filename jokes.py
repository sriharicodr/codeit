import pyjokes

while True:
    print("Welcome to the Ha Ha Ha !")
    print()
    ui = input("Do you want to hear a joke? (yes/no): ")
    print()
    ui = ui.lower()
    joke = pyjokes.get_joke()
    if ui == "yes":
        print(joke)
        print()
    elif ui == "no":
        print("Thank You for using this app!")
        print()
        quit()
    else:
        print("Please try again!")
        print()
        
        
