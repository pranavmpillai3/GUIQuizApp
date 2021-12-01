from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import *


question_bank = []
api_end = 'https://opentdb.com/api.php?amount=20&category=18&type=boolean'
response = requests.get(api_end)

question_data = response.json()['results']
print(question_data)
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
user_intf = UI(quiz)

