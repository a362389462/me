"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("Hello! Welcome to the guessing game!")
    print("We gonna gusee a number here! ")
    print("Let's just put a smallest number in this guessing range first!")
    lowerBound = input("Enter a number here to be the smallest you think: ")

    upperBound = input("Enter a number here to be the biggest you think: ")

    print(" Are you ready? A number between 0 and {}?".format(upperBound))

    upperBound = int(upperBound)

    true_age = random.randint(0,upperBound)

    guessed = False

    while not guessed:
      num = int(input("Guess a number: "))
      if num == true_age:
        print("Yes it is!")
        guessed = True
      elif num < true_age - 5:
        print("You guessed too small! try again!")
      elif num > true_age + 5:
        print("You guessed too big! try again!")
      elif true_age - 5 <= num <= true_age + 5:
        print("Close! very close! You almost there!")


    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
