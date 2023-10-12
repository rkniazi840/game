import random

# Generate a random 4-digit number
def generate_random_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:4]

# Check the user's guess against the random number and count cows and bulls
def check_guess(random_num, user_guess):
    cows = 0
    bulls = 0
    for i in range(4):
        if user_guess[i] == random_num[i]:
            cows += 1
        elif user_guess[i] in random_num:
            bulls += 1
    return cows, bulls

# Main game loop
def main():
    random_num = generate_random_number()
    num_attempts = 0

    print("Welcome to the Cows and Bulls Game!")

    while True:
        user_input = input("Enter a 4-digit number: ")

        # Check if the input is a 4-digit number
        if len(user_input) != 4 or not user_input.isdigit():
            print("Please enter a valid 4-digit number.")
            continue

        num_attempts += 1
        user_guess = [int(digit) for digit in user_input]

        cows, bulls = check_guess(random_num, user_guess)

        print(f"{cows} cow{'s' if cows != 1 else ''}, {bulls} bull{'s' if bulls != 1 else ''}")

        if cows == 4:
            print(f"Congratulations! You've guessed the correct number {user_input} in {num_attempts} attempts.")
            break

if __name__ == "__main__":
    main()
