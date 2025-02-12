let videoElement = document.getElementById('videoElement');
let canvasElement = document.getElementById('canvasElement');
let textOutput = document.getElementById('textOutput');
let startBtn = document.getElementById('startBtn');
let stopBtn = document.getElementById('stopBtn');
let speakBtn = document.getElementById('speakBtn');
let audioElement = document.getElementById('audioElement');
let languageSelect = document.getElementById('languageSelect');

let stream = null;
let isProcessing = false;
const API_URL = 'http://127.0.0.1:5000';

async function startCamera() {
    try {
        stream = await navigator.mediaDevices.getUserMedia({ 
            video: { 
                width: 640,
                height: 480
            } 
        });
        videoElement.srcObject = stream;
        startBtn.disabled = true;
        stopBtn.disabled = false;
        speakBtn.disabled = false;
        startProcessing();
    } catch (err) {
        console.error('Error accessing camera:', err);
        alert('Error accessing camera. Please ensure you have granted camera permissions.');
    }
}

function stopCamera() {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        videoElement.srcObject = null;
        startBtn.disabled = false;
        stopBtn.disabled = true;
        speakBtn.disabled = true;
        isProcessing = false;
    }
}

async function processFrame() {
    if (!isProcessing) return;

    const context = canvasElement.getContext('2d');
    canvasElement.width = videoElement.videoWidth;
    canvasElement.height = videoElement.videoHeight;
    
    context.drawImage(videoElement, 0, 0);
    const imageData = canvasElement.toDataURL('image/jpeg');

    try {
        const response = await fetch(`${API_URL}/api/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: imageData })
        });

        const data = await response.json();
        if (data.gesture) {
            textOutput.textContent = data.gesture;
        }
    } catch (err) {
        console.error('Error processing frame:', err);
    }

    requestAnimationFrame(processFrame);
}

function startProcessing() {
    isProcessing = true;
    processFrame();
}

async function speakText() {
    const text = textOutput.textContent;
    if (!text) return;

    try {
        const response = await fetch(`${API_URL}/api/text-to-speech`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                text: text,
                language: languageSelect.value
            })
        });

        const data = await response.json();
        if (data.audio_url) {
            audioElement.src = data.audio_url;
            audioElement.style.display = 'block';
            audioElement.play();
        }
    } catch (err) {
        console.error('Error generating speech:', err);
        alert('Error generating speech output');
    }
}

startBtn.addEventListener('click', startCamera);
stopBtn.addEventListener('click', stopCamera);
speakBtn.addEventListener('click', speakText);

// Check API health on page load
fetch(`${API_URL}/api/health`)
    .catch(err => {
        console.error('API health check failed:', err);
        alert('Could not connect to the server. Please ensure the backend is running.');
    });