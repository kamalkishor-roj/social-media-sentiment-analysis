# Social Media Sentiment Analysis

**Author:** KamalKishor Roj

This project demonstrates advanced sentiment analysis of social media (Twitter/X) posts about brands, events, or topics. It uses multiple methods (TextBlob, VADER, BERT) and interactive dashboards to deliver business-ready insights.

## Features

- Data collection via scraping or public datasets
- Data cleaning and preprocessing
- Sentiment analysis with TextBlob, VADER, and BERT
- Trend analysis over time
- Word clouds for each sentiment
- Topic modeling (optional)
- Interactive Streamlit dashboard
- Business insights report

## Setup

```bash
pip install -r requirements.txt
```

## Usage

1. **Add or update your data:**  
   Place your CSV file in the `data/` folder, named as `your_tweets.csv`.  
   The CSV should have columns: `date`, `text`, `username`.  
   To use your own dataset, replace `sample_tweets.csv` with your file and update the scripts to use its name.

2. **Run sentiment analysis scripts:**  
   ```
   python src/sentiment_model.py
   python src/bert_sentiment.py
   ```

3. **Launch the dashboard:**  
   ```
   streamlit run src/advanced_dashboard.py
   ```

## Data Sources

- [Kaggle Twitter Sentiment Datasets](https://www.kaggle.com/datasets)
- [snscrape Documentation](https://github.com/JustAnotherArchivist/snscrape)

## Updating the Dataset

- To analyze new data:  
  - Replace `data/sample_tweets.csv` with your new data file (`date`, `text`, `username` columns).
  - Update script paths if needed.
  - Rerun the sentiment scripts, then launch the dashboard.

## Portfolio Tips

- Add screenshots of your dashboard and insights.
- Document key findings and recommendations in `reports/business_insights.md`.

---

**Enjoy exploring social media sentiment with advanced analytics!**
