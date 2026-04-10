import sys #sys.exit() is important when you want the program to exit in an if else program instead of using a while loop in a code
import random
from enum import Enum
class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3
# WITHOUT USING ENUM
# userInput= input('WELCOME TO MY ROCK, PAPER, SCISSSORS GAME.\n Choose 1 for rock.\n Choose 2 for paper.\n choose 3 for scissors: ')
# user= int(userInput)
# if user < 1 or user > 3:
#    sys.exit('enter a number 1,2,3.')
# computerChoice= random.choice("123")
# computer= int(computerChoice) 
# print(f'you chose {userInput} and the phyton chose {computerChoice}.\n')
# print('')
# if user == 1 and computer== 3:
#     print('CONGRATS🙌🙌🙌 YOU WON!')
# elif user == 2 and computer== 1:
#     print('CONGRATS 🙌🙌🙌 YOU WON!')
# elif user == 3 and computer== 2:
#     print('CONGRATS 🙌🙌🙌 YOU WON!')
# elif user == computer:
#     print('A DRAW!😂😂😂')
# else:
#     print("PHYTON DOMINATES!!!!!!!!!!!!!!!!!😒😒😒😒")


#USING ENUM
userInput= input('WELCOME TO MY ROCK, PAPER, SCISSSORS GAME.\n Choose 1 for rock.\n Choose 2 for paper.\n choose 3 for scissors: ')
user= int(userInput)
if user < 1 or user > 3:
   sys.exit('enter a number 1,2,3.')
computerChoice= random.choice("123")
computer= int(computerChoice) 
print(f'you chose {str(RPS(user)).replace('RPS.', '')} and the phyton chose {str(RPS(computer)).replace('RPS.', '')} .\n')
print('')
if user == 1 and computer== 3:
    print('CONGRATS🙌🙌🙌 YOU WON!')
elif user == 2 and computer== 1:
    print('CONGRATS 🙌🙌🙌 YOU WON!')
elif user == 3 and computer== 2:
    print('CONGRATS 🙌🙌🙌 YOU WON!')
elif user == computer:
    print('A DRAW!😂😂😂')
else:
    print("PHYTON DOMINATES!!!!!!!!!!!!!!!!!😒😒😒😒")