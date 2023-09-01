from data import question_data
from question_model import Question

question_bank = []

for get_question in question_data:
    q_text= get_question["text"]
    q_answer = get_question["answer"]

    new_question = Question(q_text,q_answer)
    question_bank.append(new_question)


