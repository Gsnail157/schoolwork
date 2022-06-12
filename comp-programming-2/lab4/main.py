# Mark Boady and Matthew Burlick
# Drexel University 2020
# CS 172


import random
import time
# TODO: import CustomMonster class here
from monster import CustomMonster


def driver():
    # TODO: Get first monster's name, health, description, basicAttackDamange, specialAttackDamage, defenseDamage, defenseName here.
    # Instantiate a CustomMonster using that info.
    name = input("Enter monster 1 name:\n")
    health = input("Enter a number for monster 1 health:\n")
    description = input("Enter monster 1 description:\n")
    basicAttackDamage = int(
        input("Enter a number for monster 1 basic attack damage:\n"))
    specialAttackDamage = int(
        input("Enter a number for monster 1 special attack damage:\n"))
    defenseDamage = int(
        input("Enter a number for monster 1 defense damage:\n"))
    basicName = input("Enter monster 1 basic attack name:\n")
    specialName = input("Enter monster 1 special attack name:\n")
    defenseName = input("Enter monster 1 defense name:\n")

    first = CustomMonster(name, health, description, basicAttackDamage, specialAttackDamage, defenseDamage,
                          basicName, specialName, defenseName)  # this should be an instance of your CustomMonster class

    # TODO: Get second monster's name, health, description, basicAttackDamange, specialAttackDamage, defenseDamage, defenseName here.
    # Instantiate a CustomMonster using that info.
    name = input("Enter monster 2 name:\n")
    health = input("Enter a number for monster 2 health:\n")
    description = input("Enter monster 2 description:\n")
    basicAttackDamage = int(
        input("Enter a number for monster 2 basic attack damage:\n"))
    specialAttackDamage = int(
        input("Enter a number for monster 2 special attack damage:\n"))
    defenseDamage = int(
        input("Enter a number for monster 2 defense damage:\n"))
    basicName = input("Enter monster 2 basic attack name:\n")
    specialName = input("Enter monster 2 special attack name:\n")
    defenseName = input("Enter monster 2 defense name:\n")

    second = CustomMonster(name, health, description, basicAttackDamage, specialAttackDamage, defenseDamage,
                           basicName, specialName, defenseName)  # this should be an instance of your CustomMonster class

    winner = monster_battle(first, second)


# This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

    # first reset everyone's health!
    #####TODO######

    # next print out who is battling
    print("Starting Battle Between")
    print(m1.getName()+": "+m1.getDescription())
    print(m2.getName()+": "+m2.getDescription())

    # Whose turn is it?
    # Select Randomly whether m1 or m2 is the initial attacker
    # to other is the initial definder
    ######TODO######
    choice = random.choice([1, 2])
    if choice == 1:
        attacker, defender = m1, m2
    else:
        attacker, defender = m2, m1

    print(attacker.getName()+" goes first.")
    # Loop until either monster is unconscious (health < 1) or choose to stop.
    while(m1.getHealth() > 0 and m2.getHealth() > 0):
        # Ask the user a move among special attack, basic attack, defense or the stop.
        move = input(
            "Pick one of these (s)pecial attack, (b)asic attack, (d)efense or sto(p):")

        # It will be nice for output to record the damage done
        before_health = defender.getHealth()

        # for each of the options above, apply the appropriate attack and
        # print out who did what attack on whom
        # basic attack
        if(move.lower() == "b"):
            # Attacker uses basic attack on defender
            # and print results by calling print_results function
            ######TODO######
            attacker.basicAttack(defender)
            print_results(attacker, defender, attacker.getBasicName(),
                          attacker.getBasicAttackDamage())
            pass

        # defense attack
        elif move.lower() == "d":
            # Defend! and print results by calling print_results function
            ######TODO######
            attacker.defenseAttack(defender)
            print_results(attacker, defender, attacker.getDefenseName(),
                          attacker.getDefenseAttackDamage())

            pass
            # special attack
        elif move.lower() == "s":
            # Special Attack! and print results by calling print_results function
            ######T######
            attacker.specialAttack(defender)
            print_results(attacker, defender, attacker.getSpecialName(),
                          attacker.getSpecialAttackDamage())
            pass
        elif move.lower() == 'p':
            # stop the fight
            print("\nBattle is over. let's see who has won...")
            if m1.getHealth() > m2.getHealth():
                print(f'{m1.getName()} is victorious!')
            else:
                print(f'{m2.getName()} is victorious!')
            return

    # Print the names and healths after this round
    ######TODO######
        print(f'{attacker.getName()} at {attacker.getHealth()}')
        print(f'{defender.getName()} at {defender.getHealth()}')
    # Swap attacker and defender
    ######TODO######
        if attacker == m1:
            attacker, defender = m2, m1
        else:
            attacker, defender = m1, m2

    # Print out who won.
    # Return who won
    ######TODO######
    print("\nBattle is over. let's see who has won...")
    if m1.getHealth() > m2.getHealth():
        print(f'{m1.getName()} is victorious!')
    else:
        print(f'{m2.getName()} is victorious!')
    return
# Print status updates
####TODO####


def print_results(attacker, defender, attack, hchange):
    ####TODO####
    # Get the name of the attacker and the defender.
    # then give status updates based on the the attack. For more
    # info refer to the example trace.
    attacker = attacker.getName()
    defender = defender.getName()
    res = f'{attacker} used {attack} on {defender}\nThe attack did {hchange} damage.'
    print(res)


# ----------------------------------------------------
if __name__ == "__main__":
    # Ideally ever battle will be different
    # But for reproducability, we'll seed the random number generator as 0

    random.seed(0)
    driver()
