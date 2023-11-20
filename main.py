# word game

import random

name = 'Wordz'

word_bank = []

with open("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.lower())
        #print(line)

randomWord = random.choice(word_bank)
randomWord = randomWord[:-1]
#rule vars
wrongLocation = []
wrongLetter = []
turns = 10
turnNumber = 0
turnsLeft = turns - turnNumber

displayList = ["-", "-", "-", "-", "-"]

print("Welcome to " , name)
print("There are 5 letters in each word")
print("You have " , str(turnsLeft) , " turns left.")


#main loop
while turnNumber != turns:
    guess = input("What is your guess? ").lower()

    # check length == 5, only letters
    if len(guess) != 5 or not guess.isalpha():
        print("Please enter a 5 letter word")
        continue

    index = 0
    for x in guess:
        if x == randomWord[index]:
            #print(x, end=" ")
            displayList[index] = x

            #print(displayList[0], displayList[1], displayList[2], displayList[3], displayList[4])

            if x in wrongLocation:
                wrongLocation.remove(x)
        elif x in randomWord:
            if x not in wrongLocation:
                wrongLocation.append(x)
            #print("_", end=" ")
            #print(displayList[0], displayList[1], displayList[2], displayList[3], displayList[4])
        else:
            if x not in wrongLetter:
                wrongLetter.append((x))
            #print("_", end=" ")
            #print(displayList[0], displayList[1], displayList[2], displayList[3], displayList[4])

        index += 1
    print(displayList[0], displayList[1], displayList[2], displayList[3], displayList[4])

    print("\n")
    print("Misplaced letters: ", wrongLocation)
    print("Incorrect letters: ", wrongLetter)
    turnNumber += 1

    if ''.join(displayList) == randomWord:#guess == randomWord:
        print("You win!")
        break
    if turnNumber == turns:
        print("You lose!")
        break

    print("You have " , turns - turnNumber , " turns left.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
