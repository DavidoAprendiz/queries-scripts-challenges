import html

try:
    with open("./data/HighScores.txt", "r") as file:
        highscore = int(file.read())

except FileNotFoundError:
    with open("./data/HighScores.txt", "w") as file:
        highscore = 0
        file.write(str(highscore))


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.highscore = highscore
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            return f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"
            # user_answer = input(f"Q.{self.question_number}: {html.unescape(self.current_question.text)} (True/False): ")
            # self.check_answer(user_answer)
        else:
            return False

    def check_answer(self, user_answer):

        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            if self.score > self.highscore:
                self.highscore = self.score
            # print("You got it right!")
            return True
        else:
            # print("That's wrong.")
            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
