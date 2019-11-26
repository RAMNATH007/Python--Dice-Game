#Assignment programs
#Main function
def Main_menu ():
  print("1: name program")
  print("2: song lyrics prog")
  print("3: displaying serval number prg")
  print("4: summation of two numbers:")
  print("5: favourite actrees or actor")
  print("6 : date format program")
  print("7: tables")
  print("8: reverse of a number")
  print("9: sum of number in a range")
  print("10: factorial")
  print("11: even or odd")
  print("12: length of list")
  print("13. quit")
  while True:
   try:
    selection=int(input("enter the choice: "))
    if selection==1:
     name()
     break
    elif selection==2:
     song()
     break
    elif selection==3:
     num()
    elif selection==4:
     sum()
    elif selection==5:
     act()
    elif selection==6:
        day()
    elif selection==7:
        tab()
    elif selection==8:
        Num_rev()
    # elif selection==9:
    #     Num_ran()
    # elif selection==10:
    #     fact()
    # elif selection==11:
    #     eve_odd()
    # elif selection==12:
    #     funct()
    elif selection==13:
        break
    else:
     print("invalid choice enter  ")
   except ValueError:
    print("invalid choice number :")
  exit()
#printig a name
def name():
 na=int(input("enter the name:"))
 print("Name is:",na)
 #printing a song lyrics
def song():
 print("1:Hall of fame song ")
 print("2. Boy friend song  ")
 print("3. Never say never")
 print("Enter any key go back to All programs")
 while True:
  try:
   select=int(input("enter the choice:"))
   if select==1:
    print("Hall of fame song lyrics:\n""Yeah, you could be the greatest\n"
   "You can be the best\n"
   "You can be the King Kong banging on your chest\n"
   "You could beat the world\n"
   "You could beat the war\n"
   "You could talk to God, go banging on his door\n"
   "You can throw your hands up\n"
   "You can beat the clock\n"
   "You can move a mountain\n"
   "You can break rocks\n"
   "You can be a master\n"
   "Don't wait for luck\n"
   "Dedicate yourself and you can find yourself\n"
   "Standing in the hall of fame\n"
   "And the world's gonna know your name\n"
   "Cause you burn with the brightest flame\n"
   "And the world's gonna know your name\n"
   "And you'll be on the walls of the hall of fame")
    break
   elif select==2:
    print("If I was your boyfriend, I'd never let you go\n"
         "I can take you places you ain't never been before\n"
         " Baby take a chance or you'll never ever know\n"
          "I got money in my hands that I'd really like to blow\n"
          "Swag swag swag\n")
    break
   elif select==3:
    print("Never say never"
          "(Never, never)"
          "Yeah, yeah"
          "See I never thought that I could walk through fire\n"
          "I never thought that I could take the burn\n"
          "I never had the strength to take it higher\n"
          "Until I reached the point of no return\n")
    break
   else:
    print("Invalid choice: Enter1-3")
    song()
  except:ValueError
  Main_menu()
  exit()
#3
def num():
 mnum=input("enter numbers to display:")
 print(mnum)
 exit()
 #4
def sum():
  a=int(input("enter a value:"))
  b=int(input("enter b value:"))
  add=a+b
  print(add)
#5
def act():
    s_d=input("Enter the favourite actrees or actor name:")
    print("favourite actrees or actor:",s_d)
#6
def day():
    while True:
        try:
            month = int(input("enter the month:"))
            date = int(input("enter the date:"))
            year = int(input("enter the year:"))
            if month > 1 and month <= 12:
                break
            else:
                print("enter valid month 1 and 12")
            if date > 1 and date < 31:
                break
            else:
                print("enter the valid date 1-31")
            if year > 2000 and year < 2019:
                break
            else:
                print("Year should be 2000-2019:")
            print(month, date, year, sep="/")
        except:NameError
        print("enter the valid choice")
        #7
def tab():
    n = int(input("Enter the table number:"))
    for i in range(1, 11):
        num = n * i
        print(n, "*", i, "=", num)
#8
def Num_rev():
    n = int(input("enter any number:"))
    while n > 0:
        n = n - 1
        print(n)
        #9
# def Num_ran():
#     counter = 0
#     for i in range(100, 200):
#         counter = counter + i
#         print(counter)
# def fact():
#     n = int(input("Enter:"))
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     print(fact)
# def eve_odd():
#     num = int(input("enter a number:"))
#     if num % 2 == 0:
#         print(num, "is an even number")
#     else:
#         print(num, "is an odd number")
# def funct():
#         lis = []
#         lis1 = [4,7,8,9,5]
#         for i in lis1:
#             lis.append(i)
#         print(lis)
#         print(len(lis))
# def ran():
#     a=[]
#     for i in range(1,1001):
#         a.append(i)
#     print(a)
# def high():
#     a = [5445, 5646, 8, 8, 9, 5, 6, 7, 5, 8, 88, 888, 44, 5, 5, 65, 1, 4, 5]
#     print(max(a))
#     print(min(a))
# def tw():
#     a=[]
#     b=[]
#     for i in range(1,100):
#         if i%2==0:
#             a.append(i)
#             print("These are the even numbers in the range of 1-100:",i)
#         else:
#             b.append(i)
#             print("These are the odd numbers in the range of 1-100:",i)
# def dict1():
#     dicts = {"India": "IN", "united states of america": "USA", "china": "chn", "srilanka": "sl"}
#     print(dicts("India"))
# def dict2():
#     dicts = {"India": "IN", "united states of america": "USA", "china": "chn", "srilanka": "sl"}
#     print(dicts.values())
#     print(dicts.keys())
# def file():
#     import os
#     f.os.open
Main_menu()

