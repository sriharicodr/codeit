#Import python modules.
import pywhatkit
import wikipedia
print("PY WIKI")
print()
#Print guide so that the user know what to type.
print("Search something like who is _ or what is _.")
print()
#Put in a continuous loop.
while True:
    #User search here ⬇️
    search = input("Search🔍: ").lower()
    #Remove unwanted parts from the input.
    if 'who is' in search:
        person = search.replace('who is', '')
        #Getting the result
        info1 = wikipedia.summary(person, 1)
        print(info1)
    elif 'what is' in search:
        thing = search.replace('what is', '')
        #Getting the result
        info2 = wikipedia.summary(thing, 1)
        print(info2)
    #To know the user want to continue or quit.
    yn = input("Do you want to continue searching?(y/n): ").lower()
    if yn=='y' or yn=='yes':
        print()
    elif yn=='n' or yn=='no':
        quit()
