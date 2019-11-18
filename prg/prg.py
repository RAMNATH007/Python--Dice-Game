def die():
    try:
        print("Do you want to roll a dice\n=> Enter 1 To roll the dice\n=> Enter any key to Exit")
        selection=int(input("Enter your choice:"))
        while True:
                if selection<3:
                    dice()
                    print("=> Enter 2 to roll again\n=> Enter any key to exit")
                    hi=(int(input("Enter your choice:")))
                else:
                    print("Thanks for playing")

                    break
    except ValueError:
        print("Thank you")
def dice():
    import random
    for i in range(1):
        c = (random.randint(0,6))
        print("Dice value is:", c)
die()
