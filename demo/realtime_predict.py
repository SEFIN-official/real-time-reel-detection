import random
from src.predict_utils import load_model, predict_samples

# Load the model from the appropriate file type (.pkl for trained model)
model = load_model("src/reel_detector_model.pkl")

protocol_lookup = {'TCP': 0, 'HTTP': 1, 'UDP': 2}
network_lookup = {'good': 0, 'medium': 1, 'poor': 2}

# Generate random test samples
test_samples = []
for _ in range(5):
    sample = {
        'packet_size': random.randint(400, 3000),
        'duration': random.uniform(1.0, 20.0),
        'protocol_code': random.choice(list(protocol_lookup.values())),
        'network_code': random.choice(list(network_lookup.values()))
    }
    test_samples.append(sample)

# Predict on samples
results = predict_samples(model, test_samples)

# Print predictions
for sample, label in zip(test_samples, results):
    print(f"Input: {sample} => Predicted: {label}")
