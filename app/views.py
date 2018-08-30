from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    function that returns the index.html page and its content
    '''
    title = 'News Live'
    return render_template('index.html', title = title)

   #route to the articles.html page
@app.route('/article/<article_id>')
def article(article_id):
    '''
    function that returns the article.html page and its contect
    '''
    return render_template('article.html',id = article_id)