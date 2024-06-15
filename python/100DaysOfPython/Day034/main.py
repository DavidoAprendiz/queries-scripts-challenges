# Day 34
#

from data import question_model  # Question
from data import all_questions  # question_data/all_questions
from data import quiz_brain  # QuizBrain
from views import gui

question_bank: list = []
for question in all_questions.question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = question_model.Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = quiz_brain.QuizBrain(question_bank)

quiz_ui: gui.QuizInterface = gui.QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

with open("data/HighScores.txt", "w") as file:
    file.write(f"{quiz.highscore}")

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
