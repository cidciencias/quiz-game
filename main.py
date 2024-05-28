from question_model import QuestionModel
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = QuestionModel(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()