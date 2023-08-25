from question_model import Question
from quiz_brain import QuizBrain
import requests
from tkinter import *
from ui import QuizInterface

score = 0
response = requests.get(
    url='https://opentdb.com/api.php?amount=30&type=boolean').json()

question_data = response['results']
question_bank = []

for item in question_data:
    qn = Question(item["question"], item["correct_answer"])
    question_bank.append(qn)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface()
# while quiz.still_has_qns() == True:
#     quiz.NextQuestion()

print("You've completed the quiz")
print(f"Your score is {quiz.score}/{quiz.q_no}!")
