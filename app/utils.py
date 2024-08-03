from textblob import TextBlob
from newspaper import Article


def analyze_from_web(url:str):
    article = Article(url)

    article.download()
    article.parse()
    article.nlp()

    blob = TextBlob(article.text)
    sentiment = blob.sentiment

    print(sentiment)


# def analyze_sentence():
#
#
# def analyze_doc():



# Function calls
analyze_from_web("https://en.wikipedia.org/wiki/Mathematics")