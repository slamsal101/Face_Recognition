questions =[
    {
        "prompt":"what is the capital of France?",
        "options":["A.Paris","B.London","C.Berlin","D.Madrid"],
        "answer":"A"
    },
    {
        "prompt":"which language is primarily spoken in brazil?",
        "options":["A.Spanish","B.Portuguese","C.English","D.French"],
        "answer":"B"
    },
    {
        "prompt":"what is the smallest prime number?",
        "options":["A.1","B.2","C.3","D.5"],
        "answer":"B" 
    },
    {
        "prompt":"who wrote 'To kill a mocking bird?",
        "options":["A.Harper lee","B.Mark twain","C.JK Rowling","D.Ernest hemingway"],
        "answer":"A"  

    }
]
def run_quitz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A,B,C or D):").upper()
        if answer == question["answer"]:
            print("correct, hooray!!\n")
            score+=1 
        else:
         print("wrong! the correct answer was", question["answer"], "\n")
    print(f"you got {score} out of {len(questions)} questions correct")


           

run_quitz(questions) 