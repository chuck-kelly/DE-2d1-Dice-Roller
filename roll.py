# roll a "die" some number of times.
# roll - run it once and go into a loop
# roll 1 - produce a number 1-6 random and print it
# roll 2 - produce two numbers 1-6 and print them
# roll 3 - produce three numbers and print them.
#
import random
def rand_roll():
    roll = random.randint(1,6)
    return roll

def dice_to_roll():
    while True:
        dice_to_roll = int(input('How many dice to roll? :'))
        if dice_to_roll == 0:
            break
        for i in range(dice_to_roll):
            print(rand_roll())




if __name__ == '__main__':
    print('first roll')
    print(rand_roll())
    dice_to_roll()