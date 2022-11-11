class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def get_question(self):
        """Get a quiz question, ask user for a response, tie into the check answer module to check answer"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:  {current_question.text}  True or False?: \n").capitalize()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, guess, answer):
        if guess == answer:
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"You got it wrong.")
        print(f"The correct answer was {answer}.")
        print(f"Your current score is {self.score}/{self.question_number}  \n")
