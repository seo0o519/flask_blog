from flask import Flask, jsonify, request, render_template, make_response, Blueprint

blog = Blueprint('blog', __name__)

@blog.route('/home')
def home():
    return render_template('home.html')

@blog.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')
