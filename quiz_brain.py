import sys
from tkinter import messagebox
import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = self.question_list[0]
        self.usr_answer = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self, gui):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        gui.canvas.itemconfig(gui.q_text, text=html.unescape(self.current_question.question_return()))
        print(self.current_question.answer_return())

    def check_answer(self, gui):
        self.usr_answer = gui.usr_ans
        q_ans = self.current_question.answer_return()
        if (self.usr_answer and q_ans) or (not self.usr_answer and not q_ans):
            self.score += 1
            if self.question_number < len(self.question_list):
                self.next_question(gui)
                print(f"score is {self.score}")
            else:
                print(f"score is {self.score}")
                messagebox.showinfo(title="score", message=f"total score is {self.score}")
                sys.exit()
        else:
            if self.question_number < len(self.question_list):
                self.next_question(gui)
                print(f"score is {self.score}")
            else:
                print(f"score is {self.score}")
                messagebox.showinfo(title="score", message=f"total score is {self.score}")
                sys.exit()
