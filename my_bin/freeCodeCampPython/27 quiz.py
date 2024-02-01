from question import Question

question_prompt =[
    "what is your favourite color?\n(a) red\n(b) green\n(c) blue\n(d) yellow\n",
    "what is your favourite car?\n(a) tesla\n(b) ford\n(c) tata\n(d) bmw\n",
    "what is more important in life?\n(a) money\n(b) love\n(c) power\n(d) affection\n"
]

questions = [
    Question(question_prompt[0],"a"),
    Question(question_prompt[1],"b"),
    Question(question_prompt[2],"c"),
]


def runTest(questions):
    score = 0
    questionLength = len(questions)
    for question in questions:
        answer = input(question.prompt)
        #what in input(quesion.prompt) !!
        if answer == question.answer:
            score +=1
        # print("you got " + str(score) + "/" + str(len(questions)) + " correct")  
        print(f"you got {score}/{questionLength} correct")


runTest(questions)