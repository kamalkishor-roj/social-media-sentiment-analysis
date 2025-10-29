import pandas as pd
from transformers import pipeline

def bert_sentiment_analysis(texts, model_name='nlptown/bert-base-multilingual-uncased-sentiment'):
    sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)
    results = sentiment_pipeline(texts)
    sentiment = []
    for res in results:
        label = res['label']
        if '1 star' in label or '2 stars' in label:
            sentiment.append('negative')
        elif '3 stars' in label:
            sentiment.append('neutral')
        else:
            sentiment.append('positive')
    return sentiment

if __name__ == "__main__":
    df = pd.read_csv('data/sample_tweets.csv')
    texts = df['text'].tolist()
    # If your data is large, consider batching!
    df['bert_sentiment'] = bert_sentiment_analysis(texts)
    df.to_csv('data/tweets_bert_sentiment.csv', index=False)
