import rasa
from rasa.nlu.training_data import load_data
from rasa.nlu.model import Trainer

# Load data
data = load_data('queries_data.json')

# Create a trainer and train the model
trainer = Trainer(rasa.nlu.config.load("config.yml"))
interpreter = trainer.train(data)

# Use the model to predict customer queries
predictions = interpreter.parse('I need a product with high durability')

# Print the prediction results
print(predictions)