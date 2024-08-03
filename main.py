from textblob import TextBlob
from newspaper import Article

url = 'https://en.wikipedia.org/wiki/Mathematics'
article = Article(url)

article.download()  # to get it into the Script
article.parse()  # to remove the html
article.nlp()  # to make it ready for nlp

# text_blob = TextBlob(article.text)
# sentiment = text_blob.sentiment

text = article.summary
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)