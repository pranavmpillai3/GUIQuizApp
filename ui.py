from tkinter import *

THEME_COLOR = "#375362"

class UI:

    def __init__(self, qb):
        self.window = Tk()
        self.window.title("GUI QUIZ APP")
        self.window.config(padx=5, pady=5, bg=THEME_COLOR)
        self.canvas = Canvas(height=414, width=300)
        self.ques_img = PhotoImage(file="images/background.png")
        self.canvas.create_image(207, 150, image=self.ques_img)
        self.canvas.config(bg=THEME_COLOR, highlightthickness=0)
        self.q_text = self.canvas.create_text(170, 150, text="texts", width=200, font=("Arial", 15, "bold"), fill="white")
        self.wrng_img = PhotoImage(file='images/false.png')
        self.wrng_button = Button(image=self.wrng_img, command=self.wrng_button_click)
        self.crct_img = PhotoImage(file="images/true.png")
        self.crct_button = Button(image=self.crct_img, command=self.crct_button_click)
        self.crct_button.grid(row=1, column=0)
        self.wrng_button.grid(row=1, column=2)
        self.canvas.grid(row=0, column=1)
        self.usr_ans = 0
        self.qb = qb
        self.qb.next_question(self)

        self.window.mainloop()

    def crct_button_click(self):
        self.usr_ans = True
        self.qb.check_answer(self)

    def wrng_button_click(self):
        self.usr_ans = False
        self.qb.check_answer(self)





