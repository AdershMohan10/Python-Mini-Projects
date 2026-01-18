import random

movies = ["avatar", "lokah", "titanic", "bahubali", "lucifer"]
movie = random.choice(movies)

guessed = ["_"] * len(movie)
attempts = 6

print("\n***# HANGMAN GAME #***\n")

while attempts > 0:
    print("Movie: ", " ".join(guessed))
    print(f"Attempts left: {attempts}")

    guess = input("Enter a letter: ").lower()

    if guess in movie:
        for i in range(len(movie)):
            if movie[i] == guess:
                guessed[i] = guess
        print("Correct!\n")
    else:
        attempts -= 1
        print("Wrong guess!\n")

    if "_" not in guessed:
        print("You Won! The movie was:", movie)
        break

if attempts == 0:
    print("You Lost! The movie was:", movie)
