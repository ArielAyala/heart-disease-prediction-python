import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_model(model_path='heart.pkl'):
    """Load the trained classification model from a .pkl file."""
    return pickle.load(open(model_path, 'rb'))

def preprocess_input(input_df):
    """Preprocess the input data by applying LabelEncoder to categorical columns."""
    encoder = LabelEncoder()
    input_df['Family'] = encoder.fit_transform(input_df['Family'])
    return input_df[:1]  # Select the first row of input

def make_prediction(model, input_df):
    """Make a prediction using the loaded model."""
    prediction = model.predict(input_df)
    prediction_probability = model.predict_proba(input_df)
    return prediction, prediction_probability
