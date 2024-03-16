import random
your_turn = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_turn = random.randint(0,2)

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""



if your_turn == 0:
    print( rock)
elif your_turn == 1:
    print(paper)
else:
    print(scissors)

#implementing the conditions
if computer_turn == 0:
    print('computer chose: ', rock)
elif computer_turn == 1:
    print('computer chose: ',paper)
else:
    print('computer chose: ',scissors)



if computer_turn == your_turn:
    print('Draw')
elif computer_turn == 0 and  your_turn ==1:
    print('you won')
elif computer_turn == 1 and your_turn == 0:
    print('You won')
elif computer_turn == 2 and your_turn == 0:
    print('you won')
else:
    print('You lost!')


#instructor's method:
