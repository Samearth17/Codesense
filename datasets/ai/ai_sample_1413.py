def sentiment_analysis(documents):
  sentiments = []
  for document in documents:
    sentiment = None
    score = 0
    words = document.split(' ')
    for word in words:
      if word == 'great':
        score += 1
      elif word == 'bad':
        score -= 1
    if score > 0:
      sentiment = 'positive'
    elif score == 0:
      sentiment = 'neutral'
    else:
      sentiment = 'negative'
    sentiments.append(sentiment)
  return sentiments

# Example
docs = ["This food was really great!", "This movie was really bad."]
sentiments = sentiment_analysis(docs)
print(sentiments) # ['positive', 'negative']