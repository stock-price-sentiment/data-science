from nltk.sentiment.vader import SentimentIntensityAnalyzer



analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyzer.polarity_scores(sentence)
    print("{}".format(str(score)))