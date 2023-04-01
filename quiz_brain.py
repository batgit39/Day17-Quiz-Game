import os
class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.points = 0

    # to get next question
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q. {self.question_number}: {question.text} (True/False?) : ")
        self.check_answer(answer, question.answer)

    # to get the loop for all questions in the list
    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, users_answer, correct_answer):
        if users_answer.lower() == correct_answer.lower():
            print("You are correct")
            self.points += 1
        else:
            print(f"That's wrong! The correct answer is {correct_answer}")
        os.system('clear')
        print(f"Your current points are :{self.points}/{self.question_number}")


