import urllib.request, json
from .models import Article, Source

api_key = None
source_url = None
article_url = None

def configure_request(app):
    global source_url, article_url, api_key
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_SOURCE_URL']
    article_url = app.config['NEWS_ARTICLE_URL']



def get_sources():

    get_source_url = source_url.format(api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        sources_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_sources(source_results_list)

    return sources_results

def process_sources(source_list):
    '''
    Function  that processes the source results and transform them to a list of objects
    '''

    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')

        source_object = Source(id,name,description,category)

        source_results.append(source_object)

    return source_results


def get_articles(source):
    '''
    Function to get  articles
    '''
    get_articles_url = article_url.format(source,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_articles(article_list):
    '''
    Function that processes the article results and transform them to a list of objects
    ''' 

    article_results = []

    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        urlToImage = article_item.get('urlToImage')
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')

        if publishedAt != None:

            # Call publish_date_format method to convert date to a display-friendly format
            date_to_display = Article.publish_date_format(publishedAt)


            article_object = Article(author,title,urlToImage,description,date_to_display)

            article_results.append(article_object)

    return article_results





