from flask import render_template
from app import app

from .request import get_source, get_article

@app.route('/')
def index():
    '''
    function that returns the index.html page and its content
    '''
    source = get_source()
    print(source)
    title = 'News Live'
    return render_template('index.html', title = title, source = source)

   #route to the articles.html page
@app.route('/article/<article_id>')
def article(article_id):
    '''
    function that returns the article.html page and its contect
    '''
    article = get_article(article_id)
    print(article)
    title = f'{article_id}'
    return render_template('article.html',id = article_id,title = title,article = article)