from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# creating standard scalar object
scaler = StandardScaler()

# loading the dataset
data = load_dataset()

# splitting the dataset into the train and test dataset
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25)  

# standarizing the features
X_train = scaler.fit_transform(X_train)  
X_test = scaler.transform(X_test)

# Creating the model
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)

# training the model
classifier.fit(X_train, y_train)

# predictions
y_pred = classifier.predict(X_test)