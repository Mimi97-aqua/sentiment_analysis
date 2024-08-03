from textblob import TextBlob
from newspaper import Article

with open('mytext.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)