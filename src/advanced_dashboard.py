import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px

# Load processed data
df = pd.read_csv('data/tweets_bert_sentiment.csv')
df['date'] = pd.to_datetime(df['date'])

st.title("Advanced Social Media Sentiment Analysis Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
date_range = st.sidebar.date_input("Select Date Range", [df['date'].min(), df['date'].max()])
sentiment_options = st.sidebar.multiselect("Select Sentiments", ['positive', 'neutral', 'negative'], default=['positive', 'neutral', 'negative'])
keyword = st.sidebar.text_input("Keyword Filter", "")

filtered_df = df[
    (df['date'] >= pd.to_datetime(date_range[0])) &
    (df['date'] <= pd.to_datetime(date_range[1])) &
    (df['bert_sentiment'].isin(sentiment_options)) &
    (df['text'].str.contains(keyword, case=False))
]

# Sentiment distribution
st.header("Sentiment Distribution (BERT Model)")
fig1, ax1 = plt.subplots()
sns.countplot(x='bert_sentiment', data=filtered_df, ax=ax1)
st.pyplot(fig1)

# Sentiment trend over time
st.header("Sentiment Trend Over Time")
trend_df = filtered_df.groupby([filtered_df['date'].dt.date, 'bert_sentiment']).size().reset_index(name='count')
fig2 = px.line(trend_df, x='date', y='count', color='bert_sentiment', title='Sentiment Over Time')
st.plotly_chart(fig2)

# Word clouds
st.header("Word Clouds by Sentiment")
for sentiment in sentiment_options:
    st.subheader(f"{sentiment.capitalize()} Tweets")
    text = " ".join(filtered_df[filtered_df['bert_sentiment'] == sentiment]['text'])
    if text:
        wc = WordCloud(width=400, height=200, background_color="white").generate(text)
        st.image(wc.to_array())
    else:
        st.write("No tweets for this sentiment.")

# Sample tweet explorer
st.header("Sample Tweets")
n_samples = st.slider("Number of Tweets", 1, 20, 5)
for i, row in filtered_df.head(n_samples).iterrows():
    st.markdown(f"**{row['date'].strftime('%Y-%m-%d')}** | @{row['username']}")
    st.write(row['text'])
    st.write(f"Sentiment: {row['bert_sentiment']}")
    st.write("---")
