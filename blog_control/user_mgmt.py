from flask_login import UserMixin
from blog_data.mysql import conn_mysqldb

class User(UserMixin): # UserMixin class 상속받음
    def __init__(self, user_id, user_email, user_pw):
        self.id = user_id # id는 flask_login 코드 안에서도 access하기 때문에 이름 바꾸면 안됨
        self.user_email = user_email
        self.user_pw = user_pw

    def get_id(self):
        return str(self.id)