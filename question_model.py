
class QuizQuestion:
    """formats the question into a question and answer"""

    def __init__(self, question_text, question_answer):
        """pull random question from the list"""
        self.text = question_text
        self.answer = question_answer
