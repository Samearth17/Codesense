import pandas as pd

# read the data file
df = pd.read_csv('movie_data.csv')

# feature engineering
df['action'] = (df['genres'].str.contains('Action')) * 1

# define which features to be used
features_df = df[['action','rating']]

# define the target variable
target = df.popularity

# split data into train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features_df, target, test_size=0.2, random_state=42)

# train a RandomForestRegressor model
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
rf.fit(X_train, y_train)

# make prediction
input_data = {
 'action': 1,
 'rating': 8.5,
 'release_date': '2020-02-10'
}
prediction = rf.predict([input_data])

print(prediction) // Outputs the predicted movie popularity