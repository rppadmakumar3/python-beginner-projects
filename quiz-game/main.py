from Controllers.questions import questions

def run_quiz(questions):
    
    score = 0
    
    for question in questions:
        print(question["prompt"])
        for option in question['options']:
            print(option)
        answer = input("Enter Your Answer (A, B, C or D) : ").upper()
        if answer == question['answer']:
            print("Correct Answer\n")
            score += 1
        else:
            print(f"You're Wrong... The Correct Answer is {question['answer']}")
    
    print(f"You Scored {score} out of {len(questions)}")

run_quiz(questions)
        