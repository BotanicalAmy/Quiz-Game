# what the user in the quiz game will do
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.current_score = 0


user_1 = User("001", "Amy")


print(user_1.current_score)
