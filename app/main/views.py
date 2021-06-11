from flask import Flask
from . import main
from ..request import get_sources , get_articles


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources()
    return render_template('index.html',sources=sources)

@main.route('/source/<source_id>')
# def source(source_id):
#     '''
#     View source page function that returns a source page 
#     '''
#     title = f"{source_id} page"
#     articles = get_articles(source_id)
#     return render_template('articles.html', title=title, articles=articles)
