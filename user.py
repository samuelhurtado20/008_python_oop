class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email
    
class Estudent (User):
    def __init__(self, username, email, student_id):
        super().__init__(username, email)
        self.student_id = student_id

    def get_student_id(self):
        return self.student_id