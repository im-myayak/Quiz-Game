import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(self.window, text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.q_container = Canvas(self.window, width=300, height=250)
        self.question_text = self.q_container.create_text(150,
                                                          125,
                                                          width=280,
                                                          text="Some questions texts",
                                                          font=("Arial", 20, "italic"))
        self.q_container.grid(row=1, column=0, columnspan=2, pady=50)
        img1 = PhotoImage(file="images/true.png")
        self.true_btn_img = Button(self.window, image=img1, highlightthickness=0, command=self.true_button)
        self.true_btn_img.grid(row=2, column=0, )
        img = PhotoImage(file="images/false.png")
        self.false_btn_img = Button(self.window, image=img, highlightthickness=0, command=self.false_button)
        self.false_btn_img.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.q_container.configure(bg="white")
            next_question = self.quiz.next_question()
            self.q_container.itemconfig(self.question_text, text=next_question)
        else:
            self.q_container.itemconfig(self.question_text, text="Quiz Completed")
            self.false_btn_img.config(state=DISABLED)
            self.true_btn_img.config(state=DISABLED)


    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, response):
        if response:
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            self.q_container.configure(bg="green")
        else:
            self.q_container.configure(bg="red")

        self.window.after(1000, self.get_next_question)
