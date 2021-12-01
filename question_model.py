class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def question_return(self):
        return self.text

    def answer_return(self):
        return self.answer
