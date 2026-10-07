import random
def main():
    random_number = random.randint(1,100)

    print("Welcome to number guessing game.")
    print("I am thinking of number between 1 to 100, you have to guess it.")
    print("Please select your deficulty level")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")


    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        print("Great! you have selected the easy dificulty level.")
        print("Let's start the game!")
        chances = 10
    elif user_choice == 2:
        print("Great! you have selected the medium dificulty level.")
        print("Let's start the game!")
        chances = 5
    elif user_choice == 3:
        print(f"Great! you have selected the hard dificulty level.")
        print("Let's start the game!")
        chances = 3

    for attempt in range(chances):
        guess = int(input("Enter your guess: "))
        if guess == random_number:
            print(f"Congratulations! you guessed the right number in {attempt} attempts.")
            break
        elif guess < random_number:
            print(f"Incorrect! the number is greater than {guess}")
        elif guess > random_number:
            print(f"Incorrect! the number is less than {guess}")
    else:
        print("Alas! you lost the game.")


if __name__ == "__main__":
    main()