import json

with open("question.json", "r") as f:
    content = f.read()

data = json.loads(content)
score = 0

for question in data:
    print(question["question_text"])
    for index, answers in enumerate(question["alternatives"]):
        print(index + 1, "-", answers)

    while True:
        try:
            user_choice = int(input("Enter your answer: "))
            if 1 <= user_choice <= len(question["alternatives"]):
                break
            else:
                print("❌ Choice out of bounds. Try again.")
        except ValueError:
            print("❌ Please enter a number.")

    question["user_answer"] = user_choice

    if question["user_answer"] == question["correct_answer"]:
        score += 1


for question in data:
    message =  f"Your answer: {question['user_answer']}, "\
               f"correct answer: {question['correct_answer']}"
    print(message)