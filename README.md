
# E02a-Control-Structures

Let's start experimenting with some Python code! This is a set of exercises for MSCH-C220; they should give you the tools to help build your first game.

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.

Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do? I expect it to first make sure the right version of python is running, then it will print greeting and ask "what is my favorite color?"
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened. nothing happened when i answered the question

  - What do you think the program did with what you typed in answer to the question? It stored the answer in the instance for anything that would need what the user inputted

- Open main02.py. Before running it, describe how this is different than main01.py. the input is now used to describe a variable and the program prints that variable.

  - What do you think the color = input() will do? It will ask the user "what is my favorite color?" and then print whatever the user inputed

  - Run the program in the terminal and answer the question. Did the program do what you expected? Yes it did

- Open main03.py. Before running it, describe how this is different than main02.py. there are if and else commands

  - What is happening on lines 9–12? The program looks to see if the user inputted "Red" and if they did, it will print "correct". If they didn't, it will print "try again"

  - Why are lines 10 and 12 indented? Because they require something in lines 9 and 11 to happen before they can

  - Run the program and answer the question. What happens if you don’t capitalize Red? The program will tell the user that they guessed incorrectly

  - What does this tell you about "color"? It can't automatically detect capitilization

- Open main04.py. Before running it, describe how this is different than main03.py. It allowes an uncapitalized "red" to be correct

  - What problem is this trying to solve? its trying to solve the issue of the user not using a capital letter

  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)? If you use something beside the defined versison of red, it will say the user is incorrect

- Open main05.py. What do you expect line 9 to do? line 9 will make the user's input into lower case

  - What problem is it trying to solve? it solves the problem of the user using weird capitalizations

  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)? it says the user guessed incorrectly

 - Open main06.py. How is line 9 different than in main05.py? line 9 in this one has .strip

   - What would you guess .strip() is doing? i would guess that it strips something

   - Run the program and answer the question. Is there another way of writing “red” that will break this logic? Yes, you can put a space in the middle of the word and it breaks

 - Open main07.py. Before running this program, how do you expect this to be different than main06.py? there is an elif that adds an extra option

   - What is happening on line 12? line 12 adds an elif statement that gives the user extra feedback

 - Open main08.py. What is the purpose of line 9? the purpose is to create a loop in the code

   - Why are lines 10–17 indented? because they will only run while the "while" statement is true

   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)? It wouldn't do anything because line 10 is just a variable

   - Make that change and run the program again. (To end any Python program, you can type ctrl-c) it endlessly outputted an answer and cossed VS Code to crash

 - Open main09.py. What is happening on line 13? Line 13 adds up the amount of times the user has guessed

   - What is the purpose of “count”? the purpose of count is to count

   - What is happening on line 22? nothing happens on line 22 because there is nothing. One line 21 however the program tells the user how many times they guessed

   - Run the program.

 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).

 - *Extra credit:* open main11.py. What is happening on lines 6-11? Line 6 creates the function "choose_color" and defines it as "last_color". Line 7 creates the variable "color" which is defined by a list of colors. line 8 creates the variable "c" which is defined as "random.choice", which in turn is defined as the previous variable of "colors". line 9 creats a while statement that is only true while the variable "c" is equal to the "last_color", and  makes a loops. line 10 makes it so that a random color is chosen, and then line 11 returns the code back up to when "c" was created and it repeats the loop.
  
Commit your changes and push them back to the repository.
 

---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
