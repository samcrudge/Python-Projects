import random


class Dice:

    """self.PlayerChoice is collection user input"""
    def __init__(self):
        self.PlayersChoice = 0
        self.intro()

    'Intro to the application thats called on running Application'
    def intro(self):
        print('Please Select a dice by the number of sides desired to roll.\nYour options are:\n2\n4\n6\n8\n12\n16\n18\n20\n100')

    'Takes user input and validates'
    def getPlayerOption(self):
        while self.PlayersChoice == 0:
            self.PlayersChoice = int(input("Please select your number of sides: \n"))
            if self.PlayersChoice not in [2, 4, 6, 8, 12, 16, 18, 20, 100]:
                print("Please choose a valid choice.")
                self.PlayersChoice = 0

    '''output is the generated dice roll based on self.PlayerChoice variable'''
    def roll(self):
        output = random.randrange(1, self.PlayersChoice)
        return output


a = Dice()
a.getPlayerOption()
print(a.roll())
