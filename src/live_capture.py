import pyshark
import time
import logging

logging.basicConfig(level=logging.INFO)

def capture_packet_features(interface='eth0', count=10, timeout=30):
    """
    Capture live packets on specified network interface.
    Returns a list of dicts with packet features.
    """
    cap = pyshark.LiveCapture(interface=interface)
    features = []

    start_time = time.time()
    prev_time = None

    logging.info(f"Starting capture on interface {interface}")

    try:
        for packet in cap.sniff_continuously():
            if len(features) >= count or (time.time() - start_time) > timeout:
                break

            try:
                packet_size = int(packet.length)
                protocol = packet.highest_layer  # e.g., TCP, UDP, HTTP

                # Using difference in packet arrival times as duration feature
                current_time = packet.sniff_time.timestamp()
                duration = current_time - prev_time if prev_time else 0
                prev_time = current_time

                protocol_code = {'TCP': 0, 'HTTP': 1, 'UDP': 2}.get(protocol, 3)
                # Stub for network_code: can be enhanced with real logic later
                network_code = 0  

                feature = {
                    'packet_size': packet_size,
                    'duration': duration,
                    'protocol_code': protocol_code,
                    'network_code': network_code
                }
                features.append(feature)

                logging.debug(f"Captured packet feature: {feature}")

            except Exception as e:
                logging.warning(f"Failed to parse packet: {e}")
                continue

    except Exception as e:
        logging.error(f"Error during packet capture: {e}")

    logging.info(f"Captured {len(features)} packets on {interface}")
    return features

# For standalone test if run as script
if __name__ == "__main__":
    result = capture_packet_features(interface='Wi-Fi', count=5)
    for r in result:
        print(r)
