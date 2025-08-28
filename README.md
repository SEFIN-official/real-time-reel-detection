 Samsung EnnovateX 2025 AI Challenge Submission

## Problem Statement #9
 Real-time Detection of Reel Traffic vs Non-reel Traffic in a Social-networking Application


## Team Name
CodeTrios

## Team Members
SEFIN N A P , Yogasri K , Sowmithra J 
## Demo Video Link
https://www.youtube.com/watch?v=Tmu7z8Jhgeg

---

## Project Overview

This project presents a system for real-time classification of network traffic into *reel* (real-time streaming) and *non-reel* categories. The solution integrates live packet capture with a Random Forest machine learning model deployed via a Flask-SocketIO backend and interactive web dashboard. The system provides continuous traffic predictions alongside intuitive visualizations.

---

## Key Features

- Real-time network packet feature extraction using PyShark.
- Robust Random Forest classifier trained on combined reel and non-reel data.
- Live dashboard UI implemented with Chart.js and Bootstrap for smooth user experience.
- Modular and documented codebase with easy deploy/run instructions.
- Support for live monitoring and historical traffic trend visualization.

---

## Project Artifacts

### Technical Documentation
All technical details including exploratory data analysis, dataset generation, model training, and architecture design are documented in the `/docs` folder in markdown format.  
[View Docs](./docs)

### Source Code
Complete source code is located in the `/src` folder including live capture, feature extraction, prediction utilities, and backend app code.  
[View Source](./src)

### Models
- Model File: `/src/reel_detector_model.pkl`  
- Model Description: Random Forest classifier for reel/non-reel discrimination.  

### Dataset
- Combined Dataset created internally using reel and non-reel PCAP features.
- Synthetic traffic data used for model robustness.

---

## Setup & Usage

1. Clone the repository:
git clone https://github.com/SEFIN-official/real-time-reel-detection.git

text
2. Install libraries:
pip install -r requirements.txt

text
3. Run the backend app:
python app.py

text
4. Open `http://localhost:8080` in your browser to view the dashboard and live traffic predictions.
