from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Some question text", fill=THEME_COLOR, font=FONT,
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_img = PhotoImage(file="images/true.png")
        self.right = Button(image=right_img, highlightthickness=0, command=self.is_true)
        self.right.grid(column=0, row=2)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong = Button(image=wrong_img, highlightthickness=0, command=self.is_false)
        self.wrong.grid(column=1, row=2)
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", highlightthickness=0)
        self.score.grid(column=1, row=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Game Over!!\nScore = {self.quiz.score}/10")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")


    def is_true(self):
        is_true = self.quiz.check_answer("True")
        self.give_feedback(is_true)
    def is_false(self):
        is_false = self.quiz.check_answer("False")
        self.give_feedback(is_false)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)

