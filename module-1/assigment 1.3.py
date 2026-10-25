# Name: Jonathan Guadron
# Date: October 25, 2026
# Assignment: 1.3 - On the Wall + Flowcharts
# Purpose: Count down the bottles and remind the user to buy more beer.
# Reference: W3Schools Python Functions, While Loops, and Try Except.
# https://www.w3schools.com/python/python_functions.asp
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_try_except.asp


# Count backward and show the song for each bottle.
def countdown_bottles(starting_bottles):
    bottles_remaining = starting_bottles

    while bottles_remaining >= 1:
        # Use bottle when there is only one left.
        if bottles_remaining == 1:
            print('1 bottle of beer on the wall, 1 bottle of beer.')
            print('Take one down and pass it around, '
                  '0 bottles of beer on the wall.')
        else:
            print(f'{bottles_remaining} bottles of beer on the wall, '
                  f'{bottles_remaining} bottles of beer.')

            # Find how many bottles are left after taking one down.
            bottles_after_drinking = bottles_remaining - 1

            # Use the correct word for the number left on the wall.
            if bottles_after_drinking == 1:
                print('Take one down and pass it around, '
                      '1 bottle of beer on the wall.')
            else:
                print('Take one down and pass it around, '
                      f'{bottles_after_drinking} bottles of beer on the wall.')

        # Leave a blank line and subtract one bottle.
        print()
        bottles_remaining = bottles_remaining - 1


# Keep asking until the user enters a whole number of at least 1.
valid_input = False

while not valid_input:
    try:
        # Ask how many bottles are on the wall.
        starting_bottles = int(input('Enter number of bottles: '))

        # Check that the number is at least 1.
        if starting_bottles >= 1:
            valid_input = True
        else:
            print('Please enter a whole number of 1 or greater.')

    # Show an error if the input cannot be changed to an integer.
    except ValueError:
        print('Please enter a whole number of 1 or greater.')


# Send the number of bottles to the countdown function.
countdown_bottles(starting_bottles)

# Remind the user to buy more beer after the song ends.
print('Time to buy more bottles of beer.')