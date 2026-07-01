import numpy as np

class NaiveBayesClassifer():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.classes = np.unique(y)

    def fit(self):
        n_samples, n_features = self.x.shape
        self.class_priors = np.zeros(len(self.classes))

        self.means, self.stds = [], []

        # calculate class prior probability
        for i, c in enumerate(self.classes):
            x_class = self.x[self.y == c]
            self.class_priors[i] = x_class.shape[0]/float(n_samples)
            # sample mean and std for each feature
            self.means.append(x_class.mean(axis=0))
            self.stds.append(x_class.std(axis=0))

    def predict(self, X):
        prediction = []
        for x in X:
            posteriors = []
            for i, c in enumerate(self.classes):
                # calculate prior probability
                prior = np.log(self.class_priors[i])
                # calculate conditional probability
                posterior = np.sum(np.log(self.pdf(x, self.means[i], self.stds[i])))
                posteriors.append(prior + posterior)

            # print posteriors
            prediction.append(self.classes[np.argmax(posteriors)])
        return prediction

    # calculate probability density function
    def pdf(self, x, mean, std):
        # probabilities
        probabilities = (1/(np.sqrt(2*np.pi)*std))*(np.exp((-(x-mean)**2)/(2*std**2)))
        return probabilities