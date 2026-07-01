import matplotlib.pyplot as plt

# Process the Twitter data to extract
# the relevant data fields
# ...

# Plot the tweet authors
plt.xlabel('Tweet Authors')
plt.ylabel('Number of tweets')
plt.title('Tweet Author Summary')
plt.bar(authors, num_tweets)
plt.show()

# Plot the number of likes
plt.xlabel('Tweets')
plt.ylabel('Number of Likes')
plt.title('Number of Likes Summary')
plt.bar(tweets, num_likes)
plt.show()

# Plot the number of retweets
plt.xlabel('Tweets')
plt.ylabel('Number of Retweets')
plt.title('Number of Retweets Summary')
plt.bar(tweets, num_retweets)
plt.show()