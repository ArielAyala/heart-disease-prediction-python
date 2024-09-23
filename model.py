import pandas as pd

# Load the dataset into a pandas DataFrame
data = pd.read_csv('heart-data.csv')

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

# Convert the 'Family' column (categorical) into numerical values using LabelEncoder
data['Family'] = encoder.fit_transform(data['Family'])

# Separate the features (X) and the target variable (y)
# 'X' contains all columns except 'chd' (coronary heart disease)
# 'y' contains the target variable, which is 'chd'
X = data.drop('chd', axis=1)
y = data['chd']

from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
# 70% of the data will be used for training, and 30% will be used for testing
# 'random_state=0' ensures that the split is reproducible
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.ensemble import RandomForestClassifier

# Initialize the RandomForestClassifier
clf = RandomForestClassifier()

# Train the RandomForest model using the training data
clf.fit(X_train, y_train)

# Import the pickle library to save and load trained models
import pickle

# Save the trained model to a file using pickle
# The model is saved as 'heart.pkl' for later use in prediction
pickle.dump(clf, open('heart.pkl', 'wb'))
