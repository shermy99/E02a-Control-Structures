#!/usr/bin/env python3
import sys, random #imports random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7" #checks to make sure the user is using the right version of python 


print('Greetings!') #prints the string
colors = ['red','orange','yellow','green','blue','violet','purple'] #creates the variable colors with the following colors
play_again = '' #creates the variable "play again"
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): #creates a loops that only ends when the player responds with no or n to play again
    match_color = random.choice(colors) #creates the variable "match_color"
    count = 0 #creates the variable count
    color = '' #creates the variable "color"
    while (color != match_color): #creates another loop that doesnt end until color = match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line  #ask the player "what is my favorite color" and waits for an input from the user
        color = color.lower().strip() #sets the variable color so that whatever the player inputs will become lower case and will remove spaces before and after the input
        count += 1 #adds plus 1 to the count variable whenever the user makes a guess
        if (color == match_color): #creates an if statement that is only true when the color variable = the match_color variable
            print('Correct!') #prints out "correct"
        else: #creates an else statement that only happens if the if statement is false
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #tells the user they were wrong and how many guesses they've tried
    
    print('\nYou guessed it in {} tries!'.format(count)) #prints this if the user was correct and tells them how many guesses they got it in

    if (count < best_count): #creates an if statement that is only true if the current amount of guesses is smaller than the lowest amount of guesses the user has gotten the correct answer in so far
        print('This was your best guess so far!') #prints the string
        best_count = count #makes best_count the new lowest amount of guesses

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #asks the user if they want to play again, and it waits for their input

print('Thanks for playing!') #if the player says no to the previous question, it prints this string