from flask import Flask, jsonify, request, render_template, make_response, Blueprint, redirect, url_for
from blog_control.user_mgmt import User

blog = Blueprint('blog', __name__)

@blog.route('set_info', methods=['GET', 'POST'])
def set_info():
    if request.method == 'POST':
        print("HHHHHHHHHHHHHHHHHHHHHH",request.form)
        user = User.create(request.form['user_email'], request.form['user_passwd'])
        return redirect(url_for('blog.home'))

@blog.route('/home')
def home():
    return render_template('home.html')

@blog.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@blog.route('/login')
def login():
    return render_template('login.html')