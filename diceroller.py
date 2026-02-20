#A game that generates a random dice roll of of two die
#It prints a tuple when we Tell it to roll by saying Y or y doesnt matter we change the case
#and n to exit the program and any other key is considered as an invalid input
import random

def rolldice():
    tup = (random.randint(1,6),random.randint(1,6))
    return tup

while True:
    choice = input("Do you want to roll a pair of die : y to agree or n to exit : ")
    choice = choice.lower()

    if choice == "y":
        print(rolldice())
    elif choice == "n":
        print("Exiting....")
        break
    else: 
        print("Invalid Choice!")
