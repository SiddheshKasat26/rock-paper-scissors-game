rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

# for USER
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("Sorry, but you inserted wrong input. Please try again😊 (Insert 0 or 1 or 2 only).")
    

# for COMPUTER
if choice <=2 and choice >=0:
    print("Computer chose :")

    mr_x = random.randint(0,2)
    if mr_x == 0:
        print(rock)
    elif mr_x == 1:
        print(paper)
    else:
        print(scissors)

    # for results
if choice <=2 and choice >=0:
    
    if (choice != mr_x):
        if choice==0 and mr_x==2:
            print("Hurray, You Won🎉🎉🎊🎊")
        elif choice==2 and mr_x==0:
            print("Unfortunately, You Lost😔.Better Luck next time👍.")
        elif choice > mr_x:
            print("Hurray, You Won🎉🎉🎊🎊")
        else:
            print("Unfortunately, You Lost😔.Better Luck next time👍.")

    else:
        print("It's Draw😯😑.I am sure you will win next time✌.")

