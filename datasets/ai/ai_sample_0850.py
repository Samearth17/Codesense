import sklearn
import numpy as np

# load the classifier
clf = sklearn.svm.SVC()

# load the pre-trained classifier
with open('classifier.pkl', 'rb') as f:
    clf = pickle.load(f)

def classify_text(texts):
    # compile the inputs into a single array
    data = np.array(texts)
    
    # predict the labels
    labels = clf.predict(data)
    
    return labels

labels = classify_text([
    "This article discusses climate change in Europe.",
    "This article discusses the economic impact of the coronavirus pandemic."
])

print(labels) # -> ['Climate Change', 'Economic Impact']