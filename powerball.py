import random

def generate_powerball():
    # Generate 5 random numbers (1 to 69) for the main numbers
    main_numbers = random.sample(range(1, 70), 5)
    
    # Generate 1 random number (1 to 26) for the Powerball
    powerball_number = random.randint(1, 26)
    
    # Display the Powerball numbers with 4 spaces between Powerball and main numbers
    powerball_ticket = " ".join(map(str, main_numbers)) + "    " + str(powerball_number)
    print("\nYour Powerball Numbers:")
    print(powerball_ticket)

# Ask the user if they want to play again using a while loop
while True:
    generate_powerball()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break