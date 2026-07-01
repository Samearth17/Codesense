# define the data source
data_source = SomeDataSource()

# define the transformer
transformer = SomeTransformer()

# define the model
model = SomeModel()

# define the data pipeline
def data_pipeline(data):
 # pre-process data
 data = transformer.transform(data)
 
 # pass data to model
 model.fit(data)
 
 # return predictions
 predictions = model.predict(data)
 
 return predictions

# execute the data pipeline
predictions = data_pipeline(data_source.get_data())