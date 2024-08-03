from textblob import TextBlob
from newspaper import Article


def get_sentiment_category(polarity: float) -> str:
    """
    Gets text polarity.

    This function takes the polarity as input and returns a string
    representing the sentiment category of the text. ie postive,
    negative, or neutral

    :param polarity:
        A value which represents the sentiment category
        of a given text.
    :return:
        Polarity (Sentiment)
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
    Analyzes the sentiment of an article(text) from the web.

    This function downloads and processes an article from the provided
    URL and then analyzes its sentiment using TextBlob

    :param url: str
        The URL of the article to analyze
    :return: str
        The sentiment category of the article ie positive, negative or neutral
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
    Analyzes the sentiment of a given sentence.

    This function processes the provided sentence and analyzes its sentiment
    using TextBlob.

    :param sentence: str
        The sentence to analyze
    :return: str
        The sentiment category of the sentence
    """
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity

    sentiment_category = get_sentiment_category(sentiment)
    # print(sentiment_category)
    return sentiment_category


def analyze_doc(file_path: str) -> str:
    """
    Analyzes the sentiment of a given document.

    This function reads the content of a file, processes it, and analyzes
    its sentiment using TextBlob

    :param file_path: str
        The document to analyze
    :return: str
        The sentiment category of the text in the document
    """
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
