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
        print(polarity)
        return 'Positive'
    elif polarity < 0:
        print(polarity)
        return 'Negative'
    else:
        print(polarity)
        return 'Neutral'


def analyze_from_web(url: str) -> str:
    """

    :param url:
    :return:
    """
    article = Article(url)

    article.download()
    article.parse()
    article.nlp()

    blob = TextBlob(article.text)
    sentiment = blob.sentiment.polarity

    sentiment_category = get_sentiment_category(sentiment)
    # print(sentiment_category)
    return sentiment_category


def analyze_sentence(sentence: str) -> str:
    """

    :param sentence:
    :return:
    """
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity

    sentiment_category = get_sentiment_category(sentiment)
    # print(sentiment_category)
    return sentiment_category


def analyze_doc(file_path: str) -> str:
    with open(file_path, 'r') as file:
        text = file.read()

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    sentiment_category = get_sentiment_category(sentiment)
    # print(sentiment_category)
    return sentiment_category


# Function calls
# analyze_from_web("https://en.wikipedia.org/wiki/Mathematics")
# analyze_sentence("You are mad!")
# analyze_doc(r'../mytext.txt')
