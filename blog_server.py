from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from blog_view import blog
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' # 환경설정
app = Flask(__name__)
CORS(app)
app.secret_key='123abc'

app.register_blueprint(blog.blog, url_prefix='/blog')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)