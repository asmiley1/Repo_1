def madlib():
    # Get user inputs
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    # Create the madlib story
    madlib_story = f"Once upon a time, there was a {adjective} {animal} who loved to {verb} in {place}."

    # Display the madlib story
    print("\nYour Madlib Story:")
    print(madlib_story)

# Run the madlib function
madlib()