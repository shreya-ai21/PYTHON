from tkinter import *


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg='#375362')
        self.score()
        self.qnwindow()
        self.check()
        self.window.mainloop()

    def score(self):
        sc = 0
        score = Label(text=f"Score:{sc}", bg='#375362', fg='white', font=(
            'Arial', 20, 'italic'))
        score.grid(row=0, column=2)

    def qnwindow(self):
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.create_text(100, 150, text='hi', font=(
            'Arial', 20, 'italic'), fill='white')
        self.canvas.grid(row=6, column=0, columnspan=3)

    def check(self):
        check = Button(text='✅', width=500, height=500)
        check.grid(row=7, column=0)
