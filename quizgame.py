questions = [
    {
        "prompt": "Which is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Who wrote the famous play 'Hamlet'?",
        "options": ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Fyodor Dostoevsky"],
        "answer": "A"
    },
    {
        "prompt": "What is the chemical symbol for water?",
        "options": ["A. O2", "B. CO2", "C. H2O", "D. H2SO4"],
        "answer": "C"
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["A. Jupiter", "B. Mars", "C. Venus", "D. Saturn"],
        "answer": "B"
    }
]
def run_quiz(questions):
    score=0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer=input("enter your answer(A, B, C or D):")
        if answer==question["answer"]:
            print("corect\n")    
            score+=1
        else:
            print("wrong answer\n")
        print("your score=",score)
run_quiz(questions)