from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Load the data
data = pd.read_csv('credit_default.csv')

# Separate the features and target
X = data.drop('default', axis=1)
y = data['default']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Scale the data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict the target
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print('Model accuracy: {:.2f}%'.format(accuracy*100))