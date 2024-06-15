# Day 17
# Quiz game
from Day017_GameData import question_data

number_of_questions = len(question_data)
loops = 1
points = 0
user_input = None


class Question:
    def __init__(self, text: str, answer: bool):
        self.text = text
        self.answer = answer


q = {}
for a in range(number_of_questions):
    q[a] = Question(question_data[a]["question"], question_data[a]["correct_answer"])


while number_of_questions > 0:
    while user_input not in ["True", "False"]:
        user_input = input(f"Q.{loops}: {q[number_of_questions - 1].text} (True/False)?: ").capitalize()

    if user_input == q[number_of_questions-1].answer:
        print("Correct!!!  +1 POINT!!!\n")
        points += 1
        loops += 1
        number_of_questions -= 1
        user_input = ""
    else:
        print(f"\nSorry!!!  You lose with {points} points.")
        print(f"Q.{loops}: '{q[number_of_questions - 1].text}' was {q[number_of_questions - 1].answer}  ")
        number_of_questions = 0

#
#
#
#
#
#
#
# Exercise 1)
#
#
# class User:
#
#     def __init__(self, user_id: int, username: str):
#         self.id: int = user_id
#         self.username: str = username
#         self.followers: int = 0
#         self.following: int = 0
#
#     def follow(self, username):
#         if self.id != username.id:
#             self.following += 1
#             username.followers += 1
#
#
# user_1 = User(1, "AAA")
# user_2 = User(2, "BBB")
#
# print(user_1.__dict__)
# print(user_2.__dict__)
#
# user_2.follow(user_1)
# user_2.follow(user_2)
#
# print(user_1.__dict__)
# print(user_2.__dict__)
#
