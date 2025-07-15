# flash_card_quiz.py

# List of questions as dictionaries
questions = [
    {
        "question": "What is the capital of France?",
        "options": {
            "A": "Berlin",
            "B": "Madrid",
            "C": "Paris",
            "D": "Rome"
        },
        "answer": "C"
    },
    {
        "question": "Which language is used to develop Android apps?",
        "options": {
            "A": "Java",
            "B": "Python",
            "C": "Swift",
            "D": "C#"
        },
        "answer": "A"
    },
    {
        "question": "Who is the founder of Microsoft?",
        "options": {
            "A": "Elon Musk",
            "B": "Bill Gates",
            "C": "Steve Jobs",
            "D": "Mark Zuckerberg"
        },
        "answer": "B"
    }
]

# Function to run the quiz
def run_quiz():
    score = 0
    print("\n🎮 Welcome to the Flash Card Quiz!\n")

    for index, q in enumerate(questions, start=1):
        print(f"Q{index}: {q['question']}")
        for key, value in q['options'].items():
            print(f"   {key}: {value}")
        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")

    print(f"🎯 Your final score is: {score}/{len(questions)}")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
