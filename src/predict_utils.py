import pandas as pd
import joblib

def load_model(model_path='src/reel_detector_model.pkl'):
    """Load and return the trained model."""
    return joblib.load(model_path)

def predict_samples(model, samples):
    """
    Predict labels ('reel' or 'non-reel') for a list of sample dicts.
    
    samples: List of dicts, each dict has keys:
        - packet_size (int)
        - duration (float)
        - protocol_code (int)
        - network_code (int)
    
    Returns list of string labels.
    """
    results = []
    for sample in samples:
        df = pd.DataFrame([sample])
        pred = model.predict(df)[0]
        label = 'reel' if pred == 1 else 'non-reel'
        results.append(label)
    return results
