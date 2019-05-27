import random
number_to_guess = random.randint(1,20)

  



import sys

while True:
    for guesses in range(0,6):
        while True:
            guessed_number = input("Enter a number 1-20. You have 6 guesses.   ") 
            if guessed_number.isdigit():
                break
            else:
                print("Do you know what a number is?")
        guessed_number = float(guessed_number)

        if guessed_number > number_to_guess:
            print("Your number is too high.")
        elif guessed_number < number_to_guess:
            
            print("Your number is too low.")
        else:
            print("You're number is correct!")
            break

    if guessed_number == number_to_guess:
        print("You guessed the number in " + str(guesses)+ " guesses")
    else:
        print("You failed.")
    

    while True:
        again = input("Want to play again?")
        if again == "Yes" or again == "yes" or again == "y":
            print("okay")
            break
        elif again == "no" or again == "No" or again == "n":
            print("Cya")
            sys.exit()
        else:
            print("Type 'yes' or 'no'.")
            

