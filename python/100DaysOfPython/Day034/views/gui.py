import tkinter as tk
import webbrowser
from Day034.data import quiz_brain
from time import sleep

THEME_COLOR: str = "#375362"
FONT: tuple = ("Arial", 18, "italic")


class QuizInterface:

    def __init__(self, q_list: quiz_brain):
        self.window: tk.Tk = tk.Tk()
        self.window.title("Quiz TBD")
        self.window.config(bg=THEME_COLOR, padx=25, pady=25)
        self.quiz = q_list

        self.lb_score: tk.Label = tk.Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=FONT,
                                           anchor="w")
        self.lb_high_score: tk.Label = tk.Label(text=f"HighScore: {self.quiz.highscore}", bg=THEME_COLOR, fg="white",
                                                font=FONT, anchor="e")
        self.lb_score.grid(row=0, column=1, pady=5)
        self.lb_high_score.grid(row=0, column=0, pady=5)

        self.canvas: tk.Canvas = tk.Canvas(width=350, height=275, bg="white")
        self.question: int = self.canvas.create_text(300, 75, text="Welcome to the new... ERGO QUIZ!!! :D You will not see this", font=FONT,
                                                     fill=THEME_COLOR, anchor="e", width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.get_new_question(self.quiz)

        bt_yes_image: tk.PhotoImage = tk.PhotoImage(file="./data/images/true.png")
        bt_no_image: tk.PhotoImage = tk.PhotoImage(file="./data/images/false.png")
        self.bt_yes: tk.Button = tk.Button(font=FONT, image=bt_yes_image, bg=THEME_COLOR, width=85, height=85,
                                           command=self.correct)
        self.bt_yes.grid(row=2, column=0, pady=5)
        self.bt_no: tk.Button = tk.Button(font=FONT, image=bt_no_image, bg=THEME_COLOR, width=85, height=85,
                                          command=self.incorrect)
        self.bt_no.grid(row=2, column=1, pady=5)

        self.lb_power_by: tk.Label = tk.Label(text=f"⬇️Discover Ergo    ⬇️", bg=THEME_COLOR, fg="white",
                                              font=("Arial", 8, "bold"))
        self.lb_power_by.grid(row=3, column=0, columnspan=2)

        banner_image: tk.PhotoImage = tk.PhotoImage(file="./data/images/ergoplatform_banner.png")
        self.banner: tk.Button = tk.Button(text="abc", font=FONT, image=banner_image, width=330, height=70,
                                           command=lambda: webbrowser.open("https://ergoplatform.org/en/discover/",
                                                                           new=1))
        self.banner.grid(row=4, column=0, columnspan=2)

        self.window.mainloop()

    def correct(self):
        if quiz_brain.QuizBrain.check_answer(self.quiz, "True"):
            self.canvas.config(bg="green")
            self.window.after(1000, lambda: self.get_new_question(self.quiz))
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, lambda: self.get_new_question(self.quiz))

    def incorrect(self):
        if quiz_brain.QuizBrain.check_answer(self.quiz, "False"):
            self.canvas.config(bg="green")
            self.window.after(1000, lambda: self.get_new_question(self.quiz))
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, lambda: self.get_new_question(self.quiz))

    def get_new_question(self, q_list):
        self.lb_score.config(text=f"Score: {self.quiz.score}")
        self.lb_high_score.config(text=f"HighScore: {self.quiz.highscore}")
        # To update the Canvas text
        self.canvas.config(bg="white")
        next_text = quiz_brain.QuizBrain.next_question(q_list)
        if next_text:
            self.canvas.itemconfig(self.question, text=next_text)
        else:
            self.canvas.itemconfig(self.question, text="FINITO!!\nThank you for playing")
            self.bt_yes.config(state="disabled")
            self.bt_no.config(state="disabled")
