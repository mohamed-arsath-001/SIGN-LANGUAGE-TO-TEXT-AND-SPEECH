import pickle
import numpy as np
import os

# Get the directory of the current script (backend/model/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the model file
model_path = os.path.join(current_dir, 'model.p')

# Load the model directly
try:
    with open(model_path, 'rb') as f:
        models = pickle.load(f)
    print(f"Model successfully loaded from: {model_path}")
except FileNotFoundError:
    print(f"Error: Model file not found at {model_path}")
    models = None
except Exception as e:
    print(f"Error loading model: {e}")
    models = None

def predict_gesture(landmarks):
    if models is None:
        print("Error: Models not loaded. Cannot predict.")
        return None

    # Extract features from landmarks
    features = [lm.x for lm in landmarks.landmark] + [lm.y for lm in landmarks.landmark]
    
    # Find the appropriate model and scaler based on feature length
    feature_length = len(features)
    model_key = f"model_{feature_length}"
    scaler_key = f"scaler_{feature_length}"
    
    if model_key in models and scaler_key in models:
        model = models[model_key]
        scaler = models[scaler_key]
        
        features_scaled = scaler.transform([features])
        return model.predict(features_scaled)[0]
    else:
        print(f"Error: No model found for feature length {feature_length}")
        return None

# Print the model path for debugging
print(f"Model path: {model_path}")