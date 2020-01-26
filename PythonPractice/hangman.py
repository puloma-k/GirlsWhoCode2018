#ask for word input
while True:
    word = input("Enter a word: ")
    if word.isalpha() == True:
        break
    else:
        continue

#convert word to lowercase
word = word.lower()

#print empty word
currentWord = []
for letter in word:
    currentWord.append("_")

lettersGuessed = []
triesLeft = 6

while triesLeft > 0:
    guess = input("Guess a letter: ")
    guess = guess.lower()
    if len(guess) > 1:
        continue
    else:
        if guess in lettersGuessed:
            continue
        else:
            lettersGuessed.append(guess)
        print(lettersGuessed)
        index = word.find(guess)
        if guess in word:
            currentWord[index] = guess
            print("Current Word:", currentWord)
        else:
            print("Current Word:", currentWord)
            triesLeft -= 1
        print("Tries Left: ", triesLeft)
