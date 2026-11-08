# Name: Jonathan Guadron
# Date: November 7, 2026
# Assignment 3.2: Brownfield + Flowchart(s)
# Purpose: Play Cho-Han with a 12% house fee and a bonus on rolls of 2 or 7.
# Reference: Al Sweigart, The Big Book of Small Python Projects.
# https://nostarch.com/big-book-small-python-projects

"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# Explain the bonus before the player places a bet.
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
If the dice add up to 2 or 7, you get a 10 mon bonus.
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('jg: ')  # Use my initials for the wager prompt.
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han.
    while True:
        bet = input('jg: ').upper()  # Use my initials for the guess prompt.
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results.
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Use the dice total to determine whether the roll is even or odd.
    rollTotal = dice1 + dice2
    rollIsEven = rollTotal % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results.
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot
        # Collect 12 percent of the bet, rounded down to whole mon.
        houseFee = pot * 12 // 100
        print('The house collects a', houseFee, 'mon fee.')
        purse = purse - houseFee
    else:
        purse = purse - pot
        print('You lost!')

    # Award the bonus before checking the purse, even if the player lost.
    if rollTotal == 2 or rollTotal == 7:
        print('You rolled a total of', rollTotal, 'and got a 10 mon bonus!')
        purse = purse + 10

    # Check if the player has run out of money.
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
