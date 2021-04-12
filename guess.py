name=input("Enter name here: ")
import time ; time.sleep(5)
print("Fuck you " + name)
print("""______________________ made by
|                           |   
|                           |
|       __________          |
|                           |
|        venxm              |
|       __________          |
|                           |
|___________________________|    

""")
import time ; time.sleep(3)
print("""






""")
import random
random_number = random.randint(1,300)
win = False
Turns =0
while win==False:
    Your_guess = input("Enter a number between 1 and 300: ")
    Turns +=1
    if random_number==int(Your_guess):
        print("You won...but at what cost ")
        print("Number of turns you have used: ",Turns)
        win == True
        break
    else:
     if random_number>int(Your_guess):
        print("Your Guess was low, Please enter a higher number ")
     else:
        print("your guess was high, please enter a lower number ")
       
question = input("Would you like to keep going? [Y/N] ")
if question == "n":
    print("whyyy")
if question == "y":
    print("welcome to sinclairs new game!")
import time ; time.sleep(3)
print("""







""")
import time ; time.sleep(2)
import random

WORD = ('josh', 'poison', 'sinclair', 'food', 'porn', 'butter', 'rich', 'love', 'life', 'two', 'stalker', 'safe', 'folder', 'hacker')
word = random.choice(WORD)
correct = word
clue = word[0] + word[(len(word)-1):(len(word))]
letter_guess = ''
word_guess = ''
store_letter = ''
count = 0
limit = 5

print('Welcome to "Guess the Word Game!"')
print('You have 5 attempts at guessing letters in a word')
print('Let\'s begin!')
print('\n')

while count < limit:
    letter_guess = input('Guess a letter: ')

    if letter_guess in word:
        print('yes!')
        store_letter += letter_guess
        count += 1

    if letter_guess not in word:
        print('no!')
        count += 1

    if count == 2:
        print('\n')
        clue_request = input('Would you like a clue? {Y/N} : ')
        if clue_request == 'y':
            print('\n')
            print('CLUE: The first and last letter of the word is: ', clue)
        if clue_request == 'n':
            print('You\'re something, alright ig!')

print('\n')
print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.')
print('These letters are: ', store_letter)

word_guess = input('Guess the whole word: ')
while word_guess:
    if word_guess.lower() == correct:
        print('Congrats!')
        break

    elif word_guess.lower() != correct:
        print('nah, the answer was ', word)
        break

print('\n')
input('Press Enter to leave the program')
