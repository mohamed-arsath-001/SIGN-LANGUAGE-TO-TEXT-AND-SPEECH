# test_simple.py
import cv2
import numpy as np
from model import model

def test_model():
    try:
        # Load model
        print("Loading model...")
        model = load_model()
        print("Model loaded successfully!")

        # Create a test image
        print("Creating test image...")
        test_image = np.zeros((224, 224, 3), dtype=np.uint8)
        
        # Make prediction
        print("Making prediction...")
        prediction = predict(model, test_image)
        print(f"Prediction: {prediction}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_model()