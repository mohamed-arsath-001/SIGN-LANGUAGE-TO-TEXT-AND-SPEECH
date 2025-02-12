# Sign Language to Text and Speech Conversion System

A system designed to convert sign language gestures into text and synthesize the corresponding speech output. This project leverages computer vision, machine learning, and text-to-speech (TTS) technologies to assist in communication for hearing-impaired individuals.


## Features

- **Real-Time Gesture Recognition**: Uses a webcam to detect and interpret sign language gestures in real-time.
- **Text-to-Speech (TTS) Conversion**: Converts recognized text into audible speech.
- **Multi-Language Support**: Supports gestures from multiple sign languages (e.g., ASL, BSL).
- **Customizable Gestures**: Train the model with custom gestures for specialized use cases.
- **Interactive UI**: Simple user interface to display results and control the system.

## Installation

### Prerequisites
- Python 3.6+
- pip package manager

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/sign-language-to-speech.git
   cd sign-language-to-speech

# Install Dependencies:
  pip install -r requirements.txt


# Usage
  Run the Application:
    python src/main.py

    Perform Gestures:

    Stand in front of your webcam and perform sign language gestures.

    The system will display the recognized text on the screen.

    Generate Speech:

    Press S to convert the latest recognized text into speech.

    Train Custom Gestures (Optional):

    Add your gesture images/videos to the data/train/ directory.

    Retrain the model
      python src/train_model.py


# Project Structure

├── src/                   # Source code
│   ├── main.py            # Main application script
│   ├── gesture_recognition.py  # Hand detection and gesture classification
│   └── tts.py             # Text-to-speech conversion logic
├── models/                # Pre-trained ML models
├── data/                  # Datasets and training data
│   ├── train/             # Training images/videos
│   └── test/              # Testing images/videos
├── config/                # Configuration files
├── docs/                  # Documentation
├── requirements.txt       # Dependency list
└── README.md


# Dependencies
  OpenCV - Real-time video processing.

  MediaPipe - Hand tracking and gesture detection.

  TensorFlow/Keras - Gesture classification model.

  PyAudio - Audio playback.

  gTTS or pyttsx3 - Text-to-speech synthesis.



# License
  This project is licensed under the MIT License. See LICENSE for details.



### Future Enhancements
- Expand supported gestures to cover full sign language dictionaries.
- Improve real-time recognition accuracy with advanced models like LSTM or Transformer.
- Develop a mobile-compatible version.
- Add multilingual TTS support (e.g., Spanish, French).

Feel free to ⭐️ the repository if you find this project useful!
