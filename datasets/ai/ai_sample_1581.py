import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

# Define the preprocessing steps
data_process = Pipeline([
 ('extract_capacity', extract_column('capacity')),
 ('transform_capcity', StandardScaler()),
 ('extract_date', extract_column('date of commission')),
 ('transform_date', YearExtractorTransformer()),
 ('label', BooleanLabelEncoder()),
 ])

# Put the steps together into a pipeline
model = Pipeline([
 ('preprocessing', data_process),
 ('classification', RandomForestClassifier()),
 ])

# Fit and predict labels
model.fit(X_train, y_train)
y_pred = model.predict(X_test)