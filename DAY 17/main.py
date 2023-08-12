from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
                                  
quesion_bank=[]
for item in question_data:
    qn=Question(item["question"],item["correct_answer"])
    quesion_bank.append(qn)

quiz=QuizBrain(quesion_bank)
while quiz.still_has_qns()==True:
    quiz.NextQuestion()

print("You've completed the quiz")
print(f"Your score is {quiz.score}/{quiz.q_no}!")