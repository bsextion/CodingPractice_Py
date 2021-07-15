secretWord = "Word"
guess = ""
tries = 0
triesMax = 3
reachedMaxTries = False


while guess != secretWord and not(reachedMaxTries):
    if tries < triesMax:
        guess = input("Enter guess: ")
        tries += 1
    else:
        reachedMaxTries = True    


if reachedMaxTries:
    print("You ran out of guesses!")
else:    
    print("You guessed the right word!")
