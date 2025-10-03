import random

#Goal: Build a "guess the number" game.

#Requirements:

#The program should randomly select a number between 1 and 100.
#Use a loop to allow the user to keep guessing until they get the right number.
#After each guess, provide feedback: "Too high," "Too low," or "Correct!"
#Keep track of the number of guesses the user has made and print it when they win.
#Store the user's guesses in a list.

def guess_the_number():
        secret_number = random.randint(1, 100) # Ensures that the numbers we work with are between 1 and 100.
        guess = 0 # Just a variable to catch the user inputs to later be added in the list.(variable not necessary)
        total_guesses = [] # Stores all the guesses the user has until they find the number.
        
        while True:
                try:
                        guess = int(input("Enter your guess: "))
                except ValueError: 
                        print("You need to type in a number to continue!")
                        continue

                if guess > 100 or guess < 1:
                        print("Number has to be bewtween 1 and 100!")
                        print("Try again!")
                        continue

                total_guesses.append(guess)

                if guess < secret_number:
                        print("Too low!")
                        
                elif guess > secret_number:
                        print("Too high!")
                        
                else:
                        print(f"\nThe correct answer was {secret_number}!")
                        print(f"You got it in {len(total_guesses)} tries!")
                        print("You won 1 billion dollars!!! Congratulations check your bank account!!!")
                        break
        # Below is some additional code for the user to be able to quit the game if theyd like to or not
        # TODO: in the future maybe add some code for difficulities(Hard, Medium and Easy difficulity at the beginning of the game)
        while True:
                play_again = input("\nDo you want to play another round? ")
                if play_again.lower() == "yes":
                        guess_the_number()
                elif play_again.lower() == "no": 
                        print("Thanks for playing!")
                        break
                else:
                        print("Enter either Yes or No to continue: ")

                
guess_the_number()

