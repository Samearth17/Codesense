from pylab import *

from statsmodels.tsa.arima_model import ARIMA

# create a dataset
data = [12, 15, 8, 7, 8, 10, 13, 6, 11, 10, 13]

# fit model
model = ARIMA(data, order=(1, 1, 0))
model_fit = model.fit(disp=0)
# print summary of fit model
print(model_fit.summary())
# make prediction
yhat = model_fit.predict(len(data), len(data))
print('Prediction: %f' % yhat)