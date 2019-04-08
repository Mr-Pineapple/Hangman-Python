import random

answerlist = ["goodbye", "hello", "welcome"]

random.shuffle(answerlist)

answer = list(answerlist[0])

#empty list called display
display = []

#adds the variable answer to the display
display.extend(answer)

#iteration of the list called 'display'

for i in range(len(display)):
    #this replaces the letter with an underscore
    display[i] = "_"

#adds a space between the underscores
print(' '.join(display))
print()

#the counter stops the game after every letter has been guessed
count = 0

#reprint until all letters are guessed
while count < len(answer):
    guess = input("Please guess a letter:  ")
    guess = guess.lower()
    print(count)
#iterates through the letters un the answer
    for i in range(len(answer)):
        if answer[i] == guess:
            display[i] = guess
            count = count + 1


    print(' '.join(display))
    print()
print("Well done, you guessed the most simplistic word in the English Dictionary!")
