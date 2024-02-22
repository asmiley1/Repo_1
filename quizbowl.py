def quiz_bowl():
    # Define a dictionary of questions and answers
    questions_dict = {
        "What is the capital of France?": "Paris",
        "Which planet is known as the Red Planet?": "Mars",
        "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
        "What is the largest mammal in the world?": "Blue Whale",
        "In which year did World War II end?": "1945"
    }

    # Iterate through the questions and ask the user
    for question, correct_answer in questions_dict.items():
        user_answer = input(f"\n{question}\nYour Answer: ")

        # Check if the user's answer is correct
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

# Run the quiz_bowl function
quiz_bowl()

print("Thank you for playing!")