from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier

# define features (height, age) and labels (gender)
X = [[180, 25], [170, 27], [150, 40], [145, 37], [177, 23]]
y = ['male', 'female', 'female', 'male', 'female']

# create model 
svm_model = svm.SVC(gamma='auto', decision_function_shape='ovo')
knn_model = KNeighborsClassifier(n_neighbors=5)

# train and predict
svm_model.fit(X, y)
pred = svm_model.predict([[160, 32]])
knn_model.fit(X, y)
pred_knn = knn_model.predict([[160, 32]])

print(pred)
print(pred_knn)