from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import sys
from model.model import predict_gesture
import hand_detector
import text_to_speech

# Define paths
current_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(current_dir, 'templates')
static_dir = os.path.join(current_dir, 'static')

# Initialize Flask app with correct paths
app = Flask(__name__)  # No need to specify template_folder if using default 'templates' directory
CORS(app)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Template error: {str(e)}")
        return str(e), 500
    
@app.route('/debug/static-css')
def debug_css():
    return app.send_static_file('backend\static\css\style.css')

@app.route('/debug/static-js')
def debug_js():
    return app.send_static_file('backend\static\js\script.js')

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        image = request.json['image']
        hand_landmarks = hand_detector.detect_hands(image)
        if hand_landmarks:
            gesture = predict_gesture(hand_landmarks)
            return jsonify({'gesture': gesture}), 200
        return jsonify({'gesture': None, 'message': 'No hand detected'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/text-to-speech', methods=['POST'])
def generate_speech():
    try:
        text = request.json['text']
        language = request.json.get('language', 'en')
        audio_file = text_to_speech.text_to_speech(text, language)
        return jsonify({'audio_url': audio_file}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    # Check if templates directory exists
    if not os.path.exists(os.path.join(current_dir, 'templates')):
        os.makedirs(os.path.join(current_dir, 'templates'))
        print("Created templates directory")
    
    # Check if index.html exists
    if not os.path.exists(os.path.join(current_dir, 'templates', 'index.html')):
        # Create a basic index.html if it doesn't exist
        with open(os.path.join(current_dir, 'templates', 'index.html'), 'w') as f:
            f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Language Converter</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <div class="container">
        <h1>Sign Language to Text & Speech Converter</h1>
        
        <div class="video-container">
            <video id="videoElement" autoplay playsinline></video>
            <canvas id="canvasElement"></canvas>
        </div>

        <div class="controls">
            <button id="startBtn">Start Camera</button>
            <button id="stopBtn" disabled>Stop Camera</button>
            <select id="languageSelect">
                <option value="en">English</option>
                <option value="es">Spanish</option>
                <option value="fr">French</option>
            </select>
        </div>

        <div class="output">
            <div class="text-output">
                <h3>Detected Text:</h3>
                <p id="textOutput"></p>
            </div>
            <div class="audio-controls">
                <button id="speakBtn" disabled>Speak Text</button>
                <audio id="audioElement" controls style="display: none;"></audio>
            </div>
        </div>
    </div>
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
            """)
        print("Created index.html template")

    print(f"Current directory: {current_dir}")
    print(f"Template directory: {os.path.join(current_dir, 'templates')}")
    print(f"Available templates: {os.listdir(os.path.join(current_dir, 'templates'))}")
    
    app.run(debug=True, host='127.0.0.1', port=5000)