import pyshark
import pandas as pd

def extract_features(pcap_file, label, outfile):
    cap = pyshark.FileCapture(pcap_file)
    data = []
    for pkt in cap:
        try:
            size = int(pkt.length)
            protocol = pkt.transport_layer if pkt.transport_layer else 'UNKNOWN'
            timestamp = float(pkt.sniff_time.timestamp())
            # Simple network condition for now
            network = 'good'
            data.append({'packet_size': size, 'protocol': protocol, 'duration': timestamp, 
                         'network': network, 'label': label})
        except Exception:
            continue
    df = pd.DataFrame(data)
    df.to_csv(outfile, index=False)
    print(f'Features extracted and saved to {outfile}')

if __name__ == "__main__":
    extract_features('demo/reel_capture.pcap', 'reel', 'data/reel_features.csv')
    extract_features('demo/nonreel_capture.pcap', 'non-reel', 'data/nonreel_features.csv')
