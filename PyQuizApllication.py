# Define a list of questions, each with options and correct answers
questions = [
    {
        "question": "Who is the creator of the Python programming language?",
        "options": ["Larry Page", "Guido van Rossum", "Dennis Ritchie", "James Gosling"],
        "correct_answer": "Guido van Rossum"
    },
    {
        "question": "Which of the following is NOT a valid Python variable name?",
        "options": ["my_variable", "123variable", "_variable", "variable123"],
        "correct_answer": "123variable"
    },
    {
        "question": "Which of the following data types is mutable in Python?",
        "options": ["int","str","list","tuple"],
        "correct_answer": "list"
    },
    {
        "question": "Which of the following statements is used to exit a loop prematurely in Python?",
        "options": ["stop","exit","end","break"],
        "correct_answer": "break"
    },
    {
        "question": "What is the result of the expression 3 ** 2 in Python?",
        "options": ["9","6","27","5"],
        "correct_answer": "9"
    },
    
]


# Initialize the score
score = 0

# Loop through the questions
for question in questions:
    # Display the question and options
    print(question["question"])
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")
    
    # Get the user's answer
    user_answer = input("Enter the number of your answer (1, 2, 3, or 4): ")
    
    # Check if the user's answer is correct
    if user_answer == str(question["options"].index(question["correct_answer"]) + 1):
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question['correct_answer']}.\n")

# Display the final score
print("--------------------------------------------")
print(f"Your final score is {score}/{len(questions)}.")
print("--------------------------------------------")
