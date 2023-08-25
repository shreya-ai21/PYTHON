import html


class QuizBrain:
    def __init__(self, q_list):
        self.q_no = 0
        self.q_list = q_list
        self.score = 0

    def NextQuestion(self):
        current = self.q_list[self.q_no]
        current.text = html.unescape(current.text)
        self.q_no += 1
        user_answer = input(f"Q{self.q_no}.{current.text}True or false?")
        correct = current.answer
        self.check_answer(user_answer, correct)

    def still_has_qns(self):
        return self.q_no < len(self.q_list)

    def check_answer(self, user_answer: str, correct: str):
        if correct.upper() == user_answer.upper():
            print("You got it right!")
            self.score += 1
            print(f"Your score is {self.score}/{self.q_no}\n")
        else:
            print("You got it wrong")
            print(f"The correct answer was {correct}")
            print(f"Your score is {self.score}/{self.q_no}\n")
