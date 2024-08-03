from textblob import TextBlob
from newspaper import Article


def get_sentiment_category(polarity: float) -> str:
    """
    This function takes the polarity as input and returns a string
    representing the sentiment category of the text. ie postive,
    negative, or neutral
    :param polarity: A value which represents the sentiment category
        of a given text.
    :return:
    """
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'


def analyze_from_web(url: str):
    article = Article(url)

    article.download()
    article.parse()
    article.nlp()

    blob = TextBlob(article.text)
    sentiment = blob.sentiment.polarity

    sentiment_category = get_sentiment_category(sentiment)
    print(sentiment_category)




# def analyze_sentence():
#
#
# def analyze_doc():



# Function calls
analyze_from_web("https://en.wikipedia.org/wiki/Mathematics")
