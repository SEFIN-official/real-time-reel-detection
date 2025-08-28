import pandas as pd
import joblib

protocol_lookup = {'TCP': 0, 'UDP': 1, 'HTTP': 2, 'UNKNOWN': 3}
network_lookup = {'good': 0, 'medium': 1, 'poor': 2, 'unstable': 3}

model = joblib.load('src/reel_detector_model.pkl')
df = pd.read_csv('data/pcap_features.csv')
df['protocol_code'] = df['protocol'].apply(lambda p: protocol_lookup.get(p, 3))
df['network_code'] = df['network'].apply(lambda n: network_lookup.get(n, 0))
X = df[['packet_size', 'duration', 'protocol_code', 'network_code']]
preds = model.predict(X)
labels = ['reel' if p==1 else 'non-reel' for p in preds]
df['prediction'] = labels
df.to_csv('data/pcap_results.csv', index=False)
print(df[['packet_size', 'protocol', 'prediction']].head(20))  # print first 20 results
