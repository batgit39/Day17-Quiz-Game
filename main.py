from question_model import Question
from data import question_data
from quiz_brain import QuizBrain 

question_bank = []
for item in question_data:
    question = item["text"]
    answer = item["answer"]
    question_bank.append( Question(question, answer) )

# print(question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've successfully completed the quiz!")
print(f"Your final score was : {quiz.points} / {len(question_bank)}")
