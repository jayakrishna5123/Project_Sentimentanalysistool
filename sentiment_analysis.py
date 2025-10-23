from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# ------------------------
# TextBlob-based Analysis
# ------------------------
def analyze_with_textblob(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        label = 'Positive'
    elif polarity < 0:
        label = 'Negative'
    else:
        label = 'Neutral'

    return {
        'method': 'TextBlob',
        'polarity': round(polarity, 3),
        'label': label
    }


# ------------------------
# VADER-based Analysis
# ------------------------
def analyze_with_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        label = 'Positive'
    elif compound <= -0.05:
        label = 'Negative'
    else:
        label = 'Neutral'

    return {
        'method': 'VADER',
        'compound_score': round(compound, 3),
        'label': label
    }


# ------------------------
# Combined Analysis Function
# ------------------------
def analyze_sentiment(text):
    result_textblob = analyze_with_textblob(text)
    result_vader = analyze_with_vader(text)

    return {
        'TextBlob': result_textblob,
        'VADER': result_vader
    }


# ------------------------
# Testing the Function
# ------------------------
if __name__ == "__main__":
    print("Sentiment Analysis Tool (TextBlob + VADER)\n")
    while True:
        text = input("Enter a sentence (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Goodbye!")
            break

        results = analyze_sentiment(text)
        for method, result in results.items():
            score = result.get('polarity') or result.get('compound_score')
            print(f"{method} → Label: {result['label']}, Score: {score}")
        print()
