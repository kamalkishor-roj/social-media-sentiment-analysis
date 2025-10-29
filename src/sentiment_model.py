import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

if __name__ == "__main__":
    df = pd.read_csv('data/sample_tweets.csv')
    df['sentiment'] = df['text'].apply(analyze_sentiment)
    df.to_csv('data/tweets_sentiment.csv', index=False)
