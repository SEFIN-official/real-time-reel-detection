# Real-Time Reel Traffic Detector

Detects reel video versus non-reel traffic in SNS apps using AI, for real-time device performance optimization.

## How to Run

1. Install requirements:
pip install scikit-learn pandas joblib matplotlib numpy

2. Generate dataset:
- Run `notebooks/generate_dataset.ipynb`

3. Train the model:
- Run `notebooks/train_model.ipynb`

4. Simulate real-time detection:
- Run `python demo/realtime_predict.py`

## Project Structure

- `/data` - Dataset
- `/src` - Source code and saved model
- `/demo` - Demo script

## Open Source License

MIT License
