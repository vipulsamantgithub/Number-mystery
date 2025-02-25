# We are going to write a program that generates a random number and ask the user to 
# guess it.

"""
    If the player guess is higher than the actual number, the program displays "Lower 
    number please." Similarly is the user guess is too low, the program prints "Higher 
    number please." When the user guess the correct number, the program displays the 
    number of guesses the player used to arrive at the number.
"""
from random import randint
class Random_number():
    def __init__(self):
        self.n=randint(1,50)
    def guess(self):
        count=0
        while True:
            try:
                user_input=int(input("Guess the number between 1-50: "))
                count+=1
                if user_input<1 or user_input>50:
                    print("You guessed out of range. Please guess withing the range.")
                elif user_input<self.n:
                    print("Higher number please.")
                elif user_input>self.n:
                    print("Lower number please.")
                else:
                    print(f"Congratulations! You guessed the right number {self.n} in {count} attempt.")
                    break
            except ValueError:
                print("Invalid value! Please enter the valid number.")
a=Random_number()
a.guess()
