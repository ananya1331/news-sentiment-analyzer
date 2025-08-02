from textblob import TextBlob

def analyze_sentiment(headlines):
    results = {
        "positive": 0,
        "negative": 0,
        "neutral": 0
    }

    analyzed = []

    for headline in headlines:
        blob = TextBlob(headline)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            sentiment = "positive"
        elif polarity < -0.1:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        results[sentiment] += 1
        analyzed.append((headline, sentiment))

    return results, analyzed
