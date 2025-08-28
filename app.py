import threading
import time
import asyncio
from flask import Flask, render_template
from flask_socketio import SocketIO
import logging
from src.predict_utils import load_model, predict_samples
from src.live_capture import capture_packet_features

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, async_mode='threading')

logging.basicConfig(level=logging.INFO)

model = load_model("src/reel_detector_model.pkl")

def capture_and_emit(interface='Wi-Fi', poll_interval=2):
    """
    Dedicated thread function to capture packets and emit predictions.
    """
    # Create and set event loop explicitly for this thread (needed by pyshark)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    while True:
        try:
            samples = capture_packet_features(interface=interface, count=1, timeout=poll_interval)
            if samples:
                result = predict_samples(model, samples)[0]
                socketio.emit('prediction', {'sample': samples[0], 'label': result})
                logging.info(f"Emitted prediction: {result} for sample {samples[0]}")
            else:
                logging.info("No packets captured in this interval.")
        except Exception as e:
            logging.error(f"Error in capture and emit thread: {e}")
        time.sleep(poll_interval)

@socketio.on('connect')
def on_connect():
    logging.info('Client connected')

    # Start capturing thread once on first client connection
    if not hasattr(app, 'capture_thread'):
        app.capture_thread = threading.Thread(target=capture_and_emit, args=('Wi-Fi', 2), daemon=True)
        app.capture_thread.start()

@socketio.on('disconnect')
def on_disconnect():
    logging.info('Client disconnected')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    logging.info("Starting Flask-SocketIO server on port 8080")
    socketio.run(app, debug=True, port=8080, use_reloader=False)
