import pandas as pd
from sklearn.tree import DecisionTreeClassifier 

# Creating pandas dataframe to hold the animal data
animals_df = pd.DataFrame({'Animal': Animals})

# Create target variable Mammal, Bird and Fish
mammals = ['dog', 'cat', 'elephant']
birds = ['owl']
fishes = ['tuna', 'salmon']

animals_df['Mammal'] = animals_df.Animal.apply(lambda x: 1 if x in mammals else 0)
animals_df['Bird'] = animals_df.Animal.apply(lambda x: 1 if x in birds else 0)
animals_df['Fish'] = animals_df.Animal.apply(lambda x: 1 if x in fishes else 0)


# Create the target variable using the code labels
animals_df['target'] = animals_df.Mammal.astype(str) + '_' + animals_df.Bird.astype(str) + '_' + animals_df.Fish.astype(str)

#drop unwanted columns
animals_df.drop(columns = ['Mammal', 'Bird', 'Fish'], inplace=True)

# Create decision tree classifier object
clf = DecisionTreeClassifier()

# Train the model using the data
clf.fit(animals_df[['Animal']], animals_df['target'])