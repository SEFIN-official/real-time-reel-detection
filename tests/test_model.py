import joblib
import pandas as pd

model = joblib.load('../src/reel_detector_model.pkl')
# Example test
sample = pd.DataFrame([{'packet_size': 2000, 'duration': 15, 'protocol': 0}])
assert model.predict(sample) in [0, 1]
print("Test passed!")
