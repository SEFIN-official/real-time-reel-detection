# System Architecture

The system consists of three major components:

1. **Live Packet Capture**
   - Implemented using PyShark to capture network packets in real time.
   - Features are extracted on-the-fly and sent for classification.

2. **Backend Prediction Server**
   - Flask-SocketIO server loads the pretrained Random Forest model.
   - Captured features are classified and predictions emitted via WebSocket.

3. **Frontend Dashboard**
   - Displays real-time predictions with dynamic charts and logs.
   - Built using Chart.js and Bootstrap for smooth responsive UI.

Data flows from capture → backend prediction → frontend visualization to provide continuous monitoring.
