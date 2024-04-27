from Controllers.french import french_words
import random

def quiz_user(words):
    random.shuffle(words)
    score = 0
    
    for word in words:
        print(f"What is English translation of this French word {word['french']} : ")
        user_input = input("Your Answer : ").strip().lower()
        correct = word['english'].lower()
        
        if user_input == correct:
            print("Correct Answer")
            score += 1
        else:
            print(f"Wrong Answer... Correct Answer is {correct}")
    print(f"You scored {score} out of {len(words)}")

def main():
    print("Welcome to Language Learning App!!!")
    user_answer = input("Press Enter to start the quiz")
    quiz_user(french_words)
    
if __name__ == "__main__":
    main()