class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q. {self.question_number}: {current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

        # if self.still_has_question() == False:
        #     print("You have completed the quiz")
        #     print(f"your final score is {self.score}")

    score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You go it right")
            self.score += 1
        else:
            print("Wrong Answer")

        print(f"The correct answer was: {correct_answer}")
        print(f"your score is {self.score}\\{self.question_number}")
        print()


# self.question_list_length = len(self.question_list)
