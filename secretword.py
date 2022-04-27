print("Welcome to the Guessing game")
print("You have 3 tries to guess the word")
secret_word = "giraffe"
guess = ""
guess_count = 0


while guess != secret_word and guess_count < 3:
    guess = input("Enter guess: ")
    if guess == secret_word:
        print("You win!")
    else:
        guess_count += 1
        print("Wrong, try again")
        if guess_count == 3:
            print("You lose")

