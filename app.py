import streamlit as st
from scrape import get_headlines
from analyze import analyze_sentiment
import matplotlib.pyplot as plt

st.set_page_config(page_title="News Sentiment Analyzer", layout="wide")

st.title("📰 News Headline Sentiment Analyzer")
st.caption("Scrapes current Inshorts news headlines across categories and performs sentiment analysis.")

if st.button("Scrape and Analyze"):
    headlines = get_headlines()
    st.success(f"Scraped {len(headlines)} headlines.")

    results, analyzed = analyze_sentiment(headlines)

    # Pie chart
    st.subheader("📊 Sentiment Distribution")
    fig, ax = plt.subplots()
    labels = list(results.keys())
    sizes = list(results.values())
    colors = ['green', 'red', 'grey']

    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    ax.axis('equal')
    st.pyplot(fig)

    # Show headlines by sentiment
    st.subheader("📋 Headlines by Sentiment")

    sentiments = ["positive", "negative", "neutral"]
    for sent in sentiments:
        st.markdown(f"### {sent.title()} Headlines")
        for headline, sentiment in analyzed:
            if sentiment == sent:
                st.write(f"• {headline}")