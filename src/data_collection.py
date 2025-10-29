import pandas as pd
import snscrape.modules.twitter as sntwitter

def scrape_tweets(query, max_tweets=1000):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_tweets:
            break
        tweets.append([tweet.date, tweet.content, tweet.user.username])
    df = pd.DataFrame(tweets, columns=['date', 'text', 'username'])
    return df

if __name__ == "__main__":
    # Example: scrape tweets about 'Python'
    df = scrape_tweets('Python lang:en since:2025-10-01')
    df.to_csv('data/sample_tweets.csv', index=False)
