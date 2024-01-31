from flask_login import UserMixin
from blog_data.mysql import conn_mysqldb

class User(UserMixin): # UserMixin class 상속받음
    def __init__(self, user_id, user_email, user_passwd):
        self.id = user_id # id는 flask_login 코드 안에서도 access하기 때문에 이름 바꾸면 안됨
        self.user_email = user_email
        self.user_passwd = user_passwd

    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get(user_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_infomation WHERE USER_ID = '" + str(user_id) + "'"
        user = db_cursor.fetchone()
        if not user:
            return None
        
        user = User(user_id=user[0], user_email=user[1], user_passwd=user[2])
        return user
    
    @staticmethod
    def find(user_email):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM user_information WHERE USER_EMAIL = '" + str(user_email) + "'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            return None
        user = User(user_id=user[0], user_email=user[1], user_passwd=user[2])
        return user
    
    @staticmethod
    def create(user_email, user_passwd):
        user = User.find(user_email)
        if user==None:
            mysql_db = conn_mysqldb()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO user_information (USER_EMAIL, USER_PASSWD) VALUES ('%s', '%s')" % (str(user_email), str(user_passwd))
            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(user_email)
        else:
            return user