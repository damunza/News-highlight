from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    function that returns the index.html page and its content
    '''
    return render_template('index.html')